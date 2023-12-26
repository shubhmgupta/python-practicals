# WAP to define a class Point with coordinates x and y as attributes. Create relevant methods and print the objects. Also define a method distance to calculate the distance between any two point objects.
class Point:
    count=0
    def __init__(self,x,y):
        self.x=x
        self.y=y
        Point.count+=1
    def __str__(self):
        return f"X : {self.x}, Y : {self.y}"
    def __del__(self):
        Point.count-=1
        return f"{self} is deleted"
    def Distance(self,x,y):
        x1=self.x
        y1=self.y
        x2=x
        y2=y
        distance=((x2-x1)**2+(y2-y1)**2)**0.5
        return distance
ob1=Point(3,4)
ob2=Point(1,0)
d=ob1.Distance(0,0)
print(d)
del ob2
print(Point.count)
