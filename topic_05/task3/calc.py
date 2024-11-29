
import functions
import operations

def calculator():
    print("Вітаємо у калькуляторі!")
    print("Введіть 'exit' у будь-який момент, щоб завершити роботу.")

    while True:
        operation = operations.get_operation()
        num1 = operations.get_number("Введіть перше число: ")
        num2 = operations.get_number("Введіть друге число: ")

        try:
            if operation == '1':
                print(f"Результат: {num1} + {num2} = {functions.add(num1, num2)}")
            elif operation == '2':
                print(f"Результат: {num1} - {num2} = {functions.subtract(num1, num2)}")
            elif operation == '3':
                print(f"Результат: {num1} * {num2} = {functions.multiply(num1, num2)}")
            elif operation == '4':
                print(f"Результат: {num1} / {num2} = {functions.divide(num1, num2)}")
        except ZeroDivisionError as e:
            print(e)
        print("-" * 30)

# Запуск калькулятора
if __name__ == "__main__":
    calculator()
