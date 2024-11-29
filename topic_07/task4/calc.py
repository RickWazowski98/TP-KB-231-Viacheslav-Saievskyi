
import logging
from calculator import Calculator

# Налаштування логування
logging.basicConfig(
    filename="calculator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_number(prompt):
    """
    Запитує введення числа від користувача.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            logging.warning("Користувач ввів некоректне число.")
            print("Будь ласка, введіть число.")

def main():
    logging.info("Калькулятор запущено.")
    calculator = Calculator()
    print("Вітаємо у програмі Калькулятор!")
    print("Введіть 'exit', щоб завершити програму.\n")

    while True:
        # Виведення доступних операцій
        print("Доступні операції:")
        for key, (name, _) in calculator.get_operations().items():
            print(f"{key}: {name}")

        # Вибір операції
        operation_key = input("\nВиберіть операцію (1/2/3/4): ").strip()
        if operation_key.lower() == 'exit':
            print("До побачення!")
            logging.info("Програма завершена користувачем.")
            break

        try:
            # Введення чисел
            num1 = get_number("Введіть перше число: ")
            num2 = get_number("Введіть друге число: ")

            # Виконання операції
            operation_name, result = calculator.perform_operation(operation_key, num1, num2)
            print(f"\nРезультат {operation_name.lower()}: {result}\n")

            # Логування успішної операції
            logging.info(f"Операція: {operation_name}. Вхідні дані: {num1}, {num2}. Результат: {result}.")

        except ValueError as e:
            logging.error(f"Помилка: {e}")
            print(f"Помилка: {e}")
        except Exception as e:
            logging.critical(f"Невідома помилка: {e}")
            print(f"Невідома помилка: {e}")

        print("-" * 30)

if __name__ == "__main__":
    main()
