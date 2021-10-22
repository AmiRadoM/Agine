import math
import pygame
from .Attributes import *



class Vector2D():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.w = 1


    @staticmethod
    def Zero():
        return Vector2D(0,0)

    @staticmethod
    def ListToVector2D(list):
        return Vector2D(list[0], list[1])

    def Normalize(self):
        if (self == Vector2D.Zero()):
            return Vector2D.Zero()
        else:
            length = math.sqrt(self.x * self.x + self.y * self.y)
            return self / length


    def ToList(self):
        return [self.x, self.y]



    def __int__(self):
        return Vector2D(int(self.x), int(self.y))


    def __str__(self):
        return "Vector2D("+str(self.x)+", "+str(self.y)+")"

    def __iadd__(self, other):
        return self + other

    def __isub__(self, other):
        return self - other

    def __imul__(self, other):
        return self * other

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)

    def __add__(self, other):
        if (type(other) == int or type(other) == float):
            return Vector2D(self.x + other, self.y + other)
        if (type(other) == Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if (type(other) == int or type(other) == float):
            return Vector2D(self.x - other, self.y - other)
        if (type(other) == Vector2D):
            return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if (type(other) == int or type(other) == float):
            return Vector2D(self.x * other, self.y *other)
        if (type(other) == Vector2D):
            return Vector2D(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        if (type(other) == int or type(other) == float):
            return Vector2D(self.x / other, self.y / other)
        if (type(other) == Vector2D):
            return Vector2D(self.x / other.x, self.y / other.y)

    def  __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __abs__(self):
        return Vector2D(abs(self.x), abs(self.y))

    def __pow__(self, power):
        result = 1
        for i in range(power):
            result = self * result
        return result




sprite = []
class Sprite(Attribute):
    def __init__(self, imagePath = None, color = (255,255,255,255)):
        self.imagePath = imagePath
        self.color = color




line = []
class Line(Attribute):
    def __init__(self, startPoint = Vector2D(0,0), endPoint = Vector2D(0,0),color = [0,0,0], width = 1):
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.color = color
        self.width = width



square = []
class Square(Attribute):
    def __init__(self, width = 0, color = (0,0,0)):
        self.width = width
        self.color = color

polygon = []
class Polygon(Attribute):
    def __init__(self,points = [Vector2D(0,0),Vector2D(10,0),Vector2D(10,10)],color = (0,0,0), width = 0):
        self.points = points
        self.color = color
        self.width = width


circle = []
class Circle(Attribute):
    def __init__(self, radius = 100, color = (0,0,0),width = 0 ):
        super().__init__()
        self.radius = radius
        self.color = color
        self.width = width



