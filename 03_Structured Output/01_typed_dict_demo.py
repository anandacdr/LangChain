from typing import TypedDict

class Person(TypeDict):
    name: str
    age: int
    email: str

person = Person(name="Pikachu", age=30, email="pikachu@gmail.com")

print(person)

def get_person_info(person: Person) -> str:
    return f"Name: {person.name}, Age: {person.age}, Email: {person.email}"