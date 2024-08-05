import os
import random
import pandas as pd

num_patients = 1000

from typing import Dict

ehr_schema: Dict[str, list] = {
    "patient_id": [],
    "name": [],
    "date_of_birth": [],
    "sex": [],
    "medical_history": [],
    "medications": [],
    "allergies": []
}

medical_imaging_schema: Dict[str, list] = {
    "patient_id": [],
    "image_type": [],
    "image_data": [],
}

genomic_schema: Dict[str, list] = {
    "patient_id": [],
    "gene_name": [],
    "variant_id": [],
    "genotype": [],
}


# Generate EHR data
for i in range(num_patients):
    ehr_schema["patient_id"].append(f"patient_{i}")
    ehr_schema["name"].append(f"John Doe_{i}")
    ehr_schema["date_of_birth"].append(f"1990-01-01")
    ehr_schema["sex"].append(random.choice(["Male", "Female"]))
    ehr_schema["medical_history"].append(random.choice(["Diabetes", "Hypertension", "None"]))
    ehr_schema["medications"].append(random.choice(["Aspirin", "Lisinopril", "None"]))
    ehr_schema["allergies"].append(random.choice(["Penicillin", "None"]))


# Generate Medical Imaging data
for i in range(num_patients):
    patient_id = f"patient_{i}"
    medical_imaging_schema["patient_id"].append(patient_id)
    medical_imaging_schema["image_type"].append(random.choice(["X-ray", "CT Scan", "MRI"]))
    medical_imaging_schema["image_data"].append(f"Image data for {patient_id}")


# Generate Genomic data
for i in range(num_patients):
    genomic_schema["patient_id"].append(f"patient_{i}")
    genomic_schema["gene_name"].append(random.choice(["BRCA1", "BRCA2", "TP53"]))
    genomic_schema["variant_id"].append(random.choice(["rs123456", "rs789012", "rs345678"]))
    genomic_schema["genotype"].append(random.choice(["AA", "AG", "GG"]))


# Create Pandas DataFrames
ehr_df = pd.DataFrame(ehr_schema)
medical_imaging_df = pd.DataFrame(medical_imaging_schema)
genomic_df = pd.DataFrame(genomic_schema)


output_dir = "./data"
ehr_dir = os.path.join(output_dir, "ehr")
medical_imaging_dir = os.path.join(output_dir, "medical_imaging")
genomic_dir = os.path.join(output_dir, "genomic")

# Create the output directories if they don't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
if not os.path.exists(ehr_dir):
    os.makedirs(ehr_dir)
if not os.path.exists(medical_imaging_dir):
    os.makedirs(medical_imaging_dir)
if not os.path.exists(genomic_dir):
    os.makedirs(genomic_dir)

# Save the DataFrames to CSV files
ehr_df.to_csv(os.path.join(ehr_dir, "ehr_data.csv"), index=False)
medical_imaging_df.to_csv(os.path.join(medical_imaging_dir, "medical_imaging_data.csv"), index=False)
genomic_df.to_csv(os.path.join(genomic_dir, "genomic_data.csv"), index=False)