# Name Priyansh
# roll no. 1900300100165
limit = int(input("Enter the limit upto you want to print fibbonaci series : "))
a =0; b=1
print(f"fibbonaci series : {0}, {1}",end = "")
next = a + b
while next < limit:
    print(f", {next}", end= "")
    a = b
    b = next
    next = a + b