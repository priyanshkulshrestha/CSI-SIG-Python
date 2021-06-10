print("Priyansh")
print("1900300100165")

class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        a = self.radius**2*3.14
        return a

    def parameter(self):
        p = 2*self.radius*3.14
        return p

circle = Circle(1)
print(circle.area())
print(circle.parameter())