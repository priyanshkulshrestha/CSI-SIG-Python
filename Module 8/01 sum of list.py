print("Priyansh")
print("1900300100165")
# a = list(range(11)) 
a = []
x=int(input("Enter the no of element in list : "))
for i in range(x):
    _ = input(f"Enter element {i} : ")
    a.append(_)

# print(a)
print(sum([int(i) for i in a]))