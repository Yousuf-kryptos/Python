# #Input and ouput 
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# x, y = input("Enter two numbers: ").split()
# z = float(input("Enter float number: "))
# print(name,age,x,y,z)

# #Multiple inputs
# x = y = z =100
# print(x,y,z)

# x=200
# print(x)

# m,n = 2,"two"
# print(m,n)

# # type() function
# m = 10
# n = "Yousuf"
# p = [1,2]
# q = (3,4)
# print(type(m))
# print(type(n))
# print(type(p))
# print(type(q))

# print(type(m) is type(n))
# r=20
# print(type(m) is type(r))

# A = type("A",(),{"n":5,"show":lambda self:self.n})
# obj =A()

# print(type(obj))
# print(obj.show())
# print(obj.n)

# Type Casting - Implicit and Explicit Typecasting
# Implicit Typecasting
# a = 5 #Automatically convert 'a' to int
# b = 3.5 #Automatically convert 'b' to float
# print(type(a))
# print(type(b))
# c=a+b #Automatically convert 'c' to float
# print(type(c))

# Explicit Typecasting
# n = 5
# m = float(n) # Explicitly convert int to float 

# print(m)
# print(type(m))

# s = "4"
# t = int(s) # Explicitly convert string to int

# print(t)
# print(type(t))

# If string does not contain integer while casting then it will show error
# s = 't'
# t = int(s) # Error : String does not contain int

# print(t)
# print(type(t))

# a = 5
# b = str(a) # Explicitly convert int to string

# print(b)
# print(type(b))

# # Deleting the variable
# x = 10
# del x
# print(x)

# Swapping the variables
# a,b = 10,20
# print(a,b)

# a,b = b,a
# print(a,b)

# # Counting Characters
# name = "Yousuf"
# length = len(name)
# print(length)

# Identity Operator
# a = 5
# b = 10
# print(a is b)
# print(a is not b)

# # Membership Operator
# m = 2
# n = [1,2,3,4]
# if(m in n):
#     print("m is included in n")
# else:
#     print("m is not included in n")
    
# # Ternary Operator
# a = 10
# b = 5
# min = a if a<b else b
# print(min)

# # Use of Lambda Keyword
# a=lambda b:b+1

# for i in range(1,5):
#     print(a(i))
    
# # Break and Continue
# for i in range(1,10):
#     print(i)
    
#     if(i<5):
#         continue
    
#     else:
#         break

# # del keyword usage
# a=[1,2,3,4,5]
# del a[2]
# print(a)

# # Accessing the string 
# s = "Yousuf"
# print(s[1])
# print(s[4])
# print(s[-1])

# # Set
# s1 = set()

# s1 = set("yousuf")
# print(s1)
# s2 = set(["yousuf","aasik","yousuf"])
# print(s2)

# # Dictionary
# s = {1:"Yousuf",2:"Aasik",3:"Yousuf"}
# print(s)
# print(s[2])
# print(s.get(3))
