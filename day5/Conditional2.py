# Conditional Statements

# If Statement
# a = 5
# b = 3
# if a > b:
#     print("a is greater than b")

# is_loggedin = True

# if is_loggedin:
#     print("Yes")

# Elif Statement

# a = 5
# b = 5
# if a > b:
#     print("a is greater than b")

# elif a == b:
#     print("a is equal to b")

# day = 5

# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")
# elif day == 7:
#     print("Sunday")

# Else Statement

# a = 4
# b = 5
# if a > b:
#     print("a is greater than b")
# elif a == b:
#     print("a is equal to b")
# else:
#     print("a is not greater than b")

# num = 7

# if num == 0:
#     print("Neither prime nor constant")
# elif(num % 2 == 0):
#     print("Even")
# else:
#     print("Odd")

# ShortHand If and If..else

# a = 5
# b = 9

# if a > b : print("a is greater than b")
# print("a is greater than b") if a > b else print("b is greater than a") 

# max_num = a if a > b else b
# print(max_num)

# print ("a") if a > b else print("=") if a == b else print("b") 

# username = "Yousuf"
# displayname = username if username else "Guest"
# print("welcome,", displayname)

# Logical Operators

a = 5
b = 7
c = 3

# And Operator
 
# if a > b and a > c:
#     print("a is greater than b and c")

# elif b > a and b > c:
#     print("b is greater than a and c")

# else:
#     print("c is greater than a and b")

# Or Operator

# if a > b or a > c:
#     print("a is greater than both b and c")

# Not Operator

# if(not(a > b)):
#     print("a is not greater than b ")

# email = 'xxx@gmail.com'
# username = 'yousuf'
# password = '@1234'

# if (username or email) and password:
#     print("Login Successful")
# else:
#     print("Login failed")

# age = 21

# Nested if Statement
# if age > 10:
#     if age ==10:
#         print("kid")
#     elif age <20:
#         print("Teenage")
#     else:
#         print("Matured Guy")

# Nested if and logical operator

# username = 'yousuf'
# password = '@1234'
# is_active = False

# if username and password:
#     if is_active:
#         print("Login Successful")
#     else:
#         print("Status Inactive")
# else:
#     print("Username or Password is incorrect")

# Pass Statement

# age = 17

# if age < 18:
#     pass
# else:
#     print("Eligible to vote")

# Match Statement

# day = 2

# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thrusday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Looking for correct no.")

# day = 6

# match day:
#     case 1 | 2 | 3 | 4 | 5:
#         print("Weekdays")
#     case 6 | 7:
#         print("Weekends") 