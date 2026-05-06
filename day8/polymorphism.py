# Polymorphism - means Many Forms and it refers to methods/functions/operators have same name in different classes and perform different tasks

# Method Overloading - Compile Time Polymorphisms
# class Calculator:
#     def multiply(self,*args):
#         res = 1
#         for nums in args:
#             res *= nums
#         return res

# c1 = Calculator()
# print(c1.multiply(3,4,5))

# Method Overriding - RunTime Polymorphisms
# class Student:
#     def speak(self):
#         print("Student speaks")

# class Leader(Student):
#     def speak(self):
#         print("Leader guides others")

# class Athlete(Leader):
#     def speak(self):
#         print("Athlete motivates team")

# s1 = Student()
# s2 = Leader()
# s3 = Athlete()

# s1.speak()
# s2.speak()
# s3.speak()