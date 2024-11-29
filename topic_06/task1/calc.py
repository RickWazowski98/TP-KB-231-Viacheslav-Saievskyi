import logging
import functions
import operations 

# Налаштування логування
logging.basicConfig(
    filename="calculator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def calculator():
    logging.info("Калькулятор запущено.")
    print("Вітаємо у калькуляторі!")
    print("Введіть 'exit' у будь-який момент, щоб завершити роботу.")

    while True:
        try:
            operation = operations.get_operation()
            logging.info(f"Обрано операцію: {operation}")

            num1 = operations.get_number("Введіть перше число: ")
            logging.info(f"Введено перше число: {num1}")

            num2 = operations.get_number("Введіть друге число: ")
            logging.info(f"Введено друге число: {num2}")

            if operation == '1':
                result = functions.add(num1, num2)
                logging.info(f"Виконано додавання: {num1} + {num2} = {result}")
                print(f"Результат: {num1} + {num2} = {result}")
            elif operation == '2':
                result = functions.subtract(num1, num2)
                logging.info(f"Виконано віднімання: {num1} - {num2} = {result}")
                print(f"Результат: {num1} - {num2} = {result}")
            elif operation == '3':
                result = functions.multiply(num1, num2)
                logging.info(f"Виконано множення: {num1} * {num2} = {result}")
                print(f"Результат: {num1} * {num2} = {result}")
            elif operation == '4':
                result = functions.divide(num1, num2)
                logging.info(f"Виконано ділення: {num1} / {num2} = {result}")
                print(f"Результат: {num1} / {num2} = {result}")

        except ZeroDivisionError:
            logging.error(f"Спроба ділення на нуль: {num1} / {num2}")
            print("Помилка: ділення на нуль неможливе.")
        except Exception as e:
            logging.error(f"Невідома помилка: {e}")
            print("Сталася помилка. Спробуйте ще раз.")

        print("-" * 30)

if __name__ == "__main__":
    calculator()