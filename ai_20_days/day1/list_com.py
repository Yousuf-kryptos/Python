a = [2,3,4,5,6]
new_list = [val ** 2 for val in a]
print(new_list)

num = [i for i in range(10)]
print(num)

c = [(x,y) for x in range(3) for y in range(3)]
print(c)

mat=[[1,2,3],[4,5,6],[7,8,9]]
res = [val for row in mat for val in row]
print(res)