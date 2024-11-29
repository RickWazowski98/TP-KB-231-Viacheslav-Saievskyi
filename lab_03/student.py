
class Student:
    def __init__(self, name, phone, gender, details):
        self.name = name
        self.phone = phone
        self.gender = gender
        self.details = details

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Gender: {self.gender}, Details: {self.details}"

    def update(self, name=None, phone=None, gender=None, details=None):
        if name:
            self.name = name
        if phone:
            self.phone = phone
        if gender:
            self.gender = gender
        if details:
            self.details = details
