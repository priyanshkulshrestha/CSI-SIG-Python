print("Priyansh")
print("1900300100165")
# using Dictionary comprehension
square = {i:i*i for i in range(1,11)}
print(square)
# by loop
sq = {}
for i in range(1,11):
    sq.update({i:i*i})
print(sq)