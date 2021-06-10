# Name Priyansh
# roll no. 1900300100165
a,b,c = input("Enter three side of triangle seperated using comma : ").split(",")
a = int(a)
b = int(b)
c = int(c)
if a==b and b==c and a==b:
    print("This is equilateral triangle.")
elif a==b or a==c or b==c:
    print("This is isoscale triangle.")
else:
    print("This is scalence triangle.")