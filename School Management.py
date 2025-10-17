# Example
2: School Managemant

#Parent
class Person:

    def __init__(self,name,age):
        self.Name=name
        self.Age=age

class Student(Person):
    
    def __init__(self,name,age,rollno=278):
        super().__init__(name,age)
        self.roll_no= rollno

    def introduce(self):
        print(f"My name is {self.Name},age{self.Age},roll number{self.roll_no}.")

obj=Student("Udaya",21)
obj.introduce()
