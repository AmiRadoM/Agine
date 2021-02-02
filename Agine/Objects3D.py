import copy
import math
assetsPath = "./assets/"

def Vector3ListsToVector2List(list):
    return [[list[0][0],list[0][1]],[list[1][0],list[1][1]],[list[2][0],list[2][1]]]

def MultiplyMatrixVector(j ,o ,m  ):
    o[0] = j[0] * m.m[0][0] + j[1] * m.m[1][0] + j[2] * m.m[2][0] + m.m[3][0]
    o[1] = j[0] * m.m[0][1] + j[1] * m.m[1][1] + j[2] * m.m[2][1] + m.m[3][1]
    o[2] = j[0] * m.m[0][2] + j[1] * m.m[1][2] + j[2] * m.m[2][2] + m.m[3][2]
    w = j[0] * m.m[0][3] + j[1] * m.m[1][3] + j[2] * m.m[2][3] + m.m[3][3]

    if(w != 0):
        o[0] /= w
        o[1] /= w
        #o[2] /= w
    return o

def MatrixMultiplyVector3D(m,j):
    v = [0,0,0,0]
    v[0] = j[0] * m.m[0][0] + j[1] * m.m[1][0] + j[2] * m.m[2][0] + j[3] * m.m[3][0]
    v[1] = j[0] * m.m[0][1] + j[1] * m.m[1][1] + j[2] * m.m[2][1] + j[3] * m.m[3][1]
    v[2] = j[0] * m.m[0][2] + j[1] * m.m[1][2] + j[2] * m.m[2][2] + j[3] * m.m[3][2]
    v[3] = j[0] * m.m[0][3] + j[1] * m.m[1][3] + j[2] * m.m[2][3] + j[3] * m.m[3][3]
    return v

def MatrixMakeIdentity():
    matrix = Matrix4x4()
    matrix.m[0][0] = 1
    matrix.m[1][1] = 1
    matrix.m[2][2] = 1
    matrix.m[3][3] = 1
    return matrix

def MatrixMakeRotationZ(angle):
    matrix = Matrix4x4()
    matrix.m[0][0] = math.cos(angle)
    matrix.m[0][1] = math.sin(angle)
    matrix.m[1][0] = -math.sin(angle)
    matrix.m[1][1] = math.cos(angle)
    matrix.m[2][2] = 1
    matrix.m[3][3] = 1
    return matrix

def MatrixMakeRotationX(angle):
    matrix = Matrix4x4()
    matrix.m[0][0] = 1
    matrix.m[1][1] = math.cos(angle)
    matrix.m[1][2] = math.sin(angle)
    matrix.m[2][1] = -math.sin(angle)
    matrix.m[2][2] = math.cos(angle)
    matrix.m[3][3] = 1
    return matrix

def MatrixMakeRotationY(angle):
    matrix = Matrix4x4()
    matrix.m[0][0] = math.cos(angle)
    matrix.m[0][2] = math.sin(angle)
    matrix.m[2][0] = -math.sin(angle)
    matrix.m[1][1] = 1
    matrix.m[2][2] = math.cos(angle)
    matrix.m[3][3] = 1
    return matrix

def MatrixMakeTranslation(x,y,z):
    matrix = Matrix4x4()
    matrix.m[0][0] = 1
    matrix.m[1][1] = 1
    matrix.m[2][2] = 1
    matrix.m[3][3] = 1
    matrix.m[3][0] = x
    matrix.m[3][1] = y
    matrix.m[3][2] = z
    return matrix

def MatrixMakeProjection(FOVDegrees, AspectRatio, Near, Far):
    FOVRad = 1 / math.tan(FOVDegrees * 0.5 / 180 * math.pi)
    matrix = Matrix4x4()
    matrix.m[0][0] = AspectRatio * FOVRad
    matrix.m[1][1] = FOVRad
    matrix.m[2][2] = Far / (Far - Near)
    matrix.m[3][2] = (-Far * Near) / (Far - Near)
    matrix.m[2][3] = 1
    matrix.m[3][3] = 0
    return matrix

