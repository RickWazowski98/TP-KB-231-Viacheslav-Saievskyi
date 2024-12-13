
def precedence(op):
    """Визначення пріоритету оператора"""
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0

def is_number(token):
    """Перевірка, чи є токен числом (цілим або з плаваючою крапкою)"""
    try:
        float(token)
        return True
    except ValueError:
        return False

def infix_to_rpn(expression):
    """Перетворення інфіксного виразу в ЗПЗ"""
    stack = []
    output = []
    tokens = expression.split()

    for token in tokens:
        if is_number(token):  # Якщо операнд
            output.append(token)
        elif token == '(':  # Відкрита дужка
            stack.append(token)
        elif token == ')':  # Закрита дужка
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Видаляємо відкриту дужку
        else:  # Оператор
            while stack and precedence(stack[-1]) >= precedence(token):
                output.append(stack.pop())
            stack.append(token)

    while stack:  # Додаємо решту операторів
        output.append(stack.pop())

    return output

def evaluate_rpn(rpn):
    """Обчислення результату виразу в ЗПЗ"""
    stack = []

    for token in rpn:
        if is_number(token):  # Якщо операнд
            stack.append(float(token))
        else:  # Якщо оператор
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
            elif token == '^':
                stack.append(a ** b)

    return stack[0]

def main():
    print("Введіть математичний вираз (операнди та оператори розділяйте пробілом):")
    expression = input("Наприклад: 3 + 5 * ( 2 - 8 ): ")

    # Перетворення в ЗПЗ
    rpn = infix_to_rpn(expression)
    print("Зворотний польський запис:", ' '.join(rpn))

    # Обчислення результату
    result = evaluate_rpn(rpn)
    print("Результат обчислення:", result)

if __name__ == "__main__":
    main()
