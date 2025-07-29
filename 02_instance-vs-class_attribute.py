class Employee:

    language = "Python" # This is a class Attribute
    salary = 12000000

Rishi = Employee()
Rishi.language = "JavaScript" # This is Instance Attribute
print(Rishi.salary ,  Rishi.language)