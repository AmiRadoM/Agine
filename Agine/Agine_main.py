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
from .Physics2D import *
from .Collision2D import *
from .Objects3D import *
from .Input import *
from .Attributes import *
from .ObjectsUI import *





class Window():
    def __init__(self, title = "Agine Game", backgroundColor = [255, 255, 255], scale = Vector2D(1000,1000)):
        self.scale = scale
        self.originalScale = scale
        self.bgColor = backgroundColor
        self.display = pygame.display.set_mode((self.originalScale.x,self.originalScale.y),DOUBLEBUF|HWSURFACE|RESIZABLE)
        pygame.display.set_caption(title)

    def ProportionedScale(self, scale):
        return self.scale * (scale / self.originalScale)



class GameObject():
    def __init__(self, name = "GameObject", layer = 0, isVisible = True):
        self.name = name
        self.layer = layer
        self.isVisible = isVisible
        self.Transform2D = Transform2D()
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

    def __del__(self):
        objects.remove(self)






def renderer():
    trianglesToRaster = []

    # 2D!!!!
    def render2D(sprite):

        if type(sprite) != Circle and type(sprite) != Polygon and type(sprite) != Line:
            newScale = (sprite.Transform2D.scale * gameDisplay.scale/2) / cam.Camera.scale
            newPos = cam.Camera.ScreenToWorldVector2D(Vector2D(sprite.Transform2D.position.x - sprite.Transform2D.scale.x / 2,sprite.Transform2D.position.y + sprite.Transform2D.scale.y / 2))

        if (hasattr(sprite, "Line")):
            startVector = cam.Camera.ScreenToWorldVector2D(sprite.Line.startPoint)
            endVector = cam.Camera.ScreenToWorldVector2D(sprite.Line.endPoint)
            pygame.draw.line(gameDisplay.display, sprite.Line.color, [startVector.x, startVector.y],
                             [endVector.x, endVector.y], sprite.Line.width)

        if (hasattr(sprite, "Square")):
            pygame.draw.rect(gameDisplay.display, sprite.Square.color,
                             (newPos.x, newPos.y, newScale.x, newScale.y),
                             sprite.Square.width)


        if hasattr(sprite, "Sprite"):
            if(sprite.Sprite.imagePath != None):
                img = pygame.image.load(os.path.join(assetsPath,sprite.Sprite.imagePath))
                newImage = pygame.transform.scale(img, [int(a) for a in newScale.ToList()])
                newImage = newImage.convert_alpha()

                colorImage = pygame.Surface(newImage.get_rect().size, pygame.SRCALPHA)
                colorImage.fill(sprite.Sprite.color)
                newImage.blit(colorImage, (0, 0), special_flags=BLEND_RGBA_MULT)

                gameDisplay.display.blit(newImage, (newPos.x, newPos.y))

        if hasattr(sprite, "Polygon"):
            allX = [point.x for point in sprite.Polygon.points]
            allY = [point.y for point in sprite.Polygon.points]
            allX = [x * sprite.Transform2D.scale.x for x in allX]
            allY = [y * sprite.Transform2D.scale.y for y in allY]
            avarageX = sum(allX) / len(allX)
            avarageY = sum(allY) / len(allY)

            deltaX = (sprite.x - avarageX)
            deltaY = (sprite.y - avarageY)

            translatedPoints = [Vector2D((allX[i] + deltaX) + gameDisplay.display.get_width() / 2 - cam.Transform2D.position.x, -(
                        (allY[i] + deltaY) - gameDisplay.display.get_height() / 2 - cam.Transform2D.position.y)) for i in
                                range(len(allX))]


            pygame.draw.polygon(gameDisplay.display, sprite.Polygon.color, translatedPoints, sprite.Polygon.width)

        if hasattr(sprite, "Circle"):
            cPos =  cam.Camera.ScreenToWorldVector2D(sprite.Transform2D.position)
            pygame.draw.circle(gameDisplay.display, sprite.Circle.color, (cPos.x, cPos.y), sprite.Circle.radius, sprite.Circle.width)



    # def render3D(sprite):
    #
    #     # Projection Matrix
    #     mProj = MatrixMakeProjection(90, gameDisplay.height / gameDisplay.width, 0, 1000)
    #     # Rotation Matrices
    #     mZ = MatrixMakeRotationZ(sprite.rotationz)
    #     mX = MatrixMakeRotationX(math.radians(sprite.rotationx + 180))
    #     mY = MatrixMakeRotationY(sprite.rotationy)
    #     # Translation Matrix
    #     mTrans = MatrixMakeTranslation(0, 0, 0)
    #     # World Matrix
    #     mWorld = MatrixMakeIdentity()
    #     mWorld = MatrixMultiplyMatrix(mZ, mX)
    #     mWorld = MatrixMultiplyMatrix(mWorld, mTrans)
    #     # Camera Matrix
    #     Up = [0, 1, 0]
    #     Target = Vector3DAdd(cameraPos, lookDir)
    #     mCamera = MatrixPointAt(cameraPos, Target, Up)
    #     mView = MatrixQuickInverseForLookAt(mCamera)
    #
    #     for triangle in sprite.mesh.Triangles:
    #         triProjected = Triangle3D()
    #         triTranslated = copy.deepcopy(triangle)
    #
    #         # Rotation
    #         # Z
    #
    #         triTranslated.p[0][0] = triangle.p[0][0] * mZ.m[0][0] + triangle.p[0][1] * mZ.m[1][0]
    #         triTranslated.p[1][0] = triangle.p[1][0] * mZ.m[0][0] + triangle.p[1][1] * mZ.m[1][0]
    #         triTranslated.p[2][0] = triangle.p[2][0] * mZ.m[0][0] + triangle.p[2][1] * mZ.m[1][0]
    #         triTranslated.p[0][1] = triangle.p[0][1] * mZ.m[1][1] + triangle.p[0][0] * mZ.m[0][1]
    #         triTranslated.p[1][1] = triangle.p[1][1] * mZ.m[1][1] + triangle.p[1][0] * mZ.m[0][1]
    #         triTranslated.p[2][1] = triangle.p[2][1] * mZ.m[1][1] + triangle.p[2][0] * mZ.m[0][1]
    #
    #         # X
    #         tempTriangle = copy.deepcopy(triTranslated)
    #
    #         triTranslated.p[0][1] = tempTriangle.p[0][1] * mX.m[1][1] + tempTriangle.p[0][2] * mX.m[2][1]
    #         triTranslated.p[1][1] = tempTriangle.p[1][1] * mX.m[1][1] + tempTriangle.p[1][2] * mX.m[2][1]
    #         triTranslated.p[2][1] = tempTriangle.p[2][1] * mX.m[1][1] + tempTriangle.p[2][2] * mX.m[2][1]
    #         triTranslated.p[0][2] = tempTriangle.p[0][2] * mX.m[2][2] + tempTriangle.p[0][1] * mX.m[1][2]
    #         triTranslated.p[1][2] = tempTriangle.p[1][2] * mX.m[2][2] + tempTriangle.p[1][1] * mX.m[1][2]
    #         triTranslated.p[2][2] = tempTriangle.p[2][2] * mX.m[2][2] + tempTriangle.p[2][1] * mX.m[1][2]
    #
    #         # Y
    #         tempTriangle = copy.deepcopy(triTranslated)
    #
    #         triTranslated.p[0][0] = tempTriangle.p[0][0] * mY.m[0][0] + tempTriangle.p[0][2] * mY.m[0][2]
    #         triTranslated.p[1][0] = tempTriangle.p[1][0] * mY.m[0][0] + tempTriangle.p[1][2] * mY.m[0][2]
    #         triTranslated.p[2][0] = tempTriangle.p[2][0] * mY.m[0][0] + tempTriangle.p[2][2] * mY.m[0][2]
    #         triTranslated.p[0][2] = tempTriangle.p[0][2] * mY.m[2][2] + tempTriangle.p[0][0] * mY.m[2][0]
    #         triTranslated.p[1][2] = tempTriangle.p[1][2] * mY.m[2][2] + tempTriangle.p[1][0] * mY.m[2][0]
    #         triTranslated.p[2][2] = tempTriangle.p[2][2] * mY.m[2][2] + tempTriangle.p[2][0] * mY.m[2][0]
    #
    #         # Scale
    #         triTranslated.p[0][0] *= sprite.scalex
    #         triTranslated.p[1][0] *= sprite.scalex
    #         triTranslated.p[2][0] *= sprite.scalex
    #         triTranslated.p[0][1] *= sprite.scaley
    #         triTranslated.p[1][1] *= sprite.scaley
    #         triTranslated.p[2][1] *= sprite.scaley
    #         triTranslated.p[0][2] *= sprite.scalez
    #         triTranslated.p[1][2] *= sprite.scalez
    #         triTranslated.p[2][2] *= sprite.scalez
    #
    #         # Position
    #         triTranslated.p[0][0] += sprite.x
    #         triTranslated.p[1][0] += sprite.x
    #         triTranslated.p[2][0] += sprite.x
    #         triTranslated.p[0][1] += sprite.y
    #         triTranslated.p[1][1] += sprite.y
    #         triTranslated.p[2][1] += sprite.y
    #         triTranslated.p[0][2] += sprite.z
    #         triTranslated.p[1][2] += sprite.z
    #         triTranslated.p[2][2] += sprite.z
    #
    #         # Getting Normal of Triangle
    #         normal = [0, 0, 0]
    #         line1 = [0, 0, 0]
    #         line2 = [0, 0, 0]
    #         line1 = Vector3DSub(triTranslated.p[1], triTranslated.p[0])
    #         line2 = Vector3DSub(triTranslated.p[2], triTranslated.p[0])
    #         normal = Vector3DCrossProduct(line1, line2)
    #         normal = Vector3DNormalise(normal)
    #
    #         # If checks if player sees the triangle so the engine shold render it
    #         cameraRay = Vector3DSub(triTranslated.p[0], cameraPos)
    #         if (Vector3DDotProduct(normal, cameraRay) < 0):
    #             # if(True):
    #
    #             # Illumination
    #             lightDir = [0, -1, -1]
    #             lightDir = Vector3DNormalise(lightDir)
    #
    #             dp = max(0.1, Vector3DDotProduct(lightDir, normal))
    #             triProjected.color = Vector3DMultVector3D(triProjected.color, Vector3DDiv(GetColorShading(dp), 255))
    #
    #             # Convert World Space ---> View Space
    #             tempTriangle = copy.deepcopy(triTranslated)
    #             triTranslated.p[0] = MultiplyMatrixVector(tempTriangle.p[0], triTranslated.p[0], mView)
    #             triTranslated.p[1] = MultiplyMatrixVector(tempTriangle.p[1], triTranslated.p[1], mView)
    #             triTranslated.p[2] = MultiplyMatrixVector(tempTriangle.p[2], triTranslated.p[2], mView)
    #
    #             # Clip Viewed Triangle agains near
    #             clipped = TriangleClipAgainstPlane([0, 0, 0.1], [0, 0, 1.0], triTranslated)
    #
    #             for n in range(len(clipped)):
    #                 # Project Triangles from 3D ---> 2D
    #
    #                 triProjected.p[0] = MultiplyMatrixVector(clipped[n].p[0], triProjected.p[0], mProj)
    #                 triProjected.p[1] = MultiplyMatrixVector(clipped[n].p[1], triProjected.p[1], mProj)
    #                 triProjected.p[2] = MultiplyMatrixVector(clipped[n].p[2], triProjected.p[2], mProj)
    #
    #                 # Scale to View
    #                 triProjected.p[0][0] += 1.0
    #                 triProjected.p[0][1] += 1.0
    #                 triProjected.p[1][0] += 1.0
    #                 triProjected.p[1][1] += 1.0
    #                 triProjected.p[2][0] += 1.0
    #                 triProjected.p[2][1] += 1.0
    #
    #                 triProjected.p[0][0] *= 0.5 * gameDisplay.width
    #                 triProjected.p[0][1] *= 0.5 * gameDisplay.height
    #                 triProjected.p[1][0] *= 0.5 * gameDisplay.width
    #                 triProjected.p[1][1] *= 0.5 * gameDisplay.height
    #                 triProjected.p[2][0] *= 0.5 * gameDisplay.width
    #                 triProjected.p[2][1] *= 0.5 * gameDisplay.height
    #
    #                 trianglesToRaster.append(copy.deepcopy(triProjected))


    def renderUI(object):
        pass
        if (hasattr(object, "Text")):
            font = pygame.font.SysFont(None, 32)
            text = font.render(object.Text.text, True,object.Text.color)

            newPosUI = Vector2D(object.Transform2D.position.x - text.get_rect().width / 2 + gameDisplay.scale.x / 2, object.Transform2D.position.y + text.get_rect().height / 2  - gameDisplay.scale.y / 2)
            newPosUI.y = -newPosUI.y

            gameDisplay.display.blit(text, newPosUI.ToList())







    # Bubble Sort Sprite Layers
    n = len(objects)
    for i in range(n - 1):

        for j in range(0, n - i - 1):

            if objects[j].layer > objects[j + 1].layer:
                objects[j], objects[j + 1] = objects[j + 1], objects[j]


    for cam in camera:
        cam.Transform2D.position = (cam.Transform2D.position * gameDisplay.scale/2) / cam.Camera.scale
        for object in objects:
            if object.isVisible:
                #Outline
                if (hasattr(object, "Outline")):
                    if (hasattr(object, "Sprite")):
                        newPos = cam.Camera.ScreenToWorldVector2D(
                            Vector2D(object.Transform2D.position.x - object.Transform2D.scale.x / 2,
                                     object.Transform2D.position.y + object.Transform2D.scale.y / 2))

                        newImage = pygame.transform.scale(object.Sprite.image, object.Transform2D.scale.ToList())

                        outline = pygame.mask.from_surface(newImage)
                        outlineSurface = outline.to_surface()
                        outlineSurface.set_colorkey([0,0,0])

                        newSurface = pygame.Surface(outlineSurface.get_size()).convert_alpha()
                        newSurface.fill([0,0,0,0])
                        newSurface.blit(outlineSurface, (0,0))

                        # colorImage = pygame.Surface(outlineSurface.get_size()).convert_alpha()
                        # colorImage.fill(sprite.Outline.color)
                        # newSurface.blit(colorImage, (0, 0), special_flags=BLEND_MULT)

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

                        outline.Transform2D.position.x += object.Outline.width.x
                        render2D(outline)
                        outline.Transform2D.position.x -= 2 * object.Outline.width.x
                        render2D(outline)
                        outline.Transform2D.position.x += object.Outline.width.x
                        outline.Transform2D.position.y += object.Outline.width.y
                        render2D(outline)
                        outline.Transform2D.position.y -= 2 * object.Outline.width.y
                        render2D(outline)



                # 2D !!!
                render2D(object)


                # UI !!!
                renderUI(object)


                #3D !!!
                # if (object in objects3D):
                #
                #
                #
                #     render3D(object)
                #
                #     trianglesToRaster.sort(key=lambda tri: (tri.p[0][2] + tri.p[1][2] + tri.p[2][2]) / 3.0, reverse=True)
                #
                #     # Clipping on boarders of the screen
                #     for tri in trianglesToRaster:
                #
                #         listTriangles = []
                #         listTriangles.append(tri)
                #         newTriangles = 1
                #
                #         for p in range(4):
                #             while (newTriangles > 0):
                #                 test = listTriangles[-1]
                #                 listTriangles.pop()
                #                 newTriangles -= 1
                #
                #                 if (p == 0):
                #                     clipped = TriangleClipAgainstPlane([0, 0, 0], [0, 1, 0], test)
                #                 elif (p == 1):
                #                     clipped = TriangleClipAgainstPlane([0, gameDisplay.display.get_height() - 1, 0], [0, -1, 0],
                #                                                        test)
                #                 elif (p == 2):
                #                     clipped = TriangleClipAgainstPlane([0, 0, 0], [1, 0, 0], test)
                #                 elif (p == 3):
                #                     clipped = TriangleClipAgainstPlane([gameDisplay.display.get_width() - 1, 0, 0], [-1, 0, 0],
                #                                                        test)
                #
                #                 for w in range(len(clipped)):
                #                     listTriangles.append(clipped[w])
                #
                #             newTriangles = len(listTriangles)
                #
                #         for newTri in listTriangles:
                #             # Draws the Triangles
                #             pygame.draw.polygon(gameDisplay.display, newTri.color,
                #                                 [[newTri.p[0][0], newTri.p[0][1]], [newTri.p[1][0], newTri.p[1][1]],
                #                                  [newTri.p[2][0], newTri.p[2][1]]])
                #             # pygame.gfxdraw.polygon(gameDisplay.display, [[newTri.p[0][0],newTri.p[0][1]],[newTri.p[1][0],newTri.p[1][1]],[newTri.p[2][0],newTri.p[2][1]]],newTri.color)
                #
                #             # Draws the border of the Triangles
                #             # pygame.draw.polygon(gameDisplay.display, (0,0,0), [[newTri.p[0][0], newTri.p[0][1]],[newTri.p[1][0], newTri.p[1][1]],[newTri.p[2][0], newTri.p[2][1]]],7)
                #             # pygame.gfxdraw.aapolygon(gameDisplay.display, [[newTri.p[0][0], newTri.p[0][1]],[newTri.p[1][0], newTri.p[1][1]],[newTri.p[2][0], newTri.p[2][1]]], (0,0,0))










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



def Main():
    global lastTime

    while not crashed.get("crashed"):
        nowTime = time.time()
        Variables.deltaTime = nowTime - lastTime + 0.00000000001
        lastTime = nowTime
        checkClose()
        checkScreenResize()
        gameDisplay.display.fill(gameDisplay.bgColor)
        physics2D()
        input()
        for update in updateFunctions:
            update()
        renderer()
        eventsUI()
        pygame.display.flip()
        clock.tick(Variables.fps)


    pygame.quit()







#Setup
pygame.init()
gameDisplay = Window()
updateFunctions = []
objects = []

gameDisplay.scale = copy.copy(gameDisplay.originalScale)

# while Variables.deltaTime == 0:
#     for i in range(11):
#         Variables.clock.tick(fps)
#     Variables.deltaTime = 1/Variables.clock.get_fps()

lastTime = time.time()
