# Tuples - Ordered, Unchangable and immutable but contains duplicate values

# fruits = ("apple","banana","orange")
# print(fruits)
# print(len(fruits))

# print(type(fruits))
# new = ("apple")
# print(type(new))

# vegetables = tuple(("tomato","potato","onion")) # Tuple Constructor
# print(vegetables)
# print(fruits[2])
# print(fruits[1:])
# print(fruits[-3:-1])

# Tuple is unchangeable and immutable, so we have to convert tuple to list then 
# make the changes and convert it back into tuple

# fruits = ("apple","banana","orange")
# fruits_list = list(fruits)           # First, convert tuple to list
# fruits_list.append("Guava") 
# fruits_list.remove("banana")         # Then , add/append the elements in the list
# fruits = tuple(fruits_list)          # And convert it back into tuple
# print(fruits)

# OR you can declare new tuple with elements and concatenate them

# new_fruits = ("watermelon",)
# fruits +=new_fruits
# print(fruits)

# del new_fruits
# print(new_fruits)                  # Raise error because new_fruits tuple is deleted

# fruits = ("apple","banana","watermelon","Guava","Cherry")
# red,yellow,green = fruits
# print(red)
# print(yellow)
# print(green)

# red,yellow,*green = fruits         # Asterik is used to make the list of more than one values
# print(red)
# print(yellow)
# print(green)

# red,*yellow,green = fruits
# print(red)
# print(yellow)
# print(green)

# fruits = ("apple","banana","watermelon","Guava","Cherry")
# for x in fruits:
#     print(x)

# i = 0
# while i<len(fruits):
#     print(fruits[i])
#     i +=1


# num = (1,2,3,4,5)
# res = fruits + num
# res = fruits * 2
# print(res)


# fruits = ("apple","banana","watermelon","apple","Cherry")
# x = fruits.count("apple")
# print(x)

# i = fruits.index("banana")
# print(i)