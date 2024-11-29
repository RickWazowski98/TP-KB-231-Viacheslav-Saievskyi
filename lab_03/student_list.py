
from lab_03.student import Student

class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        self.students.sort(key=lambda student: student.name)

    def delete_student(self, name):
        student = self.find_student_by_name(name)
        if student:
            self.students.remove(student)
        else:
            print(f"Student {name} not found")

    def update_student(self, name, new_name=None, new_phone=None, new_gender=None, new_details=None):
        student = self.find_student_by_name(name)
        if student:
            student.update(new_name, new_phone, new_gender, new_details)
        else:
            print(f"Student {name} not found")

    def find_student_by_name(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None

    def print_students(self):
        for student in self.students:
            print(student)

    def save_to_csv(self, filename):
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            import csv
            writer = csv.writer(file, delimiter=',')
            writer.writerow(["Name", "Phone", "Gender", "Details"])
            for student in self.students:
                writer.writerow([student.name, student.phone, student.gender, student.details])

    def load_from_csv(self, filename):
        import csv
        try:
            with open(filename, 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file, delimiter=',')
                next(reader)  # Skip header
                for row in reader:
                    name, phone, gender, details = row
                    student = Student(name, phone, gender, details)
                    self.add_student(student)
        except FileNotFoundError:
            print(f"File {filename} not found.")
