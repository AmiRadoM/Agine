import time
import math
import copy
import sys
import os
import pygame
from pygame.locals import *
import pygame.gfxdraw
from .Variables import *
import Agine.Variables as Variables
from .Objects2D import *
from .Objects3D import *
from .Physics2D import *
from .Collision2D import *
from .Input import *
from .Attributes import *
from .ObjectsUI import *




class __Window():
    def __init__(self, title = "Agine Game", backgroundColor = [255, 255, 255], scale = Vector3D(1000,1000,0)):
        self.scale = scale
        self.originalScale = scale
        self.bgColor = backgroundColor
        self.display = pygame.display.set_mode((self.originalScale.x,self.originalScale.y),DOUBLEBUF|HWSURFACE|RESIZABLE)
        pygame.display.set_caption(title)

    def SetScale(self, scale):
        self.scale = scale
        self.display = pygame.display.set_mode((self.scale.x, self.scale.y),DOUBLEBUF | HWSURFACE | RESIZABLE)

    def SetSettings(self, resizable = None):
        if (resizable == True):
            self.display = pygame.display.set_mode((self.scale.x, self.scale.y), DOUBLEBUF | HWSURFACE | RESIZABLE)
        elif (resizable == False):
            self.display = pygame.display.set_mode((self.scale.x, self.scale.y), DOUBLEBUF | HWSURFACE)



class GameObject():
    def __init__(self, name = "GameObject", layer = 0, isVisible = True):
        self.name = name
        self.layer = layer
        self.isVisible = isVisible
        self.Transform = Transform()
        objects.append(self)

    def addAttr(self, attr):
        """
        :param attr: The name of the attribute
        """
        try:
            if(not Attribute in eval( attr).__bases__):
                raise TypeError("Missing an Agine2D Attribute Name!")
            exec(f"self.{attr} = {attr}()")
            eval(f"self.{attr}").owner = self
            eval(attr.lower()).append(self)
        except:
            raise TypeError("Missing an Agine2D Attribute Name!")







