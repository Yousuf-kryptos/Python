# String Formatting

# name = "Yousuf"
# print(f"My name is {name}")

# Amount = 1500
# print(f"Actual Amount is {Amount:.2f} and Discounted Amount is {1450:.2f}")

# Operations in Formatting String

# print(f"Amount is {20*30}")

# if..else in Formatting String

# n=45
# print(f"It is {'Expensive' if n >50 else 'Cheap'}")

# fruit = "Apples"
# print(f"I Love {fruit.upper()}")

# def myconvertor(x):
#     return x * 1000

# print(f"2 kilometre is equal to {myconvertor(2)} metre")

# num = 4000
# print(f"Thousand Seperator:{num:,}")

# quantity = 3
# itemno = 567
# price = 49
# myorder = "I want {} pieces of item number {} for {:.2f} dollars."
# print(myorder.format(quantity, itemno, price))

# name = "Yousuf"
# age = 21
# txt = "His name is {0}. {0} is {1} years old"
# print(txt.format(name,age))


# txt = "His name is {name}. {name} is {age} years old"
# print(txt.format(name = "Yousuf",age = 21))

# None

# x = None
# print(x)
# print(type(x))
# print(bool(None))

# if x is None:
#     print("None is a NoneType")
# else:
#     print("Done")

# if x is not None:
#     print("None is a NoneType")
# else:
#     print("Done")

# def myfunc():
#     x = 5

# x = myfunc()
# print(x)