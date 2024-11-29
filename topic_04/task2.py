def add(a, b):
    """Додавання"""
    return a + b

def subtract(a, b):
    """Віднімання"""
    return a - b

def multiply(a, b):
    """Множення"""
    return a * b

def divide(a, b):
    """Ділення"""
    if b != 0:
        return a / b
    else:
        raise ZeroDivisionError("Ділення на нуль неможливе.")

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

def calculator():
    print("Вітаємо у калькуляторі!")
    print("Введіть 'exit' у будь-який момент, щоб завершити роботу.")

    while True:
        operation = get_operation()
        num1 = get_number("Введіть перше число: ")
        num2 = get_number("Введіть друге число: ")

        try:
            match operation:
                case '1':
                    print(f"Результат: {num1} + {num2} = {add(num1, num2)}")
                case '2':
                    print(f"Результат: {num1} - {num2} = {subtract(num1, num2)}")
                case '3':
                    print(f"Результат: {num1} * {num2} = {multiply(num1, num2)}")
                case '4':
                    print(f"Результат: {num1} / {num2} = {divide(num1, num2)}")
        except ZeroDivisionError as e:
            print(e)

# Запуск калькулятора
calculator()
