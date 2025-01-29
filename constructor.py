# "self" refers to the instance of the class. It is automatically passed with a function call
# from an object.
# Any other identifier can be used in place of "self". However, self is used for readability
class Employee:  # class 
    name="harry"      # class attribute
    language="python" # class attribute
    salary = 1200000  # class attribute
    def getInfo(self):# class method >>"self" parameter is mandatory
        print(f"The language is {self.language}. The salary is {self.salary}")

    def greet(self):  # class method >>"self" parameter is mandatory
        print("Good Morning")

    @staticmethod   # decorator
    def welcome():  # No need to pass self parameter
        print("Welcome")

emp1=Employee()     # object
print(emp1.name)        # harry
print(emp1.language)    # python
print(emp1.salary)      # 1200000
emp1.age=25         # object attribute
print(emp1.age)         # 25 

emp1.language = "java"
print(emp1.language)        # java

# method call
emp1.getInfo()              # The language is java. The salary is 1200000
Employee.getInfo(emp1)      # The language is java. The salary is 1200000
## Above two lines are same 

emp1.greet()                # Good Morning
Employee.greet(emp1)        # Good Morning

emp1.welcome()              # Welcome

# this is modification
print("Hello git. Git is useful")