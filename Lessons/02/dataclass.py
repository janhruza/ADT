from dataclasses import dataclass

# dataclass automaticky vytvori metody __init__, __repr__, __eq__
# stejne jako vytvori vsechny atributy
@dataclass
class Student:
    name: str
    age: int
    
# vytvori instance objektu
student = Student("Honza", 24)
student2 = Student("Jana", 22)

# vypise objekty
print(student)
print(student2)