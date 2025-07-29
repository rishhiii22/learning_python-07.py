#  A Class is a blueprint for creating object.

class Employee:
    name = "Rishi"
    language = "Python" # This is a class Attribute
    salary = 12000000

Rishi = Employee()
Rishi.name = "Rishi" # This is Instance Attribute
print(Rishi.name ,Rishi.salary ,  Rishi.language)


Virat = Employee()
Virat.name = "Vk18 🔥" 
print(Virat.name , Virat.salary , Virat.language)

# Here name is Instance attribute and salary and language are class attributes as they directly belong to the class.
