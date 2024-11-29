class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student(name={self.name}, age={self.age})"

# Створення списку студентів
students = [
    Student("Alice", 22),
    Student("Bob", 20),
    Student("Charlie", 21),
    Student("Diana", 23),
]

# Сортування списку за іменем
sorted_students_by_name = sorted(students, key=lambda student: student.name)

# Виведення відсортованого списку
print("Список, відсортований за іменем:")
for student in sorted_students_by_name:
    print(student)

# Сортування списку за віком
sorted_students_by_age = sorted(students, key=lambda student: student.age)

# Виведення відсортованого списку
print("\nСписок, відсортований за віком:")
for student in sorted_students_by_age:
    print(student)
