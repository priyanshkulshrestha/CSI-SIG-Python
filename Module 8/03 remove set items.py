print("Priyansh")
print("1900300100165")
a = {1,2,1,2,3,4,3,4,5,3,4,5,6,7,6,8,9}
print(f"Set a before deletion {a}")
c = int(input("Enter an element to delete from set (1-9): "))
a.discard(c)
print(f"Set a after deletion of {c}: {a}")