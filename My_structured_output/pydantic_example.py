from typing import Optional

from pydantic import BaseModel, Field, field_validator


class Student(BaseModel):
    name: str = "nitesh"
    age: Optional[int] = None
    email: str
    cgpa: float = Field(
        default=5,
        gt=0,
        lt=10,
        description="CGPA must be between 0 and 10",
    )


new_student = {"name": "John Doe", "email": "john.doe@example.com", "cgpa": 8.5}

student = Student(**new_student)

print(student)