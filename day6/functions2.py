# Functions

# def my_function():
#     print("Hello")

# my_function()

# def fahrenheit_to_celsius(fahrenheit):
#     return (fahrenheit-32) * 5/9

# print (fahrenheit_to_celsius(77))
# print (fahrenheit_to_celsius(105))
# print (fahrenheit_to_celsius(95))


# def my_function(name):
#     print("Hello",name)

# my_function("Yousuf")

# def travel(country = "India"):        # Give default value for functions when argument isn't available
#     print ("I am from",country)

# travel("America")
# travel("Norway")
# travel()

# def breed(animal,name,age):
#     print("I have a",animal, "and its name is "+name,"and it's",age,"years old")

# breed("dog",name = "boxer",age = 4)

# def fruits(fruit):
#     for x in fruit:
#         print(x)

# my_fruits = ["Apple","Banana","Cherry"]
# fruits(my_fruits)

# def persons(person):
#     print("Name:",person["name"])
#     print("Age:",person["age"])

# my_persons = {"name":"Yousuf","age":21}
# persons(my_persons)

# def my_function():
#     return (10,20)

# x,y = my_function()
# print("x:",x,"y:",y)

# def my_function(name,/):            # Positional Arguments only when specify ,/
#     print("Hello",name)

# my_function("Yousuf")

# def my_function(*,name):              # Keyword Arguments only when specify *,
#     print("Hello",name)

# my_function(name = "Yousuf")

# def my_function(a, b, /, *, c, d):               # Both Positional and Keyword Arguments
#   return a + b + c + d                           # Arguments before / are positional arguments and Arguments after * are Keyword arguments

# result = my_function(5, 10, c = 15, d = 20)
# print(result)

# *args and kwargs

# *args - Arbitrary Arguments accepts any number of positional arguments and inside the function
# it becomes tuple containing all passed arguments

# def names(*args):
#     print("Type:",type(args))
#     print("First value:",args[0])
#     print("Second value:",args[1])
#     print("All value:",args)

# names("Yousuf","Aasik","Joker")

# def names(greeting,*args):
#     for name in args:
#         print(greeting,name)

# names("Hello","Yousuf","Aasik","Joker")

# def sum1(*number):
#     total = 0
#     for num in number:
#         total += num
#     return total

# print(sum1(1,2,3))
# print(sum1(1,2,3,4,5))
# print(sum1(10,13,45))

# def max1(*number):
#     if len(number) == 0:
#         return None
#     max_num = number[0]
#     for num in number:
#         if num > max_num:
#             max_num = num
#     return max_num

# print(max1(1,25,3))

# **kwargs - Arbitrary Keyword Arguments allows any number of keyword arguments 
# and becomes dictionary containig all keyword arguments

# def my_function(**kwargs):
#     print("Type:",type(kwargs))
#     print("First value:",kwargs["name"])
#     print("Second value:",kwargs["age"])
#     print("All values:",kwargs)

# my_function(name = "Yousuf",age = 21, city = "Chennai")

# def my_function(username,**details):
#     print("Username:",username)
#     print("Additional Details:")
#     for key,value in details.items():
#         print(key+":",value)

# my_function("Yousuf",age = 21,city = "Chennai")

# Both *args and **kwargs

# def my_function(title,*args,**kwargs):
#     print("Title:",title)
#     print("Positional arguments:",args)
#     print("Keyword arguments:",kwargs)

# my_function("Python","Yousuf","Aasik",age = 21,city = "Chennai")

# def my_function(a, b, c):
#   return a + b + c

# numbers = [1, 2, 3]
# result = my_function(*numbers) # Same as: my_function(1, 2, 3)
# print(result)

# Scope

# def my_func():
#     x = 300            # Local Scope
#     print(x)

# my_func()


# x = 300            # Global Scope
# def my_func():
#     print(x)

# my_func()
# print(x)

# Function inside another function
# def my_func():
#     x = 200
#     def inner_func():
#         print(x)
#     inner_func()

# my_func()

# def my_func():
#     global x           # Global Variable
#     x = 200

# my_func()
# print(x)

# x=250
# def my_func():
#     global x           # Global Variable
#     x = 200

# my_func()
# print(x)

# x = "Global"

# def my_outer():
#     x = "Outer"
#     def my_inner():
#         x = "Local"
#         print("Local:",x)
#     my_inner()
#     print("Outer:",x)
# my_outer()
# print("Global:",x)

# Decorator
# def changecase(func):
#     def innerfunc():
#         return func().upper()
#     return innerfunc

# @changecase
# def myfunction():
#     return "Hello Yousuf"

# @changecase
# def otherfunction():
#     return "Hello Aasik"

# print(myfunction())
# print(otherfunction())

# def changecase(func):                       # Parameterized Decorator
#     def innerfunc(x):
#         return func(x).upper()
#     return innerfunc

# @changecase
# def myfunction(name):
#     return "Hello "+name

# print(myfunction("Aasik"))

# def changecase(func):
#     def innerfunc(*args,**kwargs):
#         return func(*args,**kwargs).upper()
#     return innerfunc

# @changecase
# def myfunction(name):
#     return "Hello "+name

# print(myfunction("John"))

# # Arguments in Decorators
# def changecase(n):
#     def changecase(func):      
#         def innerfunc():
#             if n == 1:
#                 a = func().upper()
#             else:
#                 a = func().lower()
#             return a
#         return innerfunc
#     return changecase

# @changecase(2)
# def myfunction():
#     return "Hello Yousuf"

# print(myfunction())

# Multiple Decorators
# def changecase(func):
#     def innerfunc():
#         return func().upper()
#     return innerfunc

# def addgreeting(func):
#     def innerfunc():
#         return "Hello "+ func() + " Have a Good Day"
#     return innerfunc

# @addgreeting
# @changecase
# def myfunction():
#     return "Yousuf"

# print(myfunction())
# print(myfunction.__name__)

# def myfunc():
#     return "Have a good day"

# print(myfunc.__name__)             # use __name__ metadata to print the function name But if we use this in Decorator function it will not give proper function name

# Lambda Functions

# x = lambda a: a+10
# print(x(5))

# x = lambda a,b : a*b
# print(x(4,5))

# def myfunc(n):
#     return lambda a : a*n

# doubles = myfunc(2)
# triples = myfunc(3)

# print(doubles(11))
# print(triples(3))

# Lambda Built-in Functions - map(), filter(), sorted()

# map() Function
# numbers = [1,2,3,4,5]
# double = list(map(lambda x:x*2,numbers))
# print(double)

# # filter() Function
# numbers2 = [1,2,3,4,5]
# odd = list(filter(lambda x: x%2!=0,numbers))
# print(odd)

# sort() Function
# numbers3 = [34,2,8,4,1]
# asc = sorted(numbers3,key = lambda x:x)
# print(asc)

# fruits = ["Kiwi","Dragon Fruit","Apple","Banana"]
# length = sorted(fruits,key = lambda x: len(x))
# print(length)

# names = [("Yousuf",21),("Thameem",24),("John",23)]
# names_sort = sorted(names,key = lambda x: x[1])
# print(names_sort)