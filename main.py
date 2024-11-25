from doctor import Doctor
from patient import Patient

# Create a Doctor
doctor1 = Doctor("Alice", "Cardiology", 101, ["10:00 AM", "2:00 PM"])

# Create a Patient
patient1 = Patient("Vaibhav Mishra", 45, "Male","Dr. Alice","heart problem")

# Admit the patient to the doctor
patient1.admit(doctor1, "Hypertension")

# Print patient details before discharge
print("Before Discharge:", patient1.view_details())

# Discharge the patient
patient1.discharge()

# Print patient details after discharge
print("After Discharge:", patient1.view_details())
