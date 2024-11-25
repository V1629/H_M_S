class Patient:
    def __init__(self, name, age, gender,admitted_doctor,diagnosis):
        self.name = name
        self.age = age
        self.gender = gender
        self.admitted_doctor = None
        self.diagnosis = None

    def admit(self,doctor,diagnosis):
        self.admitted_doctor = doctor
        self.diagnosis = diagnosis

    def discharge(self):
        self.admitted_doctor = None
        self.diagnosis = None

    def view_details(self):
        doctor_name = self.admitted_doctor.name if self.admitted_doctor else "no doctor assigned"
        return f"Patient {self.name}, Age: {self.age}, Doctor: {doctor_name}"


    