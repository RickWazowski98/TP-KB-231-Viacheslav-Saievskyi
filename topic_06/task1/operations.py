# operations.py

def get_number(prompt):
    """Функція для отримання числа від користувача з обробкою винятків."""
    while True:
        try:
            value = input(prompt)
            if value.lower() == 'exit':
                print("Робота завершена. Дякуємо за використання!")
                exit()
            return float(value)
        except ValueError:
            print("Помилка: введіть дійсне число.")

def get_operation():
    """Функція для отримання операції від користувача."""
    while True:
        print("\nОберіть операцію:")
        print("1. Додавання")
        print("2. Віднімання")
        print("3. Множення")
        print("4. Ділення")
        choice = input("Введіть номер операції (1/2/3/4) або 'exit' для виходу: ")
        if choice.lower() == 'exit':
            print("Робота завершена. Дякуємо за використання!")
            exit()
        if choice in ('1', '2', '3', '4'):
            return choice
        else:
            print("Помилка: оберіть коректну операцію.")