def MatrixMultiplyMatrix(m1,m2):
    matrix = Matrix4x4()
    for i in range(4):
        for j in range(4):
            matrix.m[j][i] = m1.m[j][0] * m1.m[0][i] + m1.m[j][1] * m1.m[1][i] + m1.m[j][2] * m1.m[2][i] + m1.m[j][3] * m1.m[3][i]
    return matrix

def MatrixPointAt(pos, target, up):
    #Claculate new Forward Vector
    newForward = Vector3DSub(target, pos)
    newForward = Vector3DNormalise(newForward)

    #new Up
    a = Vector3DMult(newForward, Vector3DDotProduct(up, newForward))
    newUp = Vector3DSub(up,a)
    newUp = Vector3DNormalise(newUp)

    #new Right Direction
    newRight = Vector3DCrossProduct(newUp,newForward)

    #creating matrix
    matrix = Matrix4x4()
    matrix.m[0][0] = newRight[0]
    matrix.m[0][1] = newRight[1]
    matrix.m[0][2] = newRight[2]
    matrix.m[0][3] = 0
    matrix.m[1][0] = newUp[0]
    matrix.m[1][1] = newUp[1]
    matrix.m[1][2] = newUp[2]
    matrix.m[1][3] = 0
    matrix.m[2][0] = newForward[0]
    matrix.m[2][1] = newForward[1]
    matrix.m[2][2] = newForward[2]
    matrix.m[2][3] = 0
    matrix.m[3][0] = pos[0]
    matrix.m[3][1] = pos[1]
    matrix.m[3][2] = pos[2]
    matrix.m[3][3] = 1

    return matrix

def MatrixQuickInverseForLookAt(m):
    matrix = Matrix4x4()
    matrix.m[0][0] = m.m[0][0]
    matrix.m[1][0] = m.m[0][1]
    matrix.m[2][0] = m.m[0][2]
    matrix.m[0][1] = m.m[1][0]
    matrix.m[1][1] = m.m[1][1]
    matrix.m[2][1] = m.m[1][2]
    matrix.m[0][2] = m.m[2][0]
    matrix.m[1][2] = m.m[2][1]
    matrix.m[2][2] = m.m[2][2]
    matrix.m[3][0] = -(m.m[3][0] * matrix.m[0][0] + m.m[3][1] * matrix.m[1][0] + m.m[3][2] * matrix.m[2][0])
    matrix.m[3][1] = -(m.m[3][0] * matrix.m[0][1] + m.m[3][1] * matrix.m[1][1] + m.m[3][2] * matrix.m[2][1])
    matrix.m[3][2] = -(m.m[3][0] * matrix.m[0][2] + m.m[3][1] * matrix.m[1][2] + m.m[3][2] * matrix.m[2][2])
    matrix.m[3][3] = 1
    return matrix



def Vector3DAdd(a,b):
    return [a[0]+b[0],a[1]+b[1],a[2]+b[2]]
def Vector3DSub(a,b):
    return [a[0]-b[0],a[1]-b[1],a[2]-b[2]]
def Vector3DMult(a,b):
    return [a[0]*b,a[1]*b,a[2]*b]
def Vector3DDiv(a,b):
    return [a[0]/b,a[1]/b,a[2]/b]
def Vector3DMultVector3D(a,b):
    return [a[0]*b[0],a[1]*b[1],a[2]*b[2]]
