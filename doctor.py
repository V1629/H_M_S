class Doctor:
    def __init__(self, name,doctor_id, speciality,availability):
        self.name = name
        self.doctor_id = doctor_id
        self.speciality = speciality
        self.availability = availability

    def view_details(self):
        return f"Name: {self.name}, Doctor ID: {self.doctor_id}, Speciality:{ self.speciality }"
    
    def view_availability(self,new_slots):
        self.availability = new_slots

