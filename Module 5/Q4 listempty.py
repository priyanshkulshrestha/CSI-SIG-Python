print("Priyansh")
print("1900300100165")
li = []
a = int(input('Do you want to enter element (0 or 1) : '))
while(a):
    li.append(input("Enter element : "))
    a = int(input('Do you want to enter element (0 or 1): '))
if(len(li)):
    print("list is not empty")
else:
    print("list is empty")