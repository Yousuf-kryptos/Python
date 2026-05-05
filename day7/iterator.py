# Iterator - is an object that will traverse through all the values which consists of methods:
# __iter__() and __next__()
# List, tuple, dictionary , set and string are all iterable objects

# fruits = ("Apple","Banana","Cherry")
# my_it = iter(fruits)

# print(next(my_it))
# print(next(my_it))
# print(next(my_it))

# name = "Yousuf"
# myit = iter(name)

# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

# class MyNumber:
#     def __iter__(self):
#         self.a = 1
#         return self
    
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x

# demo = MyNumber()
# myit = iter(demo)

# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

num = MyNumbers()
myit = iter(num)

for x in myit:
    print(x)