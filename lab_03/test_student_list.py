
import unittest
from lab_03.student import Student
from lab_03.student_list import StudentList

class TestStudentList(unittest.TestCase):
    def setUp(self):
        self.student_list = StudentList()
        self.student1 = Student("Alice", "1234567890", "Female", "First year")
        self.student2 = Student("Bob", "0987654321", "Male", "Second year")
        self.student_list.add_student(self.student1)
        self.student_list.add_student(self.student2)

    def test_add_student(self):
        self.assertEqual(len(self.student_list.students), 2)
        self.student_list.add_student(Student("Charlie", "1122334455", "Male", "Third year"))
        self.assertEqual(len(self.student_list.students), 3)

    def test_delete_student(self):
        self.student_list.delete_student("Bob")
        self.assertEqual(len(self.student_list.students), 1)

    def test_update_student(self):
        self.student_list.update_student("Alice", new_phone="1112223333", new_details="Updated details")
        self.assertEqual(self.student1.phone, "1112223333")
        self.assertEqual(self.student1.details, "Updated details")

    def test_save_and_load_csv(self):
        self.student_list.save_to_csv("students_test.csv")
        new_list = StudentList()
        new_list.load_from_csv("students_test.csv")
        self.assertEqual(len(new_list.students), 2)

if __name__ == "__main__":
    unittest.main()
