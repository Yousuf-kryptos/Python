# Range - built-in functions immutable sequence commonly used for looping
# range(start, stop, step)

# Calling only one argument - indicates stop value only and start is optional and set to 0 by default

# x = range(10)
# print(x)
# print(list(x))

# Calling two arguments - indicates first argument is start value and second argument is stop value

# x = range(5,10)
# print(x)
# print(list(x))

# Calling three arguments - indicates first argument is start value,
# second argument is stop value and third argument is step value

# x = range(2,10,2)
# print(x)
# print(list(x))

# Using in for loop

# for i in range(0,5):
#     print(i)

# List

# print(list(range(8)))
# print(list(range(0,8)))
# print(list(range(0,8,2)))

# Slicing

# r = range(10)
# print(r[3])
# print(r[:3])
# print(r[2:])

# Membership Testing

# r = range(0,10,2)
# print(6 in r)
# print(9 in r)

# Length of the Range

# r = range(0,10,2)
# print(len(r))

# Arrays - is used to store multiple values in single variable

# cars = ["Ford","Volvo","BMW"]

# Access the array

# x = cars[1]
# print(x)

# Modify the array

# cars[0] = "Audi"
# print(cars)

# print(len(cars))                   # Length of an array

# for x in cars:                       # Looping through an array
#     print(x)

# Built-in Methods in Array

# Adding the element
# cars.append("Ferrari")
# print(cars)

# Removing the element
# cars.pop(1)
# print(cars)

# cars.remove("Ford")
# print(cars)

# cars2 = ["RollsRoyce","Bugatti","Pagani"]
# cars.extend(cars2)
# print(cars)

# cars.insert(2,"F1")
# print(cars)

# cars.sort()                      # Ascending Order
# print(cars)
# cars.sort(reverse=True)          # Descending Order
# print(cars)

# cars.reverse()
# print(cars)

# new_cars = cars.copy()
# print(new_cars)

# cars.clear()
# print(cars)

# cars = ["Ford","Volvo","BMW","Ford"]
# x = cars.count("Ford")
# print(x)