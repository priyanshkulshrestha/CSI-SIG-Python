print("Priyansh")
print("1900300100165")

list1 = [1,2,3,4,5]
with open("a.txt","a") as file:
    for i in list1:
        file.write(f"\t{i}")

with open("a.txt","r") as file:
    print(file.read())