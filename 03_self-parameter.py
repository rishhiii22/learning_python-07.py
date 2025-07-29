class Employee:
    name = "Rishi"
    language = "Python" # This is a class Attribute
    salary = 12000000

    def getInfo(self): # Self is given because without writing self error aajayega.
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():  # Sometimes we need a function that does not use the self-parameter. We can define a static method like this:
        print("Good Morning")
  
Rishi = Employee()

Rishi.language = "JavaScript" # This is  an Instance Attribute

print(Rishi.salary,Rishi.language)

Rishi.getInfo()
Rishi.greet()

