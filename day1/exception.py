# # Exception Handling
# try:
#     n = 0
#     res = 100/n

# except ZeroDivisionError:
#     print("Number cannot be divided by zero")

# except ValueError:
#     print("Invalid Number")

# else:
#     print("Result is",res)

# finally:
#     print("Executed well")

# # Multiple Exception
# a = ["10","Yousuf",20]

# try:
#     res = int(a[0]) + int(a[1])

# except (ValueError,TypeError) as e:
#     print("Error",e)

# finally:
#     print("Executed well")

# # use only except to catch the error
# try:
#     res = "100"/20

# except ArithmeticError:
#     print("Arithmetic Error")

# except:
#     print("Error Occured")

# # Raise an Exception
# def setAge(x):
#     if x<0:
#         raise ValueError("Age cannot be negative")
#     print(f"Age is {x}")

# try:
#     setAge(-5)
# except TypeError:
#     print("Invalid value")

# # Custom Exception
# def MyCustomError(Exception):
#     def __init__(self,message,error_code):
#         super().__init__(message)
#         self.error_code=error_code

#     def __str__(self):
#         return(f"{self.message} (Error code:{self.error_code})")
    
# def divide(a,b):
#     if b==0:
#         raise MyCustomError("DIVIDE BY ZERO IS NOT ALLOWED",400)
#     return a/b

# try:
#     res = divide(10,0)
# except MyCustomError as e:
#     print(f"Custom Error:{e}")