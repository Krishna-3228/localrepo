# object oriented programming
# objects(instances) - virtual entity that has some attributes and some functions
# class - blueprint for creating objects

class Employee:  # class 
    name="harry"      # class attribute
    language="python" # class attribute
    salary = 1200000  # class attribute

emp1=Employee()     # object1 as 'emp1'
print(emp1.name)        # harry
print(emp1.language)    # python
print(emp1.salary)      # 1200000
emp1.age=25         # object attribute
print(emp1.age)         # 25 

emp2=Employee()     # object2 as 'emp2'
print(emp2.name)        # harry
print(emp2.language)    # python
print(emp2.salary)      # 1200000
emp2.age=27         # object attribute
print(emp2.age)         # 27

# Instance attributes takes preference over class attributes during assignment and retrieval
emp2.name="karan"       
print(emp2.name)        # karan