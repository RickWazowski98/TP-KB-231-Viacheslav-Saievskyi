import requests

def get_exchange_rates():
    """
    Отримує актуальні курси валют від API НБУ.
    :return: Словник з курсами валют.
    """
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Фільтруємо необхідні валюти
        rates = {entry['cc']: entry['rate'] for entry in data if entry['cc'] in ['USD', 'EUR', 'PLN']}
        return rates
    except requests.RequestException as e:
        print("Помилка отримання даних від НБУ:", e)
        return None

def convert_currency(amount, currency, rates):
    """
    Конвертує валюту у гривні.
    :param amount: Сума валюти.
    :param currency: Тип валюти (USD, EUR, PLN).
    :param rates: Словник з курсами валют.
    :return: Сума в гривнях.
    """
    if currency not in rates:
        raise ValueError("Невідома валюта.")
    return amount * rates[currency]

def main():
    print("Конвертація валют у гривню (за даними НБУ).")
    print("Підтримувані валюти: USD, EUR, PLN.")
    
    rates = get_exchange_rates()
    if not rates:
        print("Неможливо отримати актуальні курси валют.")
        return

    while True:
        currency = input("Введіть код валюти (USD, EUR, PLN) або 'exit' для виходу: ").upper()
        if currency == 'EXIT':
            print("Дякуємо за використання програми!")
            break
        
        if currency not in rates:
            print("Некоректна валюта. Спробуйте ще раз.")
            continue

        try:
            amount = float(input(f"Введіть кількість {currency}: "))
            if amount < 0:
                print("Сума не може бути від'ємною.")
                continue

            result = convert_currency(amount, currency, rates)
            print(f"{amount} {currency} = {result:.2f} грн")
        except ValueError:
            print("Некоректне введення. Спробуйте ще раз.")

# Запуск програми
if __name__ == "__main__":
    main()
