# Lists - Ordered ,Changeable and allow duplicate values

# fruits = ["apple","cherry","Banana","Orange","apple"]
# print(fruits)

# print(fruits[3])
# fruits[1] = "Grapes"
# print(fruits)

# fruits = list(("apple","orange","banana")) # list constructor
# print(fruits)
# print(type(fruits))

# fruits = ["apple","cherry","Banana","Orange","apple"]

# print(fruits[1:4])
# print(fruits[::-1])
# print(fruits[:4])
# print(fruits[2:])

# if "cherry" in fruits:
#     print("Included")

# if "Potato" not in fruits:
#     print("Not Included")

# fruits[1:3] = ["watermelon","kiwi"]
# print(fruits)

# fruits[1:3] = ["watermelon"]
# print(fruits)

# fruits = ["apple","cherry","Banana","Orange","apple"]
# fruits.insert(2,"watermelon")
# print(fruits)

# fruits[3:4]=["Mango","Litchi"]
# print(fruits[4])
# print(fruits)

# fruits.append("Guava")
# print(fruits)

# vegetables = ["Tomato","Onion","Potato"]
# fruits.extend(vegetables)
# print(fruits)

# tup = (1,2,3)
# fruits.extend(tup)
# print(fruits)

# fruits.remove("apple") # removes first occurence of the specified 
# print(fruits)

# fruits.pop(3) # remove at specified index
# print(fruits)

# fruits.pop() # removes last element in the list
# print(fruits)

# vegetables = ["Tomato","Onion","Potato"]
# del vegetables[0]
# del vegetables 
# print(vegetables) # It will show error because we already deleted the list

# vegetables.clear()
# print(vegetables)

# fruits = ["apple","cherry","Banana","Orange","apple"]

# for x in fruits:
#     print(x)

# for x in range(len(fruits)):
#     print(fruits[x])

# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i +=1

# new_list = []
# for x in fruits:
#     new_list.append(x)
# print(new_list)

# Instead of this we use Short Hand For loop to create new list

# new_list = [x for x in fruits]
# print(new_list)

# new_list = [x for x in fruits if "a" in x]
# print(new_list)

# fruits = ["Apple","Cherry","Banana","Orange","Apple"]

# fruits.sort() # Ascending Order
# print(fruits)


# fruits.sort(reverse=True) # Descending Order
# print(fruits)

# def myFunc(x):
#     return abs(x-50)

# num = [100,50,20,35]
# num.sort(key=myFunc)
# print(num)

# fruits.reverse()
# print(fruits)

# new_fruits = fruits.copy()
# print(new_fruits)

# new_fruits = fruits[:]
# print(new_fruits)

# fruits = ["Apple","Cherry","Banana","Orange","Apple"]
# num = [100,50,20,35]

# new_list = fruits + num
# print(new_list)
# fruits.extend(num)
# print(fruits)

# print(fruits.count("Apple"))

