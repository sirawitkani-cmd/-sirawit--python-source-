"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""
class Rectangle:
    def __init__(self, lenght, width):
        self.__lenght = lenght
        self.__width = width

    def getArea(self):
        return f"Area of {self.__width} width and{self.__lenght} length = {self.__width * self.length}"
    
    def getPerimeter(self):
        return f"Area of {self.__width} width and{self.__lenght} length = {2 *(self.__width + self.length)}"

    def isSquarea(self):
        return seld.__width == self.__length

myRectangle = Rectangle(5,10)
print(myRectangle.getArea())

myRectangle2 = Rectangle(10,10)
print(myRectangle.isSquare())


