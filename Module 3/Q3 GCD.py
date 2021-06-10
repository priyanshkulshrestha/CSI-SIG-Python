# Name Priyansh
# roll no. 1900300100165
print("Enter two number for finding GCD")
n1 = int(input("Enter the first number : "))
n2 = int(input("Enter the second number : "))
i = 1
gcd = 1
while i<=n1 and i <=n2:
    if (n1%i == 0 and n2%i == 0):
        gcd = i
    i += 1
print(f"G.C.D. of {n1} and {n2} : {gcd}")