class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

# Створення об'єкта
person1 = Person("Alice", 30)

print(person1.name)
print(person1.age)
print(person1)


