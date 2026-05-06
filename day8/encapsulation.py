# Encapsulation - means Protecting the data includes properties and methods together inside a class
# and also controlling how the data can be accessed from outside the class

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age            # Private property - use (__ ) before variable to make it private

# p1 = Person("Yousuf",21)
# print(p1.name)
# print(p1.__age)                     # cause an error because __age is private property

# Access Private Property using get method and set property value using set method

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age
    
#     def get_age(self):
#         return self.__age
    
#     def set_age(self,age):
#         if(age > 0):
#             self.__age = age
#         else:
#             print("Age must ne positive")

# p1 = Person("Yousuf",21)
# print(p1.name)
# print(p1.get_age())

# p1.set_age(22)
# print(p1.get_age())\

# class Student:
#     def __init__(self,name,grade):
#         self.name = name
#         self.__grade = grade

#     def get_grade(self):
#         return self.__grade
    
#     def set_grade(self,grade):
#         if 0 < grade <100:
#             self.__grade = grade
#         else:
#             print("grade should be between 0 and 100")
#     def show_status(self):
#         if self.__grade > 60:
#             print("passed")
#         else:
#             print("Failed")

# s1 = Student("Yousuf",75)
# print(s1.get_grade())
# s1.set_grade(80)
# print(s1.get_grade())
# s1.show_status()

# Protected Properties

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self._age = age                    # Protected Property

# p1 = Person("Yousuf",21)
# print(p1.name)
# print(p1._age)

# Private Methods

# class Calculator:
#     def __init__(self):
#         self.result = 0

#     def __validate(self,num):
#         if not isinstance(num,(int,float)):
#             return False
#         return True
    
#     def add(self,num):
#         if self.__validate(num):
#             self.result += num
#         else:
#             print("Invalid Number")

# c1 =Calculator()
# c1.add(10)
# c1.add(5)
# print(c1.result)
# print(c1.__validate())                  # cause an error because private method is not accessed outside the class

