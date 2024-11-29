
from lab_03.student import Student
from lab_03.student_list import StudentList
from lab_03.utils import Utils

def main():
    student_list = StudentList()
    filename = "students.csv"

    # Завантаження даних з файлу
    Utils.load_data_from_csv(student_list, filename)

    while True:
        action = input("Choose action: [C]reate, [U]pdate, [D]elete, [P]rint, [S]ave, [X]exit: ")

        if action.lower() == 'c':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            gender = input("Enter gender: ")
            details = input("Enter details: ")
            student = Student(name, phone, gender, details)
            student_list.add_student(student)

        elif action.lower() == 'u':
            name = input("Enter name of the student to update: ")
            new_name = input("Enter new name (leave blank to keep current): ")
            new_phone = input("Enter new phone (leave blank to keep current): ")
            new_gender = input("Enter new gender (leave blank to keep current): ")
            new_details = input("Enter new details (leave blank to keep current): ")
            student_list.update_student(name, new_name or None, new_phone or None, new_gender or None, new_details or None)

        elif action.lower() == 'd':
            name = input("Enter name of the student to delete: ")
            student_list.delete_student(name)

        elif action.lower() == 'p':
            student_list.print_students()

        elif action.lower() == 's':
            Utils.save_data_to_csv(student_list, filename)
            print("Data saved to CSV.")

        elif action.lower() == 'x':
            Utils.save_data_to_csv(student_list, filename)
            print("Exiting and saving data.")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
