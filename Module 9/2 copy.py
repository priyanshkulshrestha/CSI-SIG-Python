print("Priyansh")
print("1900300100165")

string = input("Enter string to be appended: ")
with open("a.txt", 'a') as file:
    file.write(string)

with open("a.txt", "r") as file:
    print(file.read())