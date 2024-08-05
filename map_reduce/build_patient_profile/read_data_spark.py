from pyspark.sql import SparkSession
from pyspark.sql.functions import col, struct, collect_list, lit, to_json
from pyspark.sql.types import StructType, StructField, StringType
import os
import multiprocessing

# determines the number of cores available on the machine
num_cores = multiprocessing.cpu_count()

# Initialize Spark session
spark = (
    SparkSession.builder.appName("PatientProfileMapReduce")
    .config("spark.mongodb.input.uri", "mongodb://localhost:27017/")
    .config("spark.mongodb.output.uri", "mongodb://localhost:27017/")
    .config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:3.0.1")
    .config("spark.driver.cores", 1)
    .config("spark.executor.cores", num_cores - 1)
    .config("spark.cores.max", num_cores)
    .getOrCreate()
)


# Function to read CSV files
def read_csv_files(directory):
    dataframes = []
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            file_path = os.path.join(directory, filename)
            df = spark.read.csv(file_path, header=True, inferSchema=True)
            data_type = filename.split(".")[0]  # Assuming filename indicates data type
            df = df.select(col("patient_id"), to_json(struct("*")).alias("data"))
            df = df.withColumn("data_type", lit(data_type))
            dataframes.append(df)
    return dataframes


# Read all CSV files
ehr_data = read_csv_files("./data/ehr")
imaging_data = read_csv_files("./data/medical_imaging")
genomic_data = read_csv_files("./data/genomic")

all_data = ehr_data + imaging_data + genomic_data

combined_data = spark.createDataFrame(
    spark.sparkContext.emptyRDD(),
    StructType(
        [
            StructField("patient_id", StringType(), True),
            StructField("data", StringType(), True),
            StructField("data_type", StringType(), True),
        ]
    ),
)

for df in all_data:
    combined_data = combined_data.union(df)

# Repartition the data
combined_data = combined_data.repartition(num_cores, "patient_id")

# Group by patient_id and collect all data
patient_profiles = combined_data.groupBy("patient_id").agg(
    collect_list(struct("data_type", "data")).alias("profile_data")
)

# Save the result to MongoDB
patient_profiles.write.format("com.mongodb.spark.sql.DefaultSource").option(
    "uri", "mongodb://localhost:27017/medical_db.patient"
).save()
# Stop the Spark session
spark.stop()
