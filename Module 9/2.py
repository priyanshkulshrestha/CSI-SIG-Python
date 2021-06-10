print("Priyansh")
print("1900300100165")

a = input("Enter string to append in file: ")
with open("1.txt", 'a') as f:
    f.write(f"\n{a}")

with open("1.txt", "r") as f:
    print(f.read())