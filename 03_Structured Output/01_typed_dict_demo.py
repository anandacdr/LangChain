from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    email: str

new_person: Person = {'name': 'Pikachu', 'age': 10, 'email': 'pikachu@gmail.com'}

print(new_person)