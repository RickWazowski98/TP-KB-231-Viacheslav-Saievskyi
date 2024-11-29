# Невідсортований список словників
students = [
    {"name": "Anna", "grade": 85},
    {"name": "John", "grade": 92},
    {"name": "Maria", "grade": 78},
    {"name": "Mike", "grade": 88},
    {"name": "Zoe", "grade": 91}
]

# Сортуємо список за очінкою
sorted_students_by_grade = sorted(students, key=lambda student: student["grade"])

# Виведення результату
print("Список, відсортований за оцінкою:")
for student in sorted_students_by_grade:
    print(student)

print("-"*30)

# Сортуємо список за іменем
sorted_students_by_name = sorted(students, key=lambda student: student["name"])

# Виведення результату
print("Список, відсортований за іменем:")
for student in sorted_students_by_name:
    print(student)
