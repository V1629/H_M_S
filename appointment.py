from doctor import Doctor
class Appointment:
    def __init__(self, appointment_id, patient, doctor, appointment_time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.appointment_time = appointment_time

    def schedule(self):
        if self.appointment_time in self.doctor.availability:
            print(f"Appointment scheduled for {self.patient.name} with Dr. {self.doctor.name} at {self.appointment_time}")
        else:
            print(f"Error: Dr. {self.doctor.name} is not available at {self.appointment_time}. Please choose another time.")

    def view_details(self):
        return f"Appointment ID: {self.appointment_id}, Patient: {self.patient.name}, Doctor: Dr. {self.doctor.name}, Time: {self.appointment_time}"
