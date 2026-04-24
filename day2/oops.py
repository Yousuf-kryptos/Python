# # OOP Concepts
# # Class and Objects
# class Human:                     # Class Defining
#     species = "Homo Sapiens"     # Class Attributes/class variable

#     def __init__(self,name,age): # __init__ acts as an constructor and will automatically run when an object is created
#         self.name = name         # Instance variable
#         self.age = age

#     def __str__(self):
#         return f"{self.name} is {self.age} years old"

# human1 = Human("Yousuf",21)      # creating the object from class
# print(human1.name)               # Accessing the class elements
# print(human1.age)
# print(human1)

# # Four Pillars of OOP
# # 1. Inheritance
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def info(self):
#         print("Animal name:", self.name)

# class Dog(Animal):
#     def sound(self):
#         print(self.name, "barks")

# d = Dog("Buddy")
# # Inherited method
# d.info()     
# d.sound()

# # super() method
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def info(self):
#         print("Animal name:", self.name)

# class Dog(Animal):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.breed = breed

#     def details(self):
#         print(self.name, "is a ", self.breed)

# d = Dog("Buddy","ROTWEILER")
# # Inherited method
# d.info()     
# d.details()

# # Single Inheritance
# class Parent():
#     def func1(self):
#         print("Parent class")

# class Child(Parent):
#     def func2(self):
#         print("Child class")

# obj = Child()
# obj.func1()
# obj.func2()

# # Multiple Inheritance
# class Father():
#     fathername = ""

#     def father(self):
#         print(self.fathername)

# class Mother():
#     mothername = ""

#     def mother(self):
#         print(self.mothername)

# class Child(Father,Mother):
#     def Parents(self):
#         print(self.fathername)
#         print(self.mothername)

# obj = Child("one","two")
# obj.fathername = "one"
# obj.mothername = "two"
# obj.Parents()

# # Multilevel Inheritance
# class grandfather():
#     def __init__(self,grandfathername):
#         self.grandfathername = grandfathername

# class father(grandfather):
#     def __init__(self,fathername,grandfathername):
#         self.fathername = fathername
#         grandfather.__init__(self,grandfathername)

# class son(father):
#     def __init__(self,sonname,fathername,grandfathername):
#         self.sonname = sonname
#         father.__init__(self,fathername,grandfathername)

#     def printname(self):
#         print("Grandfather name: ",self.grandfathername)
#         print("Father name: ",self.fathername)
#         print("Son name: ",self.sonname)

# obj = son("One","Two","Three")
# obj.printname() 

# # Hierarchical Inheritance
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

# # Hybrid Inheritance
# class Parent():
#     def func1(self):
#         print("Parent class")

# class Child1(Parent):
#     def func2(self):
#         print("Child1 class")

# class Child2(Parent):
#     def func3(self):
#         print("Child2 class")

# class Child3(Child1,Child2):
#     def func4(self):
#         print("Child3 class")

# obj1 = Child1()
# obj2 = Child2()
# obj3 = Child3()

# obj1.func1()
# obj1.func2()
# obj2.func1()
# obj2.func3()
# obj3.func1()
# obj3.func2()
# obj3.func3()
# obj3.func4()

# # super method - no need to call the all functions seperately
# class Parent():
#     def m(self):
#         print("Parent class")

# class Child1(Parent):
#     def m(self):
#         print("Child1 class")
#         super().m()

# class Child2(Parent):
#     def m(self):
#         print("Child2 class")
#         super().m()

# class Child3(Child1,Child2):
#     def m(self):
#         print("Child3 class")
#         super().m()

# obj1 = Child3()
# obj1.m()

# #2. PolyMorphisms
# # Method Overloading - Complie time polymorphisms
# class Calculator:
#     def multiply(self,a=1,b=1,*args):
#         res = a*b
#         for nums in args:
#             res *= nums
#         return(res)

# cal = Calculator()

# print(cal.multiply())
# print(cal.multiply(4))
# print(cal.multiply(2,3))

# # Method Overriding - Runtime Polymorphisms
# class Animal:
#     def sound(self):
#         return "Some generic sound"

# class Dog(Animal):
#     def sound(self):
#         return "Bark"
    
# class Cat(Animal):
#     def sound(self):
#         return "Meow"
    
# animals = [Animal(),Dog(),Cat()]
# for animal in animals:
#     print(animal.sound())
    
# class Pen():
#     def use(self):
#         return "Writing"
    
# class Eraser():
#     def use(self):
#         return "Erasing"
    
# def perform_tool(tool):
#     print(tool.use())

# perform_tool(Pen())
# perform_tool(Eraser())

# # Encapsulation
# # Public and Private
# class Employee:
#     def __init__(self,name,salary):
#         self.name = name        #public attribute
#         self.__salary = salary  #private attribute

#     def display_name(self):     #public method
#         print(self.name)

#     def show_salary(self):      #Way to access the private attribute
#         print(self.__salary)

# e1 = Employee("Yousuf",15000)
# e1.display_name()
# print(e1.name)
# # print(e1.__salary)         #Show error wrong way to access the private attribute
# e1.show_salary()


# # Protected
# class Employee:
#     def __init__(self,name):
#         self._name = name        #protected attribute

# class SubEmployee(Employee):
#     def show_name(self):
#         print(self._name)        #Accessible in subclass

# e1 = SubEmployee("Yousuf")
# e1.show_name()

# # Private using getter and setter
# class Employee:
#     def __init__(self):
#         self.__salary = 15000      #Private Attribute

#     def get_salary(self):
#         return self.__salary
    
#     def set_salary(self,amount):
#         if amount>0:
#             self.__salary = amount
#         else:
#             print("Invalid Salary amount")

# emp = Employee()
# print(emp.get_salary())

# emp.set_salary(17000)
# print(emp.get_salary())

# # Abstraction
# from abc import ABC,abstractmethod

# class Greet(ABC):
#     @abstractmethod
#     def say_hello(self):
#         pass                   #Abstract Method

#     def move(self):
#         return "Moving"        #Concrete Method

# class Demo(Greet):
#     def say_hello(self):
#         return "Hello"
    
# demo = Demo()
# print(demo.say_hello())