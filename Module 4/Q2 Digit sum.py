print("Priyansh")
print("1900300100165")
num = input("Enter any number: ")
l = len(num)
sum = 0
i = -1
while(i>=-l):
    # print(num[i])
    sum += int(num[i])
    i -= 1
print (f"sum of all digit of given number: {sum}")