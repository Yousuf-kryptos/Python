# Inheritance - It is used to define the class that inherits methods and properties from another class
# Parent class - Base Class  Child class - Derived Class

# class Parent:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def printinfo(self):
#         print(f"{self.name} {self.age}")

# class Child(Parent):
#     pass

# p1 = Child("Yousuf",21)
# p1.printinfo()

# Single Inheritance

# class Parent:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def printinfo(self):
#         print(f"{self.name} {self.age}")

# class Child(Parent):
#     def __init__(self,name,age,year):                 # When we declare seperate __init() for Child class, it will overrides parent's __init__()
#         # Parent.__init__(self,name,age)           # So, we made a call to the Parent's __init__(), to keep the inheritance of parent's
#         super().__init__(name,age)          # Instead of using Parent class name , we can use super() method
#         self.year = year
    
#     def welcome(self):
#         print(f"Welcome {self.name} to the year of {self.year}" )

# p1 = Child("Yousuf",21,2026)
# p1.printinfo()
# print(p1.year)
# p1.welcome()

# Multiple Inheritance

# class Father:
#     def skill1(self):
#         print("Driving")

# class Mother:
#     def skill2(self):
#         print("Cooking")

# class Child(Father,Mother):
#     def show(self):
#         print("Inherits both skills")

# c1 = Child()
# c1.skill1()
# c1.skill2()
# c1.show()

# MultiLevel Inheritance

# class Grandfather:
#     def __init__(self,grandfathername):
#         self.grandfathername = grandfathername

# class Father(Grandfather):
#     def __init__(self, grandfathername, fathername):
#         super().__init__(grandfathername)
#         self.fathername = fathername

# class Child(Father):
#     def __init__(self,grandfathername,fathername,childname):
#         super().__init__(grandfathername,fathername)
#         self.childname = childname

#     def printname(self):
#         print("Grandfather Name: ",self.grandfathername)
#         print("Father Name: ",self.fathername)
#         print("Child Name: ",self.childname)

# c1 = Child("one","two","three")
# c1.printname()

# Hierarchical Inheritance

# class Parent():
#     def func1(self):
#         print("Parent class")

# class Child1(Parent):
#     def func2(self):
#         print("Child1 class")

# class Child2(Parent):
#     def func3(self):
#         print("child2 class")

# obj1 = Child1()
# obj2 = Child2()

# obj1.func1()
# obj1.func2()
# obj2.func1()
# obj2.func3()

# Hybrid Inheritance

# class Grandfather:
#     def func1(self):
#         print("Grandfather class")

# class Parent1(Grandfather):
#     def func2(self):
#         print("Parent1 class")

# class Parent2(Grandfather):
#     def func3(self):
#         print("Parent2 class")

# class Child(Parent1,Parent2):
#     def func4(self):
#         print("Child class")

# c1 = Child()
# c1.func4()
# c1.func3()
# c1.func2()
# c1.func1()

