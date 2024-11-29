def test_list_functions():
    # Початковий список
    test_list = [5, 3, 8, 1, 7]
    print("Початковий список:", test_list)

    # Тест extend()
    test_list.extend([2, 6])
    print("Після extend([2, 6]):", test_list)

    # Тест append()
    test_list.append(4)
    print("Після append(4):", test_list)

    # Тест insert()
    test_list.insert(2, 9)  # Вставка 9 на позицію 2
    print("Після insert(2, 9):", test_list)

    # Тест remove()
    try:
        test_list.remove(8)  # Видалення значення 8
        print("Після remove(8):", test_list)
    except ValueError:
        print("Значення 8 не знайдено у списку.")

    # Тест clear()
    temp_list = test_list.copy()  # Копія для відновлення після clear()
    test_list.clear()
    print("Після clear():", test_list)

    # Відновлення списку
    test_list = temp_list

    # Тест sort()
    test_list.sort()
    print("Після sort():", test_list)

    # Тест reverse()
    test_list.reverse()
    print("Після reverse():", test_list)

    # Тест copy()
    copied_list = test_list.copy()
    print("Копія списку після copy():", copied_list)

# Виклик функції тестування
test_list_functions()
