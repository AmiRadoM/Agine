from .Attributes import *
from .Objects2D import Vector2D
import math

class Vector3D():
    def __init__(self, x = 0, y = 0, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.w = 1


    @staticmethod
    def Zero():
        return Vector3D(0,0,0)

    @staticmethod
    def One():
        return Vector3D(1, 1, 1)

    @staticmethod
    def Up():
        return Vector3D(0, 1, 0)

    @staticmethod
    def Forward():
        return Vector3D(0, 0, 1)

    @staticmethod
    def Right():
        return Vector3D(1, 0, 0)

    @staticmethod
    def ListToVector3D(list):
        if (len(list) == 3):
            return Vector3D(list[0], list[1], list[2])
        else:
            raise ValueError("Expected 3 Values in the list, but got " + str(len(list)))

    def Normalize(self):
        if (self == Vector3D.Zero()):
            return Vector3D.Zero()
        else:
            length = math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
            return self / length

    def ToList(self):
        return [self.x, self.y, self.z]

    def ToVector2D(self):
        return Vector2D(self.x, self.y)

    def DotProduct(self, vector):
        return self.x * vector.x + self.y * vector.y + self.z * vector.z

    def CrossProduct(self, vector):
        v = Vector3D()
        v.x = self.y * vector.z - self.z * vector.y
        v.y = self.z * vector.x - self.x * vector.z
        v.z = self.x * vector.y - self.y * vector.x
        return v

    @staticmethod
    def IntersectWithPlane(planePoint, planeNormal, lineStart, lineEnd):
        planeNormal = planeNormal.Normalize()
        planeD = -planeNormal.DotProduct(planePoint)
        aD = lineStart.DotProduct(planeNormal)
        bD = lineEnd.DotProduct(planeNormal)
        t = (-planeD - aD) / (bD - aD)
        lineStartToEnd = lineEnd - lineStart
        lineToIntersect = lineStartToEnd * t
        return lineStart + lineToIntersect, t

    def __int__(self):
        return Vector3D(int(self.x), int(self.y), int(self.z))

    def __len__(self):
        return math.sqrt(self.DotProduct(self))

    def __str__(self):
        return "Vector3D("+str(self.x)+", "+str(self.y)+", "+str(self.z)+")"

    def __iadd__(self, other):
        return self + other

    def __isub__(self, other):
        return self - other

    def __imul__(self, other):
        return self * other

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y and self.z == other.z)

    def __add__(self, other):
        if (type(other) == int or type(other) == float):
            return Vector3D(self.x + other, self.y + other, self.z + other)
        if (type(other) == Vector3D):
            return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
        if (type(other) == Vector2D):
            return Vector3D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if (type(other) == int or type(other) == float):
            return Vector3D(self.x - other, self.y - other, self.z - other)
        if (type(other) == Vector3D):
            return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
        if (type(other) == Vector2D):
            return Vector3D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if (type(other) == int or type(other) == float):
            return Vector3D(self.x * other, self.y * other, self.z * other)
        if (type(other) == Vector3D):
            return Vector3D(self.x * other.x, self.y * other.y, self.z * other.z)
        if (type(other) == Vector2D):
            return Vector3D(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        if (type(other) == int or type(other) == float):
            return Vector3D(self.x / other, self.y / other, self.z / other)
        if (type(other) == Vector3D):
            return Vector3D(self.x / other.x, self.y / other.y, self.z / other.z)
        if (type(other) == Vector2D):
            return Vector3D(self.x / other.x, self.y / other.y)

    def  __neg__(self):
        return Vector3D(-self.x, -self.y, -self.z)

    def __abs__(self):
        return Vector3D(abs(self.x), abs(self.y), abs(self.z))

    def __pow__(self, power):
        result = 1
        for i in range(power):
            result = self * result
        return result

class Matrix4x4():
    def __init__(self):
        self.matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    @staticmethod
    def MakeIdentity():
        matrix = Matrix4x4()
        matrix.matrix[0][0] = 1
        matrix.matrix[1][1] = 1
        matrix.matrix[2][2] = 1
        matrix.matrix[3][3] = 1
        return matrix

    @staticmethod
    def MakeRotationZ(angle):
        matrix = Matrix4x4()
        matrix.matrix[0][0] = math.cos(angle)
        matrix.matrix[0][1] = math.sin(angle)
        matrix.matrix[1][0] = -math.sin(angle)
        matrix.matrix[1][1] = math.cos(angle)
        matrix.matrix[2][2] = 1
        matrix.matrix[3][3] = 1
        return matrix

    @staticmethod
    def MakeRotationX(angle):
        matrix = Matrix4x4()
        matrix.matrix[0][0] = 1
        matrix.matrix[1][1] = math.cos(angle)
        matrix.matrix[1][2] = math.sin(angle)
        matrix.matrix[2][1] = -math.sin(angle)
        matrix.matrix[2][2] = math.cos(angle)
        matrix.matrix[3][3] = 1
        return matrix

    @staticmethod
    def MakeRotationY(angle):
        matrix = Matrix4x4()
        matrix.matrix[0][0] = math.cos(-angle)
        matrix.matrix[0][2] = math.sin(-angle)
        matrix.matrix[2][0] = -math.sin(-angle)
        matrix.matrix[1][1] = 1
        matrix.matrix[2][2] = math.cos(-angle)
        matrix.matrix[3][3] = 1
        return matrix

    @staticmethod
    def MakeTranslation(x, y, z):
        matrix = Matrix4x4()
        matrix.matrix[0][0] = 1
        matrix.matrix[1][1] = 1
        matrix.matrix[2][2] = 1
        matrix.matrix[3][3] = 1
        matrix.matrix[3][0] = x
        matrix.matrix[3][1] = y
        matrix.matrix[3][2] = z
        return matrix

    @staticmethod
    def MakeProjection(cam, aspectRatio):
        matrix = Matrix4x4()
        matrix.matrix[0][0] = aspectRatio * cam.Camera.fovRad()
        matrix.matrix[1][1] = cam.Camera.fovRad()
        matrix.matrix[2][2] = cam.Camera.far / (cam.Camera.far - cam.Camera.near)
        matrix.matrix[3][2] = (-cam.Camera.far * cam.Camera.near) / (cam.Camera.far - cam.Camera.near)
        matrix.matrix[2][3] = 1
        return matrix

    @staticmethod
    def MakePointAt(position, target, up):
        newForward = target - position
        newForward = newForward.Normalize()

        a = newForward * up.DotProduct(newForward)
        newUp = up - a
        newUp = newUp.Normalize()

        newRight = newUp.CrossProduct(newForward)

        matrix = Matrix4x4()
        matrix.matrix[0][0] = newRight.x
        matrix.matrix[0][1] = newRight.y
        matrix.matrix[0][2] = newRight.z
        matrix.matrix[0][3] = 0

        matrix.matrix[1][0] = newUp.x
        matrix.matrix[1][1] = newUp.y
        matrix.matrix[1][2] = newUp.z
        matrix.matrix[1][3] = 0

        matrix.matrix[2][0] = newForward.x
        matrix.matrix[2][1] = newForward.y
        matrix.matrix[2][2] = newForward.z
        matrix.matrix[2][3] = 0

        matrix.matrix[3][0] = position.x
        matrix.matrix[3][1] = -position.y
        matrix.matrix[3][2] = position.z
        matrix.matrix[3][3] = 1

        return matrix

    @staticmethod
    def MakeQuickInverse(matrix): #Only For Rotation/Translation Matrices
        newMatrix = Matrix4x4()
        newMatrix.matrix[0][0] = matrix.matrix[0][0]
        newMatrix.matrix[0][1] = matrix.matrix[1][0]
        newMatrix.matrix[0][2] = matrix.matrix[2][0]
        newMatrix.matrix[0][3] = 0.0
        newMatrix.matrix[1][0] = matrix.matrix[0][1]
        newMatrix.matrix[1][1] = matrix.matrix[1][1]
        newMatrix.matrix[1][2] = matrix.matrix[2][1]
        newMatrix.matrix[1][3] = 0.0
        newMatrix.matrix[2][0] = matrix.matrix[0][2]
        newMatrix.matrix[2][1] = matrix.matrix[1][2]
        newMatrix.matrix[2][2] = matrix.matrix[2][2]
        newMatrix.matrix[2][3] = 0.0
        newMatrix.matrix[3][0] = -(matrix.matrix[3][0] * newMatrix.matrix[0][0] + matrix.matrix[3][1] * newMatrix.matrix[1][0] + matrix.matrix[3][2] * newMatrix.matrix[2][0])
        newMatrix.matrix[3][1] = -(matrix.matrix[3][0] * newMatrix.matrix[0][1] + matrix.matrix[3][1] * newMatrix.matrix[1][1] + matrix.matrix[3][2] * newMatrix.matrix[2][1])
        newMatrix.matrix[3][2] = -(matrix.matrix[3][0] * newMatrix.matrix[0][2] + matrix.matrix[3][1] * newMatrix.matrix[1][2] + matrix.matrix[3][2] * newMatrix.matrix[2][2])
        newMatrix.matrix[3][3] = 1.0
        return newMatrix

    def __mul__(self, other):
        if (type(other) == Vector3D):
            output = Vector3D()

            output.x = other.x * self.matrix[0][0] + other.y * self.matrix[1][0] + other.z * self.matrix[2][0] + other.w * self.matrix[3][0]
            output.y = other.x * self.matrix[0][1] + other.y * self.matrix[1][1] + other.z * self.matrix[2][1] + other.w * self.matrix[3][1]
            output.z = other.x * self.matrix[0][2] + other.y * self.matrix[1][2] + other.z * self.matrix[2][2] + other.w * self.matrix[3][2]
            output.w = other.x * self.matrix[0][3] + other.y * self.matrix[1][3] + other.z * self.matrix[2][3] + other.w * self.matrix[3][3]

            return output
        if (type(other) == Matrix4x4):
            output = Matrix4x4()
            for c in range(4):
                for r in range(4):
                    output.matrix[r][c] = self.matrix[r][0] * other.matrix[0][c] + self.matrix[r][1] * other.matrix[1][c] + self.matrix[r][2] * other.matrix[2][c] + self.matrix[r][3] * other.matrix[3][c]
            return output


class Triangle():
    def __init__(self, p1=Vector3D(), p2=Vector3D(), p3=Vector3D(), t1 = Vector2D(), t2 = Vector2D(), t3 = Vector2D(), color = [255,255,255]):
        self.points = [p1, p2, p3]
        self.textureCords = [t1, t2, t3]
        self.color = color


    def ClipAgainstPlane(self,planeP, planeN):
        planeN = planeN.Normalize()

        def distance(p):
            return (planeN.x * p.x + planeN.y * p.y + planeN.z * p.z - planeN.DotProduct(planeP))

        insidePoints = []
        outsidePoints = []
        insideTextures = []
        outsideTextures = []

        d0 = distance(self.points[0])
        d1 = distance(self.points[1])
        d2 = distance(self.points[2])

        if (d0 >= 0):
            insidePoints.append(self.points[0])
            insideTextures.append(self.textureCords[0])
        else:
            outsidePoints.append(self.points[0])
            outsideTextures.append(self.textureCords[0])

        if (d1 >= 0):
            insidePoints.append(self.points[1])
            insideTextures.append(self.textureCords[1])
        else:
            outsidePoints.append(self.points[1])
            outsideTextures.append(self.textureCords[1])
        if (d2 >= 0):
            insidePoints.append(self.points[2])
            insideTextures.append(self.textureCords[2])
        else:
            outsidePoints.append(self.points[2])
            outsideTextures.append(self.textureCords[2])

        if (len(insidePoints) == 0):
            return None, None
        elif (len(insidePoints) == 3):
            return self, None
        elif (len(insidePoints) == 1 and len(outsidePoints) == 2):
            a = Triangle(color=(100, 0, 0))

            a.color = self.color

            a.points[0] = insidePoints[0]
            a.textureCords[0] = insideTextures[0]

            a.points[1], t = Vector3D.IntersectWithPlane(planeP, planeN, insidePoints[0], outsidePoints[0])
            a.textureCords[1].x = t * (outsideTextures[0].x - insideTextures[0].x) + insideTextures[0].x
            a.textureCords[1].y = t * (outsideTextures[0].y - insideTextures[0].y) + insideTextures[0].y
            a.textureCords[1].w = t * (outsideTextures[0].w - insideTextures[0].w) + insideTextures[0].w

            a.points[2], t = Vector3D.IntersectWithPlane(planeP, planeN, insidePoints[0], outsidePoints[1])
            a.textureCords[2].x = t * (outsideTextures[1].x - insideTextures[0].x) + insideTextures[0].x
            a.textureCords[2].y = t * (outsideTextures[1].y - insideTextures[0].y) + insideTextures[0].y
            a.textureCords[2].w = t * (outsideTextures[1].w - insideTextures[0].w) + insideTextures[0].w

            return a, None
        elif (len(insidePoints) == 2 and len(outsidePoints) == 1):
            import copy

            a = Triangle(color=(0, 0, 100))
            a.color = self.color

            a.points[0] = insidePoints[0]
            a.points[1] = insidePoints[1]
            a.textureCords[0] = insideTextures[0]
            a.textureCords[1] = insideTextures[1]

            a.points[2], t = Vector3D.IntersectWithPlane(planeP, planeN, insidePoints[0], outsidePoints[0])
            a.textureCords[2].x = t * (outsideTextures[0].x - insideTextures[0].x) + insideTextures[0].x
            a.textureCords[2].y = t * (outsideTextures[0].y - insideTextures[0].y) + insideTextures[0].y
            a.textureCords[2].w = t * (outsideTextures[0].w - insideTextures[0].w) + insideTextures[0].w

            b = copy.deepcopy(Triangle(color=(0, 100, 0)))
            b.color = self.color
            b.points[0] = insidePoints[1]
            b.points[1] = a.points[2]
            b.textureCords[0] = insideTextures[1]
            b.textureCords[1] = a.textureCords[2]

            b.points[2], t = Vector3D.IntersectWithPlane(planeP, planeN, insidePoints[1], outsidePoints[0])
            b.textureCords[2].x = t * (outsideTextures[0].x - insideTextures[1].x) + insideTextures[1].x
            b.textureCords[2].y = t * (outsideTextures[0].y - insideTextures[1].y) + insideTextures[1].y
            b.textureCords[2].w = t * (outsideTextures[0].w - insideTextures[1].w) + insideTextures[1].w

            return a,b


mesh=[]
class Mesh(Attribute):
    cubeTriangles = [

            #SOUTH
            Triangle(Vector3D(-0.5, -0.5, -0.5), Vector3D(-0.5, 0.5, -0.5), Vector3D(0.5, 0.5, -0.5), Vector2D(0,1), Vector2D(0,0), Vector2D(1,0)),
            Triangle(Vector3D(-0.5, -0.5, -0.5), Vector3D(0.5, 0.5, -0.5), Vector3D(0.5, -0.5, -0.5), Vector2D(0,1), Vector2D(1,0), Vector2D(1,1)),

            # EAST
            Triangle(Vector3D(0.5, -0.5, -0.5), Vector3D(0.5, 0.5, -0.5), Vector3D(0.5, 0.5, 0.5), Vector2D(0,1), Vector2D(0,0), Vector2D(1,0)),
            Triangle(Vector3D(0.5, -0.5, -0.5), Vector3D(0.5, 0.5, 0.5), Vector3D(0.5, -0.5, 0.5), Vector2D(0,1), Vector2D(1,0), Vector2D(1,1)),

            # NORTH
            Triangle(Vector3D(0.5, -0.5, 0.5), Vector3D(0.5, 0.5, 0.5), Vector3D(-0.5, 0.5, 0.5), Vector2D(0,1), Vector2D(0,0), Vector2D(1,0)),
            Triangle(Vector3D(0.5, -0.5, 0.5), Vector3D(-0.5, 0.5, 0.5), Vector3D(-0.5, -0.5, 0.5), Vector2D(0,1), Vector2D(1,0), Vector2D(1,1)),

            # WEST
            Triangle(Vector3D(-0.5, -0.5, 0.5), Vector3D(-0.5, 0.5, 0.5), Vector3D(-0.5, 0.5, -0.5), Vector2D(0,1), Vector2D(0,0), Vector2D(1,0)),
            Triangle(Vector3D(-0.5, -0.5, 0.5), Vector3D(-0.5, 0.5, -0.5), Vector3D(-0.5, -0.5, -0.5), Vector2D(0,1), Vector2D(1,0), Vector2D(1,1)),

            # TOP
            Triangle(Vector3D(-0.5, 0.5, -0.5), Vector3D(-0.5, 0.5, 0.5), Vector3D(0.5, 0.5, 0.5), Vector2D(0,1), Vector2D(0,0), Vector2D(1,0)),
            Triangle(Vector3D(-0.5, 0.5, -0.5), Vector3D(0.5, 0.5, 0.5), Vector3D(0.5, 0.5, -0.5), Vector2D(0,1), Vector2D(1,0), Vector2D(1,1)),

            # BOTTOM
            Triangle(Vector3D(0.5, -0.5, 0.5), Vector3D(-0.5, -0.5, 0.5), Vector3D(-0.5, -0.5, -0.5), Vector2D(0,1), Vector2D(0,0), Vector2D(1,0)),
            Triangle(Vector3D(0.5, -0.5, 0.5), Vector3D(-0.5, -0.5, -0.5), Vector3D(0.5, -0.5, -0.5), Vector2D(0,1), Vector2D(1,0), Vector2D(1,1))

        ]

    def __init__(self):
        import pygame
        self.triangles = []
        self.texture= pygame.image.load("./Amir.png")

    def LoadFromOBJ(self, filename, hasTexture = False):
        try:
            verts = []
            with open(filename, 'r') as f:
                for line in f:
                    if (line.split(' ')[0] == 'v'):
                        if (line.split(' ')[1] == 't'):
                            v = line.split(' ')
                            v.pop(0)
                            v = [float(e) for e in v]
                            verts.append(Vector2D.ListToVector2D(v))
                        else:
                            v = line.split(' ')
                            v.pop(0)
                            v = [float(e) for e in v]
                            verts.append(Vector3D.ListToVector3D(v))
                    if (not hasTexture):
                        if (line.split(' ')[0] == 'f'):
                            fs = line.split(' ')
                            fs.pop(0)
                            fs = [e.split('/')[0] for e in fs]
                            fs = [int(e) for e in fs]
                            self.triangles.append(Triangle(verts[fs[0] - 1], verts[fs[1] - 1], verts[fs[2] - 1]))
                    else:
                        pass


            return True
        except:
            return False

cube=[]
class Cube(Mesh, Attribute):
    def __init__(self):
        super().__init__()
        self.triangles = [

            #SOUTH
            Triangle(Vector3D(-0.5, -0.5, -0.5), Vector3D(-0.5, 0.5, -0.5), Vector3D(0.5, 0.5, -0.5), Vector2D(0,1), Vector2D(0,0), Vector2D(1,0)),
            Triangle(Vector3D(-0.5, -0.5, -0.5), Vector3D(0.5, 0.5, -0.5), Vector3D(0.5, -0.5, -0.5), Vector2D(0,1), Vector2D(1,0), Vector2D(1,1)),

            # EAST
            Triangle(Vector3D(0.5, -0.5, -0.5), Vector3D(0.5, 0.5, -0.5), Vector3D(0.5, 0.5, 0.5), Vector2D(0,1), Vector2D(0,0), Vector2D(1,0)),
            Triangle(Vector3D(0.5, -0.5, -0.5), Vector3D(0.5, 0.5, 0.5), Vector3D(0.5, -0.5, 0.5), Vector2D(0,1), Vector2D(1,0), Vector2D(1,1)),

            # NORTH
            Triangle(Vector3D(0.5, -0.5, 0.5), Vector3D(0.5, 0.5, 0.5), Vector3D(-0.5, 0.5, 0.5), Vector2D(0,1), Vector2D(0,0), Vector2D(1,0)),
            Triangle(Vector3D(0.5, -0.5, 0.5), Vector3D(-0.5, 0.5, 0.5), Vector3D(-0.5, -0.5, 0.5), Vector2D(0,1), Vector2D(1,0), Vector2D(1,1)),

            # WEST
            Triangle(Vector3D(-0.5, -0.5, 0.5), Vector3D(-0.5, 0.5, 0.5), Vector3D(-0.5, 0.5, -0.5), Vector2D(0,1), Vector2D(0,0), Vector2D(1,0)),
            Triangle(Vector3D(-0.5, -0.5, 0.5), Vector3D(-0.5, 0.5, -0.5), Vector3D(-0.5, -0.5, -0.5), Vector2D(0,1), Vector2D(1,0), Vector2D(1,1)),

            # TOP
            Triangle(Vector3D(-0.5, 0.5, -0.5), Vector3D(-0.5, 0.5, 0.5), Vector3D(0.5, 0.5, 0.5), Vector2D(0,1), Vector2D(0,0), Vector2D(1,0)),
            Triangle(Vector3D(-0.5, 0.5, -0.5), Vector3D(0.5, 0.5, 0.5), Vector3D(0.5, 0.5, -0.5), Vector2D(0,1), Vector2D(1,0), Vector2D(1,1)),

            # BOTTOM
            Triangle(Vector3D(0.5, -0.5, 0.5), Vector3D(-0.5, -0.5, 0.5), Vector3D(-0.5, -0.5, -0.5), Vector2D(0,1), Vector2D(0,0), Vector2D(1,0)),
            Triangle(Vector3D(0.5, -0.5, 0.5), Vector3D(-0.5, -0.5, -0.5), Vector3D(0.5, -0.5, -0.5), Vector2D(0,1), Vector2D(1,0), Vector2D(1,1))

        ]