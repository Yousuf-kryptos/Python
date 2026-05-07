# # Arguments - are the values that are passed into the functions as parameters
# # A function can have any number of arguments seperated by comma

# # Types of Arguments 
# # Default Argument, Keyword Argument, Positional Argument, Arbitrary argument and Lambda Function 

# # Default Argument

# def calculator(length,width = 5):  # whenever user forget give value for arguments , then default value will be used
#     area = length * width
#     print(f"Area: {area}")

# calculator(10,7)
# calculator(3)

# # Keyword Arguments - pass the values by parameters names while calling the function

# def person(name,age):
#     print("Name: ",name)
#     print("Age: ",age)

# person(name = "Yousuf",age = 21)
# person(age = 22,name = "Aasik")  # Even order is swapped still get the same result

# # Positional Arguments - values are passes in same order as parameters are defined in the function 
# and change in order leads to unexpected error or  changes the meaning of the result

# def multiply(a,b):
#     return a*b

# print(multiply(3,4))

# def sub(a,b):
#     return a-b

# a,b = 10,5

# print("correct result",sub(a,b))
# print("Changed result",sub(b,a))

# # Arbitrary Arguments(*args and **kwargs)

# # *args - It accepts any number of positional arguments/values to a function into a tuple

# def person(*args):
#     print(type(args))
#     print(args)
#     print(args[0])
#     print(args[2])
#     for arg in args:
#         print(arg)

# person("Yousuf","Aasik","Nobita")

# # **kwargs - it accepts any number of keyword arguments/values to a function into a dictionary

# def fun(**kwargs):
#     for key,value in kwargs.items():
#         print(key,'=',value)

# fun(a=1,b=2,c=4)

# # using both *args and **kwargs

# def display(*args,**kwargs):
#     print("Subjects: ",args)
#     print("Details: ",kwargs)

# display("English","Tamil","Maths",name = "Yousuf",age=21,city = "Chennai")

# # Lambda Function Arguments

# # Passing one argument
# square = lambda x : x**2
# print(square(4))

# # Passing two arguments

# add = lambda a,b : a+b
# print(add(3,5))

x = lambda x : "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(x(3))
print(x(0))
print(x(-3))