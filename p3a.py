# Encapsulation: Hiding data using methods (getter and setter)
class Person:
    def __init__(self, name, age):
        self.__name = name  # Private variable
        self.__age = age    # Private variable

    # Setter methods to set values
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    # Getter methods to get values
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


# Inheritance: A child class 'Student' that inherits from 'Person'
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)  # Inheriting from Person
        self.grade = grade

    def display(self):
        print(f"Name: {self.get_name()}, Age: {self.get_age()}, Grade: {self.grade}")


# Overloading: Function with default parameters
class Calculator:
    def add(self, a, b=0):  # Default b = 0, so it's optional
        return a + b


def main():
    # Encapsulation: Creating a person and changing details
    person = Person("John", 25)
    print(f"Person Info: Name = {person.get_name()}, Age = {person.get_age()}")

    person.set_name("Mike")  # Change name
    person.set_age(30)       # Change age
    print(f"Updated Person Info: Name = {person.get_name()}, Age = {person.get_age()}")

    # Inheritance: Creating a student and displaying their info
    student = Student("Alice", 20, "A")
    student.display()

    # Overloading: Adding numbers
    calculator = Calculator()
    print("Addition of 5 and 3:", calculator.add(5, 3))  # 2 arguments
    print("Addition of 5 (with default b=0):", calculator.add(5))  # 1 argument


if __name__ == "__main__":
    main()
