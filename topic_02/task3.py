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
        return "Помилка: ділення на нуль."

def calculator():
    print("Вітаємо у калькуляторі!")
    print("Оберіть операцію:")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")

    choice = input("Введіть номер операції (1/2/3/4): ")
    try:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
    except ValueError:
        print("Помилка: введіть дійсні числа.")
        return

    match choice:
        case '1':
            print(f"Результат: {num1} + {num2} = {add(num1, num2)}")
        case '2':
            print(f"Результат: {num1} - {num2} = {subtract(num1, num2)}")
        case '3':
            print(f"Результат: {num1} * {num2} = {multiply(num1, num2)}")
        case '4':
            print(f"Результат: {num1} / {num2} = {divide(num1, num2)}")
        case _:
            print("Помилка: обрана некоректна операція.")

# Запуск калькулятора
calculator()
