# # List
# l1 = [1,2,3,4] # List of int
# l2 = ["apple",'banana','cherry'] # List of strings
# l3 = [1,2.5,'high',True] # List of mixed data
# print(l1)
# print(l2)
# print(l3)

# l4 = list("GFG")
# l5 = list((1,2,3,4))
# print(l4)
# print(l5)

# l1 = [2]*5
# print(l1)

# # Methods to add the elements in list
# s = ["Yousuf",1,3.5]
# print(s[2])
# print(s[-3])
# print(s[1:3])

# s.append(10)
# print(s)

# s.insert(1,"Aasik")
# print(s)

# s.extend([3,4,5])
# print(s)

# s.clear()
# print(s)

# # Update the list
# s = [1,2,3,4]
# s[1] = 20
# print(s)

# # Remove elements from list
# s = [1,2,3,4]
# popped_val = s.pop(2)
# print(popped_val)
# print(s)

# s.remove(2)
# print(s)

# del s[0]
# print(s)

# squares = [x**2 for x in range(0,6)]
# print(squares)

# # Tuples - Tuples are similiar to lists but they cannot be changed after creation
# t = ("Yousuf",1)
# print(t)

# l1 = [1,2,3,4,"yousuf"]
# print(tuple(l1))

# t2 = tuple("Yousuf")
# print(t2)

# tup = ("It","is a","Warm day")
# a,b,c = tup
# print(a)
# print(b)
# print(c)

# t = (1,2,3,4,5)
# a,*b,c = t
# print(a)
# print(b)
# print(c)

# del t
# print(t)

# # Concatenate two tuples
# t1 = (1,2,3,4)
# t2 = ("Yousuf","Aasik")
# print(t1 + t2)

# # Dictionary
# data = {"name":"Yousuf","age":21}
# print(data)

# data2 = dict(a=1,b=2,c=3)
# print(data2)

# data["age"]=22
# print(data)

# data["city"]="Chennai"
# print(data)

# del data["city"]
# print(data)

# values = data.pop("age")
# print(values)

# key,value = data.popitem()
# print(f"Key:{key},Value:{value}")

# d = {1:"one",2:"two",3:"three"}
# for key in d:
#     print(key)
    
# for value in d.values():
#     print(value)
    
# for key,value in d.items():
#     print(f"{key}:{value}")

# d = {1:"one",2:"two",3:{"name":"Yousuf","age":21}}
# print(d.get(3))
    
