class Employee:
    name = "Rishi"
    language = "Python" # This is a class Attribute
    salary = 12000000
    
    def __init__(self, name, salary, language):  # It is dunder method which is automatically called.
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an Object")

    def getInfo(self): # Self is given because without writing self error aajayega.
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():  # Sometimes we need a function that does not use the self-parameter. We can define a static method like this:
        print("Good Morning")
  
Rishi = Employee("Harry" , 1300 , "C++")
print(Rishi.name , Rishi.salary , Rishi.language)
#Rishi.name = "Rishi"
