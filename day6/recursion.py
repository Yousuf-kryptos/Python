# Recursions - Calls itself again and again to complete the task efficiently

# def count(n):
#     if n <= 0:
#         print("Great Work , Done")
#     else:
#         print(n)
#         count(n-1)

# count(4)

# Factorial Problem
# def fact(n):
#     if n == 0 or n == 1:                   # Base case which indicates to stop the recursion
#         return 1
#     else:
#         return n * fact(n-1)               # Recursive case which indicates that function calls itself
    
# print(fact(5))
    
# Fibonacci Problem

# def fibo(n):
#     if n<=1:
#         return n
#     else:
#         return fibo(n-1)+fibo(n-2)

# print(fibo(7))

# List Sum

# def sum_list(numbers):
#     if len(numbers)<=0:
#         return 0
#     else:
#         return numbers[0]+sum_list(numbers[1:])
    
# numbers=[1,2,3,4,5]
# print(sum_list(numbers))

# Maximum in the List

# def max_list(num):
#     if len(num) == 1:
#         return num[0]
#     else:
#         max_of_rest = max_list(num[1:])
#         return num[0] if num[0] > max_of_rest else max_of_rest

# numbers = [3,25,0,9,4]
# print(max_list(numbers))

# To check the recursion limit

# import sys
# print(sys.getrecursionlimit())


# Generators - we use Generators to pause and resume the execution 
# In this , we use yield() methods to pause and when function called again it will execute from where it stops

# def my_generator():
#     yield 1
#     yield 2
#     yield 3

# for value in my_generator():
#     print(value)

# When yield is encountered, the function's state is saved, and the value is returned. 
# The next time the generator is called, it continues from where it left off.

# def count_up_to(n):
#     count = 1
#     while count<=n:
#         yield count
#         count +=1

# for num in count_up_to(5):
#     print(num)

# def simple_gen():
#     yield "Yousuf"
#     yield "Aasik"
#     yield "Down"

# gen = simple_gen()
# print(next(gen))
# print(next(gen))
# print(next(gen))

# gen_exp = (x*x for x in range(5))
# print(gen_exp)
# print(list(gen_exp))

# def fibo():
#     a,b = 0,1
#     while True:
#         yield a
#         a,b = b,a+b

# gen = fibo()
# for _ in range(100):
#     print(next(gen))