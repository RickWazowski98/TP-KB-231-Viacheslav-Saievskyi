import math

def discriminant(a, b, c):
    return b**2 - 4*a*c

def find_roots(a, b, c):
    """
    Функція для знаходження коренів квадратного рівняння ax^2 + bx + c = 0.
    
    Параметри:
    a, b, c (float): коефіцієнти рівняння.
    
    Повертає:
    tuple: корені рівняння (може бути 2, 1 або ж порожній кортеж).
    """
    if a == 0:
        if b == 0:
            return "Рівняння не має змісту." if c != 0 else "Рівняння має безліч коренів."
        return (-c / b,)  # Лінійне рівняння
    
    discr = discriminant(a, b, c)
    
    if discr > 0:
        root1 = (-b + math.sqrt(discr)) / (2 * a)
        root2 = (-b - math.sqrt(discr)) / (2 * a)
        return root1, root2
    elif discr == 0:
        root = -b / (2 * a)
        return (root,)
    else:
        return "коренів немає (дискримінант менший за 0)."

# Приклад використання:
a, b, c = 1, -3, 2  # Коефіцієнти рівняння x^2 - 3x + 2 = 0
roots = find_roots(a, b, c)
print("Корені рівняння:", roots)