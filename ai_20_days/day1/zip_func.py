a = [1,2,3]
b = ['a','b','c']

zero = zip()
print(list(zero))

one = zip(a)
print(list(one))

two = zip(a,b)
print(list(two))

# Zipping the two lists

names = ['Yousuf','Aasik','John']
number = [10,7]

res = zip(names, number)
print(list(res))

# Unzipping the list

fruits = [('Apple',10),('Banana',20),('Cherry',30)]
fruit,quantity = zip(*fruits)

print("Fruit: ",fruit)
print("Quantity: ",quantity)

# Combines the keys and values of dictionary

d = {"name":"Yousuf","age":22}
key = d.keys()
value = d.values()

res = zip(key, value)
print(list(res))