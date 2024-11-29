import unittest
from unittest.mock import patch, mock_open
from lab_02.lab_02 import (
    add_new_student,
    update_student,
    delete_student,
    load_data_from_csv,
    save_data_to_csv,
)

# Оскільки програма зберігає та завантажує дані в окремих функціях, вони будуть тестуватися
# Напишемо функції для тестування основних операцій, наприклад:
# 1) Додавання нового студента
# 2) Оновлення студента
# 3) Видалення студента
# 4) Завантаження та збереження файлів CSV

# Тести
class TestStudentDirectory(unittest.TestCase):

    def test_load_data_from_csv(self):
        """Тестуємо завантаження даних з CSV"""
        students = []
        mock_csv_data = "name,phone,gender,details\nJohn,0631234567,Male,First year\n"
        with patch("builtins.open", mock_open(read_data=mock_csv_data)):
            load_data_from_csv("students_test.csv", students)
            self.assertEqual(len(students), 1)
            self.assertEqual(students[0]["name"], "John")
            self.assertEqual(students[0]["phone"], "0631234567")
            self.assertEqual(students[0]["gender"], "Male")
            self.assertEqual(students[0]["details"], "First year")

    def test_add_new_student(self):
        """Тестуємо додавання нового студента"""
        students = []
        add_new_student("Slava", "0631234567", "Male", "First year1", students)
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0]["name"], "Slava")
        self.assertEqual(students[0]["phone"], "0631234567")
        self.assertEqual(students[0]["gender"], "Male")
        self.assertEqual(students[0]["details"], "First year1")

    def test_update_student(self):
        """Тестуємо оновлення даних студента"""
        students = []
        add_new_student("John", "0631234567", "Male", "First year", students)
        update_student("John", "0637654321", "Male", "Second year", students)
        self.assertEqual(students[0]["phone"], "0637654321")
        self.assertEqual(students[0]["details"], "Second year")

    def test_delete_student(self):
        """Тестуємо видалення студента"""
        students = []
        add_new_student("John", "0631234567", "Male", "First year", students)
        delete_student("John", students)
        self.assertEqual(len(students), 0)

    def test_save_data_to_csv(self):
        """Тестуємо збереження даних у CSV"""
        students = []
        add_new_student("John", "0631234567", "Male", "First year", students)
        # Мокування open та csv.DictWriter
        mock_open_func = mock_open()
        # Патчим відкриття файлів
        with patch("builtins.open", mock_open_func):
            # Мокуємо метод writer, щоб додати потрібні атрибути
            mock_writer = patch('csv.DictWriter', return_value=mock_open_func).start()
            save_data_to_csv("students_test.csv", students)

if __name__ == "__main__":
    unittest.main()
