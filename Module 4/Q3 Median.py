print("Priyansh")
print("1900300100165")
a,b,c = input("Enter any three number seperated using comma : ").split(",")
if (a>b and a>c):
    if(b>c):
        med = b
    else:
        med = c
elif (b>a and b>c):
    if(a>c):
        med = a
    else:
        med = c
else:
    if(a>b):
        med = a
    else:
        med = b
print(f"Median of {a}, {b}, {c} =  {med}")