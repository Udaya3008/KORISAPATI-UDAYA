'''
Constructor is a special method used to create and initialize an object of a class.
destructor is used to destroy the object.
we'll create a Class Student with an instance variable student name
we'll see how to use a constructor to initialize the student name at the time of object
creation.
Using self,we can access the instance variable and instance method of the object.

'''
class Student:
  def __init__(self,name):
    self.name = name
  def show(self):
    print('Hello,my name is',self.name)
s1=Student('Udaya')
s1.show()
