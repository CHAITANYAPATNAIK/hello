class Patient:
    def __init__(self, patient_id, name):
        self.patient_id = patient_id
        self.name = name
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_latest_record(self):
        return self.records[-1] if self.records else "No records found."
class HealthRecord:
    def __init__(self, date, symptoms, diagnosis, treatment):
        self.date = date
        self.symptoms = symptoms
        self.diagnosis = diagnosis
        self.treatment = treatment
    def __str__(self):
        return (f"Date: {self.date}\n"
                f"Symptoms: {self.symptoms}\n"
                f"Diagnosis: {self.diagnosis}\n"
                f"Treatment: {self.treatment}\n")
def display_patient_record(patient):
    print(f"Patient ID: {patient.patient_id}")
    print(f"Name: {patient.name}")
    print("Latest Health Record:")
    print(patient.get_latest_record())
def main():
    patients = {}
    
    while True:
        print("\n--- Automatic Health Monitoring System ---")
        print("1. Add Patient")
        print("2. Add Health Record")
        print("3. View Patient Record")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            patient_id = input("Enter Patient ID: ")
            name = input("Enter Patient Name: ")
            if patient_id not in patients:
                patients[patient_id] = Patient(patient_id, name)
                print("Patient added successfully.")
            else:
                print("Patient ID already exists.")
        elif choice == '2':
            patient_id = input("Enter Patient ID: ")
            if patient_id in patients:
                date = input("Enter Date (YYYY-MM-DD): ")
                symptoms = input("Enter Symptoms: ")
                diagnosis = input("Enter Diagnosis: ")
                treatment = input("Enter Treatment: ")
                record = HealthRecord(date, symptoms, diagnosis, treatment)
                patients[patient_id].add_record(record)
                print("Health record added successfully.")
            else:
                print("Patient ID not found.")
        
        elif choice == '3':
            patient_id = input("Enter Patient ID: ")
            if patient_id in patients:
                display_patient_record(patients[patient_id])
            else:
                print("Patient ID not found.")
        
        elif choice == '4':
            print("Exiting system.")
            break
        
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
