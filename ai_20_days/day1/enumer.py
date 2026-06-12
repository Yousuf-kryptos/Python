a = ["python","java","FastAPI"]
for i,v in enumerate(a):
    print(i,v)

res = list(enumerate(a))
print(res)

e = enumerate(a)

print(next(e))
print(next(e))
print(next(e))

d ={"a":10,"b":20}
for i,(k,v) in enumerate(d.items()):
    print(i,k,v)