def Vector3DDotProduct(a,b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def Vector3DLength(a):
    return math.sqrt(Vector3DDotProduct(a,a))
def Vector3DNormalise(a):
    l = Vector3DLength(a)
    return [a[0]/l, a[1]/l,a[2]/l]
def Vector3DCrossProduct(a,b):
    v = [0,0,0]
    v[0] = a[1] * b[2] - a[2] * b[1]
    v[1] = a[2] * b[0] - a[0] * b[2]
    v[2] = a[0] * b[1] - a[1] * b[0]
    return v
def Vector3DIntersectPlane(planeP, planeN, lineStart, lineEnd):
    planeN = Vector3DNormalise(planeN)
    planeD = -Vector3DDotProduct(planeN, planeP)
    ad = Vector3DDotProduct(lineStart,planeN)
    bd = Vector3DDotProduct(lineEnd,planeN)
    t = (-planeD - ad) / (bd - ad)
    lineStartToEnd = Vector3DSub(lineEnd, lineStart)
    lineToIntersect = Vector3DMult(lineStartToEnd, t)
    return Vector3DAdd(lineStart, lineToIntersect)


def TriangleClipAgainstPlane(planeP, planeN, inTri):
    planeN = Vector3DNormalise(planeN)
    
    def distance(p):
        n = Vector3DNormalise(p)
        return (planeN[0] * p[0] + planeN[1] * p[1] + planeN[2] * p[2] - Vector3DDotProduct(planeN,planeP))

    insidePoints = [[0,0,0],[0,0,0],[0,0,0]]
    insidePointCount = 0
    outsidePoints = [[0,0,0],[0,0,0],[0,0,0]]
    outsidePointCount = 0

    d0 = distance(inTri.p[0])
    d1 = distance(inTri.p[1])
    d2 = distance(inTri.p[2])

    if(d0 >= 0):
        insidePoints[insidePointCount] = inTri.p[0]
        insidePointCount+=1

    else:
        outsidePoints[outsidePointCount] = inTri.p[0]
        outsidePointCount+=1

    if (d1 >= 0):
        insidePoints[insidePointCount] = inTri.p[1]
        insidePointCount += 1
    else:
        outsidePoints[outsidePointCount] = inTri.p[1]
        outsidePointCount += 1
    if (d2 >= 0):
        insidePoints[insidePointCount] = inTri.p[2]
        insidePointCount += 1
    else:
        outsidePoints[outsidePointCount] = inTri.p[2]
        outsidePointCount += 1

    if(insidePointCount == 0):
        return []
    elif(insidePointCount == 3):
        a = Triangle3D()

        a.color = inTri.color

        a.p[0] = inTri.p[0]
        a.p[1] = inTri.p[1]
        a.p[2] = inTri.p[2]

        return [a]
    elif(insidePointCount == 1 and outsidePointCount == 2):
        a = Triangle3D(color = (100,0,0))

        a.color = inTri.color

        a.p[0] = insidePoints[0]
        a.p[1] = Vector3DIntersectPlane(planeP,planeN,insidePoints[0],outsidePoints[0])
        a.p[2] = Vector3DIntersectPlane(planeP,planeN,insidePoints[0],outsidePoints[1])

        del inTri
        return [a]
    elif(insidePointCount==2 and outsidePointCount == 1):

        a = copy.deepcopy(Triangle3D(color = (0,0,100)))

        a.color = inTri.color


        a.p[0] = copy.deepcopy(insidePoints[0])
        a.p[1] = copy.deepcopy(insidePoints[1])
        a.p[2] = copy.deepcopy(Vector3DIntersectPlane(planeP, planeN, insidePoints[0], outsidePoints[0]))



        b = copy.deepcopy(Triangle3D(color = (0,100,0)))
        b.color = inTri.color

        b.p[0] = insidePoints[1]
        b.p[1] = a.p[2]
        b.p[2] = Vector3DIntersectPlane(planeP, planeN, insidePoints[1], outsidePoints[0])




        return [a,b]








def GetColorShading(lum):
    bgColor = []
    
    pixelBW = (int)(13*lum)
    if(pixelBW == 0):
        bgColor = (0,0,0)
    elif(pixelBW ==1):
        bgColor = (21,21,21)
    elif (pixelBW == 2):
        bgColor = (42, 42, 42)
    elif (pixelBW == 3):
        bgColor = (64, 64, 64)
    elif (pixelBW == 4):
        bgColor = (85, 85, 85)
    elif (pixelBW == 5):
        bgColor = (106, 106, 106)
    elif (pixelBW == 6):
        bgColor = (127, 127, 127)
    elif (pixelBW == 7):
        bgColor = (149, 149, 149)
    elif (pixelBW == 8):
        bgColor = (170, 170, 170)
    elif (pixelBW == 9):
        bgColor = (191, 191, 191)
    elif (pixelBW == 10):
        bgColor = (212, 212, 212)
    elif (pixelBW == 11):
        bgColor = (234, 234, 234)
    elif (pixelBW == 12):
        bgColor = (255, 255, 255)
    else:
        bgColor = (0,0,0)

    
    return bgColor




class Triangle3D():
    def __init__(self, points= [[0,0,0],[0,0,0],[0,0,0]], color = (255,255,255)):
        self.p = points
        self.color = color


class Mesh3D():
    def __init__(self):
        self.Triangles = []

    def LoadFromObjectFile(self, FileName):
        try:
            verts = []
            with open(assetsPath + FileName, 'r') as f:
                for line in f:
                    if(line.split(' ')[0] == 'v'):
                        v = line.split(' ')
                        v.pop(0)
                        v = [float(e) for e in v]
                        verts.append(v)
                    if(line.split(' ')[0] == 'f'):
                        fs = line.split(' ')
                        fs.pop(0)
                        fs = [e.split('/')[0] for e in fs]
                        fs = [int(e) for e in fs]
                        self.Triangles.append(Triangle3D(points=[verts[fs[0]-1],verts[fs[1]-1],verts[fs[2]-1]]))

            return True
        except:
            return False

class Matrix4x4():
    def __init__(self):
        self.m = [[0,0,0,0],
             [0,0,0,0],
             [0,0,0,0],
             [0,0,0,0]]

class Cube3D():
    def __init__(self, name = "", position = [0,0,0], rotation = [0,0,0], scale = [1,1,1],color = (0,0,0), layer = 0):
        self.mesh = Mesh3D()

        self.mesh.Triangles = [
            #South
            Triangle3D([[-1,-1,-1],[-1,1,-1],[1,1,-1]]),
            Triangle3D([[-1,-1,-1],[1,1,-1],[1,-1,-1]]),
            #East
            Triangle3D([[1,-1,-1],[1,1,-1],[1,1,1]]),
            Triangle3D([[1,-1,-1],[1,1,1],[1,-1,1]]),
            #North
            Triangle3D([[1,-1,1],[1,1,1],[-1,1,1]]),
            Triangle3D([[1,-1,1],[-1,1,1],[-1,-1,1]]),
            #West
            Triangle3D([[-1,-1,1],[-1,1,1],[-1,1,-1]]),
            Triangle3D([[-1,-1,1],[-1,1,-1],[-1,-1,-1]]),
            #Top
            Triangle3D([[-1,1,-1],[-1,1,1],[1,1,1]]),
            Triangle3D([[-1,1,-1],[1,1,1],[1,1,-1]]),
            #Bottom
            Triangle3D([[1,-1,1],[-1,-1,1],[-1,-1,-1]]),
            Triangle3D([[1,-1,1],[-1,-1,-1],[1,-1,-1]])
        ]

        self.name = name
        self.color = color
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]
        self.rotationx = rotation[0]
        self.rotationy = rotation[1]
        self.rotationz = rotation[2]
        self.scalex = scale[0]
        self.scaley = scale[1]
        self.scalez = scale[2]
        self.layer = layer

        

        objects3D.append(self)

    def Move(self, x=0,y=0,z=0):
        self.x += x
        self.y += y
        self.z += z


