print("Priyansh")
print("1900300100165")

def rane(num,ran):
    if num in range(1,ran):
        print(f"{num} is in range 1 to {ran}")
    else:
        print(f"{num} is not in range 1 to {ran}")

a = int(input("Enter a number: "))
b = int(input("Enter range: "))
rane(a,b)