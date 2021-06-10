print("Priyansh")
print("1900300100165")

a = [1,2,3,"a","bcd",2.0]
with open("1.txt","a") as f:
    for i in a:
        f.write(f"\n{i}")

with open("1.txt","r") as f:
    print(f.read())