def renderer():

    def render2D(sprite):
        if type(sprite) != Circle and type(sprite) != Polygon and type(sprite) != Line:
            newScale = (sprite.Transform.scale * gameDisplay.scale/2) / cam.Camera.scale
            newPos = cam.Camera.TranslateWorldVector2D(Vector2D(sprite.Transform.position.x - sprite.Transform.scale.x / 2,sprite.Transform.position.y + sprite.Transform.scale.y / 2))

        if (hasattr(sprite, "Line")):
            startVector = cam.Camera.TranslateWorldVector2D(sprite.Line.startPoint)
            endVector = cam.Camera.TranslateWorldVector2D(sprite.Line.endPoint)
            pygame.draw.line(gameDisplay.display, sprite.Line.color, [startVector.x, startVector.y],
                             [endVector.x, endVector.y], sprite.Line.width)

        if (hasattr(sprite, "Square")):
            pygame.draw.rect(gameDisplay.display, sprite.Square.color,
                             (newPos.x, newPos.y, newScale.x, newScale.y),
                             sprite.Square.width)



        if hasattr(sprite, "Sprite"):
            if(sprite.Sprite.imagePath != None):
                img = pygame.image.load(sprite.Sprite.imagePath)
                newImage = pygame.transform.scale(img, [int(a) for a in newScale.ToVector2D().ToList()])
                newImage = newImage.convert_alpha()

                colorImage = pygame.Surface(newImage.get_rect().size, pygame.SRCALPHA)
                colorImage.fill(sprite.Sprite.color)
                newImage.blit(colorImage, (0, 0), special_flags=BLEND_RGBA_MULT)

                gameDisplay.display.blit(newImage, (newPos.x, newPos.y))

        if hasattr(sprite, "Polygon"):
            allX = [point.x for point in sprite.Polygon.points]
            allY = [point.y for point in sprite.Polygon.points]
            allX = [x * sprite.Transform.scale.x for x in allX]
            allY = [y * sprite.Transform.scale.y for y in allY]
            avarageX = sum(allX) / len(allX)
            avarageY = sum(allY) / len(allY)

            deltaX = (sprite.x - avarageX)
            deltaY = (sprite.y - avarageY)

            translatedPoints = [Vector2D((allX[i] + deltaX) + gameDisplay.display.get_width() / 2 - cam.Transform.position.x, -(
                        (allY[i] + deltaY) - gameDisplay.display.get_height() / 2 - cam.Transform.position.y)) for i in
                                range(len(allX))]


            pygame.draw.polygon(gameDisplay.display, sprite.Polygon.color, translatedPoints, sprite.Polygon.width)

        if hasattr(sprite, "Circle"):
            cPos =  cam.Camera.TranslateWorldVector2D(sprite.Transform.position)
            pygame.draw.circle(gameDisplay.display, sprite.Circle.color, (cPos.x, cPos.y), sprite.Circle.radius, sprite.Circle.width)

    def render3D(object):
        if(hasattr(object, "Cube") or hasattr(object, "Mesh")):
            aspectRatio = gameDisplay.scale.x / gameDisplay.scale.y
            matrixProjection = Matrix4x4.MakeProjection(cam, aspectRatio)

            #Rotation Matrices
            matrixRotationZ = Matrix4x4.MakeRotationZ(object.Transform.rotation.z + math.radians(180))
            matrixRotationX = Matrix4x4.MakeRotationX(object.Transform.rotation.x)
            matrixRotationY = Matrix4x4.MakeRotationY(object.Transform.rotation.y)

            #Translation Matrix and World Matrix
            matrixTranslation = Matrix4x4.MakeTranslation(object.Transform.position.x,object.Transform.position.y,object.Transform.position.z)
            matrixWorld = matrixRotationZ * matrixRotationX * matrixRotationY
            matrixWorld = matrixWorld * matrixTranslation

            #Camera Matrix
            camTraget = Vector3D.Forward()
            matrixCamRotationY = Matrix4x4.MakeRotationY(cam.Transform.rotation.y)
            lookDirection = matrixCamRotationY * camTraget
            camTraget = cam.Transform.position + lookDirection
            matrixCam = Matrix4x4.MakePointAt(cam.Transform.position, camTraget, Vector3D.Up())
            matrixView = Matrix4x4.MakeQuickInverse(matrixCam)

            trianglesToRender = []

            for tri in object.Mesh.triangles if hasattr(object, "Mesh") else object.Cube.triangles:
                triTransformed = Triangle()
                triViewed = Triangle()

                triTransformed.points[0] = matrixWorld * tri.points[0]
                triTransformed.points[1] = matrixWorld * tri.points[1]
                triTransformed.points[2] = matrixWorld * tri.points[2]
                triTransformed.textureCords[0] = tri.textureCords[0]
                triTransformed.textureCords[1] = tri.textureCords[1]
                triTransformed.textureCords[2] = tri.textureCords[2]

                #Claculate The Normal
                line1 = triTransformed.points[1] - triTransformed.points[0]
                line2 = triTransformed.points[2] - triTransformed.points[0]
                
                normal = line1.CrossProduct(line2)
                normal = normal.Normalize()

                cameraRay = triTransformed.points[0] - Vector3D(cam.Transform.position.x,-cam.Transform.position.y,cam.Transform.position.z)

                if(normal.DotProduct(cameraRay) < 0):

                    #Illumination
                    lightDirection = Vector3D(0,-0.4,-1)
                    lightDirection = lightDirection.Normalize()

                    dotProduct = max(0.1, lightDirection.DotProduct(normal))

                    triTransformed.color = (max(min(255 * dotProduct,255),0), max(min(255 * dotProduct,255),0), max(min(255 * dotProduct,255),0))

                    #World Space to View Space
                    triViewed.points[0] = matrixView * triTransformed.points[0]
                    triViewed.points[1] = matrixView * triTransformed.points[1]
                    triViewed.points[2] = matrixView * triTransformed.points[2]
                    triViewed.color = triTransformed.color
                    triViewed.textureCords[0] = triTransformed.textureCords[0]
                    triViewed.textureCords[1] = triTransformed.textureCords[1]
                    triViewed.textureCords[2] = triTransformed.textureCords[2]

                    clipped = [None, None]
                    clipped[0],clipped[1] = triViewed.ClipAgainstPlane(Vector3D(0,0,0.1), Vector3D(0,0,1))
                    for clippedTri in clipped:
                        if(clippedTri != None):

                            triProjected = Triangle()

                            #Turn The Triangles Points To Be Projectable
                            triProjected.points[0] = matrixProjection * clippedTri.points[0];
                            triProjected.points[1] = matrixProjection * clippedTri.points[1];
                            triProjected.points[2] = matrixProjection * clippedTri.points[2];
                            triProjected.color = clippedTri.color
                            triProjected.textureCords[0] = copy.deepcopy(clippedTri.textureCords[0])
                            triProjected.textureCords[1] = copy.deepcopy(clippedTri.textureCords[1])
                            triProjected.textureCords[2] = copy.deepcopy(clippedTri.textureCords[2])

                            triProjected.textureCords[0].x = triProjected.textureCords[0].x / triProjected.points[0].w
                            triProjected.textureCords[1].x = triProjected.textureCords[1].x / triProjected.points[1].w
                            triProjected.textureCords[2].x = triProjected.textureCords[2].x / triProjected.points[2].w

                            triProjected.textureCords[0].y = triProjected.textureCords[0].y / triProjected.points[0].w
                            triProjected.textureCords[1].y = triProjected.textureCords[1].y / triProjected.points[1].w
                            triProjected.textureCords[2].y = triProjected.textureCords[2].y / triProjected.points[2].w

                            triProjected.textureCords[0].w = 1 / triProjected.points[0].w
                            triProjected.textureCords[1].w = 1 / triProjected.points[1].w
                            triProjected.textureCords[2].w = 1 / triProjected.points[2].w

                            triProjected.points[0] = triProjected.points[0] / triProjected.points[0].w
                            triProjected.points[1] = triProjected.points[1] / triProjected.points[1].w
                            triProjected.points[2] = triProjected.points[2] / triProjected.points[2].w


                            #Scale into View
                            offsetView = Vector3D(1,1)
                            triProjected.points[0] += offsetView
                            triProjected.points[1] += offsetView
                            triProjected.points[2] += offsetView

                            triProjected.points[0].x *= 0.5 * gameDisplay.scale.x
                            triProjected.points[0].y *= 0.5 * gameDisplay.scale.y
                            triProjected.points[1].x *= 0.5 * gameDisplay.scale.x
                            triProjected.points[1].y *= 0.5 * gameDisplay.scale.y
                            triProjected.points[2].x *= 0.5 * gameDisplay.scale.x
                            triProjected.points[2].y *= 0.5 * gameDisplay.scale.y


                            #Store Triangles To Sort Them
                            trianglesToRender.append(triProjected)
                    
            #Sort Triangles To Render
            trianglesToRender.sort(key=lambda t: (t.points[0].z + t.points[1].z + t.points[2].z)/3, reverse= True)

            for triToRender in trianglesToRender:
                listTriangles = []
                listTriangles.append(triToRender)
                numOfTris = 1

                for p in range(4):
                    while (numOfTris > 0):
                        test = listTriangles[len(listTriangles)-1]
                        listTriangles.pop(len(listTriangles)-1)
                        numOfTris -= 1


                        trisToAdd = [None,None]
                        if (p == 0):
                            trisToAdd[0], trisToAdd[1] = test.ClipAgainstPlane(Vector3D(0,0,0), Vector3D(0,1,0))
                        elif (p == 1):
                            trisToAdd[0], trisToAdd[1] = test.ClipAgainstPlane(Vector3D(0,gameDisplay.scale.y-1,0), Vector3D(0,-1,0))
                        elif (p == 2):
                            trisToAdd[0], trisToAdd[1] = test.ClipAgainstPlane(Vector3D(0,0,0), Vector3D(1,0,0))
                        elif (p == 3):
                            trisToAdd[0], trisToAdd[1] = test.ClipAgainstPlane(Vector3D(gameDisplay.scale.x-1,0,0), Vector3D(-1,0,0))

                        for t in trisToAdd:
                            if (t != None):
                                listTriangles.append(copy.deepcopy(t))

                    numOfTris = len(listTriangles)

                for newTri in listTriangles:
                    # Textured Rendering
                    TriangleTextured(newTri, object.Cube.texture if (hasattr(object,"Cube")) else object.Mesh.texture)
                    # Normal Rendering
                    # pygame.draw.polygon(gameDisplay.display, newTri.color, ((newTri.points[0].x, newTri.points[0].y),(newTri.points[1].x, newTri.points[1].y),(newTri.points[2].x, newTri.points[2].y)), 0)
                    # Wire Frame Rendering
                    pygame.draw.polygon(gameDisplay.display, (0,0,0), ((newTri.points[0].x, newTri.points[0].y), (newTri.points[1].x, newTri.points[1].y), (newTri.points[2].x, newTri.points[2].y)), 1)

    def TriangleTextured(tri, img):
        pixelArray = pygame.PixelArray(gameDisplay.display)
        x1 = int(tri.points[0].x)
        y1 = int(tri.points[0].y)
        u1 = tri.textureCords[0].x
        v1 = tri.textureCords[0].y
        w1 = tri.textureCords[0].w

        x2 = int(tri.points[1].x)
        y2 = int(tri.points[1].y)
        u2 = tri.textureCords[1].x
        v2 = tri.textureCords[1].y
        w2 = tri.textureCords[1].w

        x3 = int(tri.points[2].x)
        y3 = int(tri.points[2].y)
        u3 = tri.textureCords[2].x
        v3 = tri.textureCords[2].y
        w3 = tri.textureCords[2].w

        if (y2 < y1):
            x1, x2 = x2, x1
            y1, y2 = y2, y1
            u1, u2 = u2, u1
            v1, v2 = v2, v1
            w1, w2 = w2, w1

        if (y3 < y1):
            x1, x3 = x3, x1
            y1, y3 = y3, y1
            u1, u3 = u3, u1
            v1, v3 = v3, v1
            w1, w3 = w3, w1

        if (y3 < y2):
            x3, x2 = x2, x3
            y3, y2 = y2, y3
            u3, u2 = u2, u3
            v3, v2 = v2, v3
            w3, w2 = w2, w3

        dya = y2 - y1
        dxa = x2 - x1
        dua = u2 - u1
        dva = v2 - v1
        dwa = w2 - w1

        dyb = y3 - y1
        dxb = x3 - x1
        dub = u3 - u1
        dvb = v3 - v1
        dwb = w3 - w1

        mxa = dxa / abs(dya) if dya != 0 else 0
        mxb = dxb / abs(dyb) if dyb != 0 else 0
        mua = dua / abs(dya) if dya != 0 else 0
        mub = dub / abs(dyb) if dyb != 0 else 0
        mva = dva / abs(dya) if dya != 0 else 0
        mvb = dvb / abs(dyb) if dyb != 0 else 0
        mwa = dwa / abs(dya) if dya != 0 else 0
        mwb = dwb / abs(dyb) if dyb != 0 else 0

        if (dya!= 0):
            for i in range(y1,y2+1):
                firstX = int(x1 + mxa*(i - y1))
                lastX = int(x1 + mxb*(i - y1))
                firstU = u1 + mua * (i - y1)
                firstV = v1 + mva * (i - y1)
                firstW = w1 + mwa * (i - y1)

                lastU = u1 + mub * (i - y1)
                lastV = v1 + mvb * (i - y1)
                lastW = w1 + mwb * (i - y1)

                if(firstX > lastX):
                    firstX, lastX = lastX, firstX
                    firstU, lastU = lastU, firstU
                    firstV, lastV = lastV, firstV
                    firstW, lastW = lastW, firstW

                tStep = 1 / (lastX - firstX) if (lastX - firstX) != 0 else 0
                t = 0

                for j in range(firstX, lastX+1):
                    texU = (1 - t) * firstU + t * lastU
                    texV = (1 - t) * firstV + t * lastV
                    texW = (1 - t) * firstW + t * lastW
                    color = img.get_at((int((1-texU/texW) * (img.get_size()[0]-0.00001)), int(texV/texW * (img.get_size()[1]-0.00001))))
                    #gameDisplay.display.set_at((j, i), (color[0] * (tri.color[0] / 255) , color[1] * (tri.color[1] / 255), color[2] * (tri.color[2] / 255 )))
                    pixelArray[j,i] = (color[0] * (tri.color[0] / 255) , color[1] * (tri.color[1] / 255), color[2] * (tri.color[2] / 255 ))
                    t+= tStep

        dyc = y3 - y2
        dxc = x3 - x2
        duc = u3 - u2
        dvc = v3 - v2
        dwc = w3 - w2
        mxc = dxc / abs(dyc) if dyc != 0 else 0
        muc = duc / abs(dyc) if dyc != 0 else 0
        mvc = dvc / abs(dyc) if dyc != 0 else 0
        mwc = dwc / abs(dyc) if dyc != 0 else 0

        if (dyb != 0):
            for i in range(y2, y3+1):
                firstX = int(x2 + mxc * (i - y2))
                lastX = int(x1 + mxb * (i - y1))

                firstU = u2 + muc * (i - y2)
                firstV = v2 + mvc * (i - y2)
                firstW = w2 + mwc * (i - y2)

                lastU = u1 + mub * (i - y1)
                lastV = v1 + mvb * (i - y1)
                lastW = w1 + mwb * (i - y1)

                if (firstX > lastX):
                    firstX, lastX = lastX, firstX
                    firstU, lastU = lastU, firstU
                    firstV, lastV = lastV, firstV
                    firstW, lastW = lastW, firstW

                tStep = 1 / (lastX - firstX) if (lastX - firstX) != 0 else 0
                t = 0

                for j in range(firstX, lastX + 1):
                    texU = (1 - t) * firstU + t * lastU
                    texV = (1 - t) * firstV + t * lastV
                    texW = (1 - t) * firstW + t * lastW
                    color = img.get_at((int((1 - texU / texW) * (img.get_size()[0] - 0.00001)),int(texV / texW * (img.get_size()[1] - 0.00001))))
                    #gameDisplay.display.set_at((j, i), (color[0] * (tri.color[0] / 255), color[1] * (tri.color[1] / 255),color[2] * (tri.color[2] / 255)))
                    pixelArray[j, i] = (color[0] * (tri.color[0] / 255), color[1] * (tri.color[1] / 255), color[2] * (tri.color[2] / 255))
                    t+= tStep

        pixelArray.close()

    def renderUI(object):
        if (hasattr(object, "Text")):
            font = pygame.font.SysFont(None, object.Text.fontSize)
            text = font.render(object.Text.text, True,object.Text.color)

            newPosUI = Vector2D(object.Transform.position.x * (gameDisplay.scale.x/2 / cam.Camera.scale) - text.get_rect().width / 2 + gameDisplay.scale.x / 2, object.Transform.position.y * (gameDisplay.scale.y/2 / cam.Camera.scale) + text.get_rect().height / 2  - gameDisplay.scale.y / 2)
            newPosUI.y = -newPosUI.y


            gameDisplay.display.blit(text, newPosUI.ToList())
        if (hasattr(object, "Button")):
            newMousePos = cam.Camera.ScreenToWorldVector2D(mousePos)

            if object.Transform.position.x - object.Transform.scale.x / 2 < newMousePos.x < object.Transform.position.x + object.Transform.scale.x / 2 and object.Transform.position.y - object.Transform.scale.y / 2 < newMousePos.y < object.Transform.position.y + object.Transform.scale.y / 2:
                if MouseDown["button0"]:
                    for func in object.Button.onClick:
                        try:
                            func(object)
                        except TypeError:
                            func()








    # Bubble Sort Sprite Layers
    n = len(objects)
    for i in range(n - 1):

        for j in range(0, n - i - 1):

            if objects[j].layer > objects[j + 1].layer:
                objects[j], objects[j + 1] = objects[j + 1], objects[j]


    for cam in camera:
        #cam.Transform.position = (cam.Transform.position * gameDisplay.scale/2) / cam.Camera.scale
        for object in objects:
            if object.isVisible:
                #Outline
                if (hasattr(object, "Outline")):
                    if (hasattr(object, "Sprite")):
                        newPos = cam.Camera.TranslateWorldVector2D(
                            Vector2D(object.Transform.position.x - object.Transform.scale.x / 2,
                                     object.Transform.position.y + object.Transform.scale.y / 2))

                        newImage = pygame.transform.scale(object.Sprite.image, object.Transform.scale.ToList())

                        outline = pygame.mask.from_surface(newImage)
                        outlineSurface = outline.to_surface()
                        outlineSurface.set_colorkey([0,0,0])

                        newSurface = pygame.Surface(outlineSurface.get_size()).convert_alpha()
                        newSurface.fill([0,0,0,0])
                        newSurface.blit(outlineSurface, (0,0))

                        colorImage = pygame.Surface(newSurface.get_rect().size, pygame.SRCALPHA)
                        colorImage.fill(object.Outline.color)
                        newSurface.blit(colorImage, (0, 0), special_flags=BLEND_RGBA_MULT)
                        newSurface.blit(outlineSurface, (0, 0), special_flags=BLEND_RGBA_MULT)

                        gameDisplay.display.blit(newSurface, (newPos.x - object.Outline.width.x, newPos.y))
                        gameDisplay.display.blit(newSurface, (newPos.x + object.Outline.width.x, newPos.y))
                        gameDisplay.display.blit(newSurface, (newPos.x, newPos.y - object.Outline.width.y))
                        gameDisplay.display.blit(newSurface, (newPos.x, newPos.y + object.Outline.width.y))
                    else:
                        outline = copy.deepcopy(object)
                        outline.color = object.Outline.color

                        outline.Transform.position.x += object.Outline.width.x
                        render2D(outline)
                        outline.Transform.position.x -= 2 * object.Outline.width.x
                        render2D(outline)
                        outline.Transform.position.x += object.Outline.width.x
                        outline.Transform.position.y += object.Outline.width.y
                        render2D(outline)
                        outline.Transform.position.y -= 2 * object.Outline.width.y
                        render2D(outline)



                # 2D !!!
                render2D(object)

                # 3D !!!
                render3D(object)

                # UI !!!
                renderUI(object)










