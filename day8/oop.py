# OOP - Object Oriented Programming allows to structure the code using class and onjects for better readability and code efficiency
# DRY - Don't Repeat Yourself
# Class / Objects

# Class - Class is a blueprint for creating objects or like object constructor

# class MyClass:
#     x = 5

# p1 = MyClass()
# print(p1.x)

# del p1
# print(p1)

# p1 = MyClass()
# p2 = MyClass()
# p3 = MyClass()

# print(p1.x)
# print(p2.x)
# print(p3.x)

# __init__() Method and self

# __inti__() -is used to assign values to object properties, 
# or to perform operations that are necessary when the object is being created.

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# p1 = Person("Yousuf",21)
# print(p1.name)
# print(p1.age)


# Without __init__()
# class Person:
#     pass

# p1 = Person()
# p1.name = "Yousuf"
# p1.age = 21
# print(p1.name)
# print(p1.age)

# Default Parameters

# class Person:
#     def __init__(self,name="Yousuf",age=21):
#         self.name = name
#         self.age = age

# p1 = Person()
# print(p1.name)
# print(p1.age)

# Multiple Parameters

# class Person:
#     def __init__(self,name,age,city,state,country):
#         self.name = name
#         self.age = age
#         self.city = city
#         self.state = state
#         self.country = country

# p1 = Person("Yousuf",21,"Chennai","TamilNadu","India")
# print(p1.name)
# print(p1.age)
# print(p1.city)
# print(p1.state)
# print(p1.country)

# self Parameter

# self - is the reference to the current instance of the class
# It is used to access properties and methods that belong to the class
# self must be used as the first parameter in the methods

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def greet(self):
#     print("Hello, my name is " + self.name)

# p1 = Person("Emil", 25)
# p2 = Person("Yousuf",21)
# p1.greet()
# p2.greet()

# class Car:
#     def __init__(self,name,model):
#         self.name = name
#         self.model = model

#     def displayinfo(self):
#         print(f"{self.name} {self.model}")

# c1 = Car("Ford","Mustang")
# c1.displayinfo()

# Calling methods using self

# class Person:
#     def __init__(self,name):
#         self.name = name

#     def greet(self):
#         return "Hello, "+self.name

#     def welcome(self):
#         message = self.greet()
#         print(message +" Welcome to the website")

# p1 = Person("Yousuf")
# p1.welcome()

# Class Properties

# class Person:                               # Class with properties(name,age)
#     species = "Homo Sapiens"                # Class Property
#     def __init__(self,name,age):
#         self.name = name                    # Instance Property
#         self.age = age

# p1 = Person("Yousuf",21)
# print(p1.name)                              # Accessing Instance properties
# print(p1.age)

# p1.age = 22                                 # Modifying Instance Properties
# print(p1.age)

# del p1.age                                  # Deleting Instance Propertie
# # print(p1.age)                               # cause error because p1.age is deleted

# print(p1.species)                           # Printing Class Properties
# p1.species = "Humans"                       # Modifying Class Properties
# print(p1.species)

# Adding new properties

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# p1 = Person("Yousuf",21)
# p1.city = "Chennai"                    # Adding properties to the instance class
# p1.country = "India"
# print(p1.name)
# print(p1.age)
# print(p1.city)
# print(p1.country)

# Class Methods - All Methods mush have self as the first parameter

# class Calculator:
#     def add(self,a,b):
#         return a + b
#     def multiply(self,a,b):
#         return a * b
    
# c1 = Calculator()
# print(c1.add(4,5))
# print(c1.multiply(5,5))

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def getinfo(self):
#         self.age += 1                                     # Modifying Method properties
#         print(f"{self.name} is {self.age} years old")     # Accessing Method Properties

# p1 = Person("Yousuf",21)
# p1.getinfo()

# __str__() Method

# without __str__() Method
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("Emil", 36)
# print(p1)

# With __str__() Method

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   def __str__(self):
#     return f"{self.name} is {self.age} years old"

# p1 = Person("Emil", 36)
# print(p1)

# class Playlists:
#     def __init__(self,name):
#         self.name = name
#         self.songs = []
#     def add_songs(self,song):
#         self.songs.append(song)
#         print(f"Added Song:{song}")

#     def remove_songs(self,song):
#         if song in self.songs:
#             self.songs.remove(song)
#             print(f"Removed Song:{song}")

#     def show_songs(self):
#         print(f"Playlists:{self.name}")

#         for song in self.songs:
#             print(f"- {song}")
# p1 = Playlists("Favourites")
# # del p1.remove_songs()                            # Delete the Method
# p1.add_songs("Oru Naal")
# p1.add_songs("Ek Din")
# p1.show_songs()
# p1.remove_songs("Ek Din")
# p1.show_songs()

