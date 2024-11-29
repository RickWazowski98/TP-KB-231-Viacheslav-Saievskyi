def find_insert_position(sorted_list, value):
    """
    Знаходить позицію для вставки нового елемента у відсортований список.
    
    :param sorted_list: Відсортований список.
    :param value: Значення, яке потрібно вставити.
    :return: Індекс, на який потрібно вставити новий елемент.
    """
    left, right = 0, len(sorted_list)
    
    while left < right:
        mid = (left + right) // 2
        if sorted_list[mid] < value:
            left = mid + 1
        else:
            right = mid
    
    return left

mylist = [4,5,6,7324,5456,4356,2123,467,34,345,457,3,2134,7,653456,123,45567,46578,34245,574,4256,234,652345]
mysortedlist = sorted(mylist)
print(f"Відсортований список:{mysortedlist}")
position = find_insert_position(mysortedlist, 1)
print(f"Позиція для вставки елемента: {position}")
