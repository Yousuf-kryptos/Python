# Dictionary - Ordered, Changeable and does not allow duplicates

# car = {
#     "brandname":"TATA",
#     "model":"SIERRA",
#     "year":2025,
#     "price":[65000,75000,80000]
# }
# print(car)
# print(car.get("year"))
# print(car.keys())

# car["colour"] = "Yellow"
# print(car.items())
# print(car.keys())
# print(car.values())

# Update the values

# car["year"] = 2026
# print(car.items())
# car.update({"year":2025})
# print(car.items())

# Adding the items

# car["country"] = "India"
# print(car.items())
# car.update({"state":"TamilNadu"})
# print(car.keys())

# Removing the items

# car.pop("model")            # Remove the specified item
# car.popitem()               # Remove the last inserted item
# del car["model"]
# del car
# print(car)
# car.clear()
# print(car.keys())

# Looping through dictionary

# for x in car:                   # Return keys in the dictionary
#     print(x)

# for x in car:                   # Return values in the dictionary
#     print(car[x])

# for x in car.values():          # Return values in the dictionary
#     print(x)

# for x in car.keys():            # Return keys in the dictionary
#     print(x)

# for x,y in car.items():         # Return both keys and values
#     print(x,y)

# Copying Dictionaries

# new_dict = car.copy()
# print(new_dict)

# new_dict = dict(car)
# print(new_dict)

# Multiple Dictionaries

# fruits ={
#     "Apple":{
#         "color":"Red",
#         "seeds":"yes"
#     },
#     "Orange":{
#         "color":"orange",
#         "seeds":"yes"
#     },
#     "Grapes":{
#         "color":"green",
#         "seeds":"no"
#     }
# }

# print(fruits["Apple"]["color"])
# print(fruits["Grapes"]["seeds"])
# print(fruits["Orange"])

# Apple = {
#     "color":"Red",
#     "seeds":"yes"
#     }
# Orange = {
#     "color":"orange",
#     "seeds":"yes"
#     }
# Grapes = {
#     "color":"green",
#     "seeds":"no"
#     }

# fruits = {
#     "Apple":Apple,
#     "Orange":Orange,
#     "Grapes":Grapes
# }

# print(fruits["Apple"]["color"])
# print(fruits["Grapes"]["seeds"])
# print(fruits["Orange"])

# for x,obj in fruits.items():
#     print(x)

#     for y in obj:
#         print(y + ':'+obj[y])

# x = ("key1","key2","key3")
# y = 0

# new_dict = dict.fromkeys(x,y)
# print(new_dict)

# x = ("key1","key2","key3")

# new_dict = dict.fromkeys(x)
# print(new_dict)