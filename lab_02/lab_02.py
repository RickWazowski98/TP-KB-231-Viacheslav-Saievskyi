import csv
import sys

students = []

def load_data_from_csv(filename, students=students):
    """
    Завантаження даних з CSV файлу.
    """
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=',')
            if reader.fieldnames != ["name", "phone", "gender", "details"]:
                raise ValueError("Incorrect CSV format. Expected columns: name,phone,gender,details.")
            for row in reader:
                students.append({
                    "name": row["name"],
                    "phone": row["phone"],
                    "gender": row["gender"],
                    "details": row["details"]
                })
        print(f"Data successfully loaded from {filename}.")
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with an empty directory.")
    except ValueError as e:
        print(f"Error loading file: {e}. Starting with an empty directory.")
    except Exception as e:
        print(f"An unexpected error occurred while loading the file: {e}. Starting with an empty directory.")

def save_data_to_csv(filename, students=students):
    """
    Збереження даних у CSV файл.
    """
    if not students:
        print("No data to save. File will not be modified.")
        return

    try:
        with open(filename, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "phone", "gender", "details"], delimiter=',')
            writer.writeheader()
            writer.writerows(students)
        print(f"Data successfully saved to {filename}.")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")

def print_all_students(students=students):
    """
    Виводить всю інформацію про студентів.
    """
    if not students:
        print("No students in the directory.")
        return

    for student in students:
        print(f"Name: {student['name']}, Phone: {student['phone']}, Gender: {student['gender']}, Details: {student['details']}")
    return

def add_new_student(name=None, phone=None, gender=None, details=None, students=students):
    """
    Додає нового студента в список, зберігаючи сортування.
    """
    if name==None:
        name = input("Please enter student name: ")
        phone = input("Please enter student phone: ")
        gender = input("Please enter student gender (Male/Female): ")
        details = input("Please enter additional details about student: ")

    new_student = {"name": name, "phone": phone, "gender": gender, "details": details}

    # Знаходимо позицію для вставки
    insert_position = 0
    for student in students:
        if name > student["name"]:
            insert_position += 1
        else:
            break

    students.insert(insert_position, new_student)
    print("New student has been added successfully!")
    return

def delete_student(name=None, students=students):
    """
    Видаляє студента зі списку за ім'ям.
    """
    if name == None:
        name = input("Please enter name to be deleted: ")
    delete_position = -1
    for student in students:
        if name == student["name"]:
            delete_position = students.index(student)
            break

    if delete_position == -1:
        print("Student was not found.")
    else:
        del students[delete_position]
        print(f"Student '{name}' has been deleted successfully.")
    return

def update_student(name=None, 
                   new_phone=None,
                   new_gender=None,
                   new_details=None,
                   students=students):
    """
    Оновлює інформацію про існуючого студента.
    """
    if name==None:
        name = input("Please enter the name of the student to update: ")
    student_to_update = None

    # Знаходимо студента
    for student in students:
        if student["name"] == name:
            student_to_update = student
            break

    if not student_to_update:
        print("Student was not found.")
        return

    print(f"Current details of {name}:")
    print(f"Phone: {student_to_update['phone']}, Gender: {student_to_update['gender']}, Details: {student_to_update['details']}")

    # Запитуємо нові дані
    if new_phone==None or new_gender==None or new_details==None:
        new_phone = input("Enter new phone (leave blank to keep current): ") or student_to_update["phone"]
        new_gender = input("Enter new gender (Male/Female, leave blank to keep current): ") or student_to_update["gender"]
        new_details = input("Enter new details (leave blank to keep current): ") or student_to_update["details"]

    # Оновлюємо інформацію
    students.remove(student_to_update)
    updated_student = {"name": name, "phone": new_phone, "gender": new_gender, "details": new_details}

    # Вставляємо в потрібну позицію для збереження сортування
    insert_position = 0
    for student in students:
        if name > student["name"]:
            insert_position += 1
        else:
            break

    students.insert(insert_position, updated_student)
    print(f"Student '{name}' has been updated successfully.")
    return

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        load_data_from_csv(filename)
    else:
        print("No filename provided. Starting with an empty directory.")

    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ").strip()
        match choice:
            case "C" | "c":
                print("New student will be created:")
                add_new_student()
                print_all_students()
            case "U" | "u":
                print("Existing student will be updated:")
                update_student()
                print_all_students()
            case "D" | "d":
                print("Student will be deleted:")
                delete_student()
                print_all_students()
            case "P" | "p":
                print("List of students:")
                print_all_students()
            case "X" | "x":
                if len(sys.argv) > 1:
                    save_data_to_csv(sys.argv[1])
                print("Exiting the program...")
                break
            case _:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
