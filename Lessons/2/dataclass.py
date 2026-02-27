from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    
student = Student("John", 20)
print(student)