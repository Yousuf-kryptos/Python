# Exception Handling
# try - try block lets you test the block of code for an error
# except - except block lets you handle the error occurs
# else - else block lets you execute the block of code when there is no error
# finally - finally block lets you execute the block regardless of an error or not

# Try and Except Block

# try:
#     print(x)
# except:
#     print("An Exception occured")

# Multiple Except Block

# try:
#     print(x)
# except NameError:
#     print("variable x is not defined")
# except:
#     print("Something else went wrong")

# Else Block

# try:
#     print("hello")
# except:
#     print("Something else went wrong")
# else:
#     print("Nothing went wrong")

# Finally Block

# try:
#     print("hello")
# except:
#     print("Something else went wrong")
# else:
#     print("Nothing went wrong")
# finally:
#     print("try..except completed successfully")

# Raise an Exception

# x = -1

# if x < 0:
#     raise Exception("Less than 0 is not allowed")

# x = "hello"

# if type(x) is not int:
#     raise Exception("String is not allowed")

# Arithmetic Error - ZeroDivision Error, Overflow Error

# ZeroDivision Error
# try:
#     a = 10
#     b = 0
#     print(a/b)
#  except ZeroDivisionError:
#      print("Numbers cannot be divided by zeros")
# except ArithmeticError:
#     print("Numbers cannot be divided by zeros")

# Overflow Error
# import math

# try:
#     x = math.exp(999)
#     print(x)
# except OverflowError:
#     print("Overflow Occurs")

# # ValueError

# try:
#     x = float("Hello")
#     print(x)
# except ValueError:
#     print("Value format is wrong")

# fruits = {"name":"APPLE","colour":"Red"}
# try:
#     print(fruits["price"])
# except KeyError:
#     print("key is not available in dictionary")
# else:
#     print("Printed Successfully")