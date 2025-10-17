from datetime import date
class Person:
    #initialize the Person object with a name,country,and date of birth
    def __init__(self,name,country,date_of_birth):
        self.name=name
        self.country=country
        self.date_of_birth=date_of_birth
        #calculate the age of the person based on their date of birth
    def calculate_age(self):
        today=date.today()
        age=today.year-self.date_of_birth.year
        if today<date(today.year,self.date_of_birth.month,self.date_of_birth.day):
            age-=1
        return age
    #Example usage
        #Create three Person objects with different attributes

person1=Person("Udaya","ongole",date(2026,7,12))

    #Access and print the attributes and calculated age for each person
print("calculated age for each person")
print("*****************************************")
print("Person 1:")
print("Name:",person1.name)
print("Country:",person1.date_of_birth)
print("Age:",person1.calculate_age())
