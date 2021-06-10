print("Priyansh")
print("1900300100165")

a = {1:2,2:4,3:6,4:8,5:10}

m=1
for i in a:
    m *= i
print(f"product of all keys : {m}")

m=1
for i in a.values():
    m *= i
print(f"product of all values : {m}")

m = 1
for i, j in a.items():
    m *= i*j
print(f"product of all items : {m}")