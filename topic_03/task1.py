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
    print("Введіть 'exit' у будь-який момент, щоб завершити роботу.")

    while True:
        print("\nОберіть операцію:")
        print("1. Додавання")
        print("2. Віднімання")
        print("3. Множення")
        print("4. Ділення")
        choice = input("Введіть номер операції (1/2/3/4) або 'exit' для виходу: ")

        if choice.lower() == 'exit':
            print("Робота завершена. Дякуємо за використання!")
            break

        if choice not in ('1', '2', '3', '4'):
            print("Помилка: оберіть коректну операцію.")
            continue

        try:
            num1_input = input("Введіть перше число (або 'exit' для виходу): ")
            if num1_input.lower() == 'exit':
                print("Робота завершена. Дякуємо за використання!")
                break
            num1 = float(num1_input)

            num2_input = input("Введіть друге число (або 'exit' для виходу): ")
            if num2_input.lower() == 'exit':
                print("Робота завершена. Дякуємо за використання!")
                break
            num2 = float(num2_input)
        except ValueError:
            print("Помилка: введіть дійсні числа.")
            continue

        match choice:
            case '1':
                print(f"Результат: {num1} + {num2} = {add(num1, num2)}")
            case '2':
                print(f"Результат: {num1} - {num2} = {subtract(num1, num2)}")
            case '3':
                print(f"Результат: {num1} * {num2} = {multiply(num1, num2)}")
            case '4':
                print(f"Результат: {num1} / {num2} = {divide(num1, num2)}")

# Запуск калькулятора
calculator()