class Sphere3D():
    def __init__(self, name = "", position=[0, 0, 0], rotation=[0, 0, 0], scale=[1, 1, 1], color=(0, 0, 0),
                 layer=0):
        self.mesh = Mesh3D()

        print(self.mesh.LoadFromObjectFile("Sphere.obj"))

        self.name = name
        self.color = color
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]
        self.rotationx = rotation[0]
        self.rotationy = rotation[1]
        self.rotationz = rotation[2]
        self.scalex = scale[0]
        self.scaley = scale[1]
        self.scalez = scale[2]
        self.layer = layer

        objects3D.append(self)

    def Move(self, x=0, y=0, z=0):
        self.x += x
        self.y += y
        self.z += z


class Object3D():
    def __init__(self,  fileDirectory,name = "",position=[0, 0, 0], rotation=[0, 0, 0], scale=[1, 1, 1], color=(0, 0, 0), layer=0):
        self.mesh = Mesh3D()

        self.mesh.LoadFromObjectFile(fileDirectory)

        self.name = name
        self.color = color
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]
        self.rotationx = rotation[0]
        self.rotationy = rotation[1]
        self.rotationz = rotation[2]
        self.scalex = scale[0]
        self.scaley = scale[1]
        self.scalez = scale[2]
        self.layer = layer

        objects3D.append(self)
    
    def Move(self, x=0,y=0,z=0):
        self.x += x
        self.y += y
        self.z += z 











objects3D = []