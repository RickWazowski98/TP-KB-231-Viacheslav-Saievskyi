
from operations import add, subtract, multiply, divide

class Calculator:
    def __init__(self):
        self.operations = {
            '1': ('Додавання', add),
            '2': ('Віднімання', subtract),
            '3': ('Множення', multiply),
            '4': ('Ділення', divide),
        }

    def get_operations(self):
        """
        Повертає список доступних операцій.
        """
        return self.operations

    def perform_operation(self, operation_key, a, b):
        """
        Виконує операцію, вибрану користувачем.
        """
        if operation_key not in self.operations:
            raise ValueError("Невірний вибір операції.")
        
        operation_name, operation_func = self.operations[operation_key]
        return operation_name, operation_func(a, b)