def checkClose():
    for event in pygame.event.get(pygame.QUIT):
        if event.type == pygame.QUIT:
            crashed["crashed"] = True


def checkScreenResize():
    minimumScale = Vector2D(500,500)
    for event in pygame.event.get(pygame.VIDEORESIZE):
        if (event.type == pygame.VIDEORESIZE):
            if (gameDisplay.scale.x != event.w and gameDisplay.scale.y == event.h):
                proportion = gameDisplay.scale.x / gameDisplay.scale.y
                gameDisplay.scale.x = event.w
                if (gameDisplay.scale.x < minimumScale.x):
                    gameDisplay.scale.x = minimumScale.x
                gameDisplay.scale.y = (1/proportion) * gameDisplay.scale.x
            elif (gameDisplay.scale.x == event.w and gameDisplay.scale.y != event.h):
                proportion = gameDisplay.scale.x/gameDisplay.scale.y
                gameDisplay.scale.y = event.h
                if (gameDisplay.scale.y < minimumScale.y):
                    gameDisplay.scale.y = minimumScale.y
                gameDisplay.scale.x = proportion * gameDisplay.scale.y
            else:
                maxDimension = max(event.w, event.h)
                if(maxDimension == event.w):
                    proportion = gameDisplay.scale.x / gameDisplay.scale.y
                    gameDisplay.scale.x = event.w
                    gameDisplay.scale.y = (1 / proportion) * gameDisplay.scale.x
                else:
                    proportion = gameDisplay.scale.x / gameDisplay.scale.y
                    gameDisplay.scale.y = event.h
                    gameDisplay.scale.x = proportion * gameDisplay.scale.y

            gameDisplay.display = pygame.display.set_mode((int(gameDisplay.scale.x), int(gameDisplay.scale.y)), DOUBLEBUF|HWSURFACE|RESIZABLE)
            depthBuffer = [0] * int(gameDisplay.scale.x * gameDisplay.scale.y + gameDisplay.scale.x)



def Main():
    global gameDisplay

    # Setup
    try:
        gameDisplay
    except NameError:
        gameDisplay = __Window()

    pygame.init()

    lastTime = time.time()

    while not crashed.get("crashed"):
        nowTime = time.time()
        Variables.deltaTime = nowTime - lastTime + 0.00000000001
        lastTime = nowTime
        checkClose()
        checkScreenResize()
        gameDisplay.display.fill(gameDisplay.bgColor)
        physics2D()
        inputSystem()
        for update in updateFunctions:
            update()
        renderer()
        pygame.display.flip()
        clock.tick(Variables.fps)


    pygame.quit()


gameDisplay = __Window()
updateFunctions = []
objects = []
depthBuffer = [0] * (gameDisplay.scale.x * gameDisplay.scale.y + gameDisplay.scale.x)

gameDisplay.scale = copy.copy(gameDisplay.originalScale)






