from pymongo import MongoClient
import json
import argparse


class PatientProfileDatabase:
    def __init__(self, connection_string="mongodb://localhost:27017/"):
        self.client = MongoClient(connection_string)
        self.db = self.client.medical_db
        self.profiles = self.db.patient

    def get_patient_profile(self, patient_id):
        profile = self.profiles.find_one({"patient_id": patient_id})
        if profile:
            # Parse the JSON strings in the profile data
            for item in profile["profile_data"]:
                item["data"] = json.loads(item["data"])
        return profile

    def close(self):
        self.client.close()


def print_profile(profile, patient_id):
    if profile:
        print(f"Patient {patient_id} profile:")
        for item in profile["profile_data"]:
            print(f"{item['data_type']}:")
            print(json.dumps(item["data"], indent=2))
    else:
        print(f"No profile found for patient {patient_id}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Retrieve patient profile from MongoDB."
    )
    parser.add_argument(
        "--patient_id", type=str, required=True, help="The patient ID to retrieve"
    )
    args = parser.parse_args()

    db = PatientProfileDatabase()

    try:
        profile = db.get_patient_profile(args.patient_id)
        print_profile(profile, args.patient_id)
    finally:
        db.close()
