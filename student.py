class student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displaystudent(self):
        print("Name : ", self.name, ", Salary: ", self.age)
    def __del__(self):
        print('Destructor called, deleted.')

emp1 = student("Zara", "2000")
emp2 = student("Manni", "5000")
emp3 = student("anu","345")
emp1.displaystudent()
emp2.displaystudent()
emp3.displaystudent()
del emp1
del emp2



