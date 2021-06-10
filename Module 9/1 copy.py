print("Priyansh")
print("1900300100165")

s = int(input("Enter a no.: "))
i = 0 
with open("a.txt", 'r') as file:
    for i in range(s):
        print(file.readline())