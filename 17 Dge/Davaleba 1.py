class Student:
    def __init__(self, name, age, grades = None):
        self.name = name
        self.age = age
        self.grades = grades if grades is not None else []
    
    