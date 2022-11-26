from dataclasses import dataclass


class Person:

    def __init__(self, name: str, profession: str) -> None:

        self.name = name
        self.profession = profession
        self.skills = []

    def add_skill(self, skill):
        self.skills.append(skill)

    def __str__(self) -> str:
        return f'I am {self.name} and my profession is {self.profession}, skills: {self.skills}'


@dataclass
class Vehicle:
    brand: str
    year: int

    def __str__(self) -> str:
        return f"Car {self.brand} and year {self.year} "


vehicle = Vehicle("Toyota", 2022)
print(vehicle)

person = Person('Jose', 'Software Engineer')
person.add_skill('Python')
person.add_skill('POO')
print(person)
