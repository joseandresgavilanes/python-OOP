from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    @abstractmethod
    def say_hello(self):
        """This method should be implemented by subclass"""

    @abstractmethod
    def say_goodbye(self):
        """This method should be implemented by subclass"""

    def __str__(self) -> str:
        return f"{self.name} {self.age}"


class Student(Person):
    def __init__(self, name, age, school) -> None:
        super().__init__(name, age)
        self.school = school
        self.__is_enabled = True

    def say_hello(self):
        return f"Hello my name is {self.name}"

    def say_goodbye(self):
        return f"Goodbye, {self.name}!"

    def enable(self):
        self.__is_enabled = True

    def disable(self):
        self.__is_enabled = False

    def get__status(self):
        return self.__is_enabled

    def __str__(self) -> str:
        return super().__str__() + f" I'm a student from {self.school} {self.__is_enabled}"


student = Student("Jose", 18, "Ambato high school")
print(student)
