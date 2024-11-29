
students = [
    {"name": "Bob", "phone": "0631234567", "gender": "Male", "details": "Good at math"},
    {"name": "Emma", "phone": "0631234567", "gender": "Female", "details": "Prefers literature"},
    {"name": "Jon", "phone": "0631234567", "gender": "Male", "details": "Interested in sports"},
    {"name": "Zak", "phone": "0631234567", "gender": "Male", "details": "Enjoys painting"}
]

def print_all_students():
    for student in students:
        print(f"Name: {student['name']}, Phone: {student['phone']}, Gender: {student['gender']}, Details: {student['details']}")
    return

def add_new_student():
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

def delete_student():
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

def update_student():
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
                print("Exiting the program...")
                break
            case _:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
