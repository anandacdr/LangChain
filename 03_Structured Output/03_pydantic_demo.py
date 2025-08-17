from pydantic import BaseModel, Field
from typing import Optional
from pydantic import EmailStr

class Student(BaseModel):
    name: str
    age: Optional[int] = None
    email: EmailStr
    GPA: float = Field(gt = 0, lt = 10, default = 3.8, description = "The GPA of the student")

new_student = {'name': "Ananda", 'age': 20, 'email': 'ananda@anovoxlabs.com'}

student = Student(**new_student)

print(student)
print(type(student))

print(student.name)

