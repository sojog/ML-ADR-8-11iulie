class Student:
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

    def __str__(self):
        return f"Studentul: {self.nume} are {self.varsta}" 