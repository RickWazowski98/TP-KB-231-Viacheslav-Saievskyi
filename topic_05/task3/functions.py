
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
        raise ZeroDivisionError("Ділення на нуль неможливе.")
