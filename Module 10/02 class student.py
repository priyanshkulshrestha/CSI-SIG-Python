print("Priyansh")
print("1900300100165")

class Student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
        self.age = ""
        self.mark = ""
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll no.: {self.roll}")
        if(self.age != ""):
            print(f"Age: {self.age}")
        if(self.mark != ""):
            print(f"Mark: {self.mark}")  
    def setAge(self):
        self.age = int(input("Enter age of {self.name}: "))

    def setMarks(self):
        self.mark = int(input("Enter marks of {self.name}: "))

s1 = Student("Priyansh",165)
s1.display()
s1.setAge()
s1.setMarks()
s1.display()