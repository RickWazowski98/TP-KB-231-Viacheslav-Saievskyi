def test_dict_functions():
    # Початковий словник
    test_dict = {"a": 1, "b": 2, "c": 3}
    print("Початковий словник:", test_dict)

    # Тест update()
    test_dict.update({"d": 4, "e": 5})
    print("Після update({'d': 4, 'e': 5}):", test_dict)

    # Тест del()
    try:
        del test_dict["b"]  # Видалення ключа 'b'
        print("Після del test_dict['b']:", test_dict)
    except KeyError:
        print("Ключ 'b' не знайдено у словнику.")

    # Тест clear()
    temp_dict = test_dict.copy()  # Копія для відновлення після clear()
    test_dict.clear()
    print("Після clear():", test_dict)

    # Відновлення словника
    test_dict = temp_dict

    # Тест keys()
    print("Ключі словника після keys():", list(test_dict.keys()))

    # Тест values()
    print("Значення словника після values():", list(test_dict.values()))

    # Тест items()
    print("Пари ключ-значення після items():", list(test_dict.items()))

# Виклик функції тестування
test_dict_functions()
