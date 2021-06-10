print("Priyansh")
print("1900300100165")

a = int(input("Enter no of line to read: "))
i = 0 
with open("1.txt", 'r') as f:
    for i in range(a):
        print(f.readline())