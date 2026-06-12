sqr = {x: x**2 for x in range(1,6)}
print(sqr)

keys = ['a','b','c','d','e']
values = [1,2,3,4,5]

dict1 = {k:v for (k,v) in zip(keys,values)}
print(dict1)

d = dict.fromkeys(range(5), True)
print(d)

ch = {x.upper() : x*3 for x in "yousuf"}
print(ch)

length = {fruit: len(fruit) for fruit in ['Apple','Banana','Cherry']}
print(length)