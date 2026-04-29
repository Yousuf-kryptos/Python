# Sets - Unordered, Unchangable and not allow duplicate values but able to remove and add new items

# fruits = {"apple","banana","apple","orange",True,1,0,False,2} # True and 1 are same & False and 0 are same
# print(fruits)

# print(len(fruits))

# fruits = set(("apple","orange","banana")) # set constructor
# print(fruits)

# In Sets, we cannot be able to access items items through index

# fruits = {"apple","banana","orange"}
# for x in fruits:
#     print(x)

# print("apple" in fruits)
# print("orange" not in fruits)

# fruits.add("watermelon")
# print(fruits)

# vegetables ={"tomato","onion","carrot"}
# fruits.update(vegetables)                # add current set into existing set
# print(fruits)

# num = [1,2,3]
# fruits.update(num)
# print(fruits)

# fruits = {"apple","banana","orange"}

# fruits.remove("banana")
# fruits.remove("papaya") # If the value is not in the fruits then it will raise error Instead use discard
# fruits.discard("banana")
# fruits.discard("papaya")
# print(fruits)

# x = fruits.pop()
# print(x)

# fruits.clear()
# print(fruits)

# del fruits
# print(fruits)

# for x in fruits:
#     print(x)

# fruits = {"apple","banana","orange"}
# vegetables = {"tomato","onion","potato"}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}

# f_v = fruits | vegetables
# f_v1 = fruits.union(vegetables,set3,set4)
# f_v2 = fruits | vegetables | set3 | set4
# print(f_v)
# print(f_v1)
# print(f_v2)

# set3.update(set4)
# print(set3)

# new = fruits.intersection(set4)
# new2 = fruits & set4
# print(new)
# print(new2)

# fruits = {"apple","banana","orange"}
# fruits2 = {"apple", "bananas", "cherry"}

# fruits3 = fruits.difference(fruits2) # contains values from first set other than same from both
# fruits4 = fruits2.difference(fruits) # contains values from second set other than same from both
# fruits5 = fruits - fruits2
# print(fruits3)
# print(fruits4)
# print(fruits5)

# fruits6 = fruits.symmetric_difference(fruits2) # contains values other than same values
# fruits7 = fruits ^ fruits2
# print(fruits6)
# print(fruits7)

# FrozenSet - it is like Set but does not allow add and remove elements

x = frozenset({"apple","banana","cherry"})
# print(x)
# print(type(x))

# Immutable frozenset methods

# y = x.copy()
# print(y)
# k = frozenset({1,2,3})
# l = frozenset({3,4,5})

# print(k.difference(l))
# print(k-l)
# print(k & l)
# print(k.isdisjoint(l))

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)
a = y.issuperset(x)
print(z)
print(a)