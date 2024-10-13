class Shape:
    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
     
     def __init__(self,length,width):
         self.length = length
         self.width = width
     
     def area(self):
        result = self.length * self.width
        return result

class circle(Shape):
     
     def __init__(self,radius):
         self.radius = radius
     
     def area(self):
        result = self.radius**2
        return result
