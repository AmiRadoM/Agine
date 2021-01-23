from Objects2D import *
import math

def AABB(object1, object2):
    col1 = object1.BoxCollider
    col2 = object2.BoxCollider

    if(col1.x < col2.x + col2.scale[0] and\
    col1.x + col1.scale[0] > col2.x and\
    col1.y < col2.y + col2.scale[1] and\
    col1.y + col1.scale[1] > col2.y):
        return True

    return False

def DynsamicAABB(object1, object2):
    pass


def LineVsSqr(line, sqr, circle):
    lineDirection = [(line.endPoint[0] - line.startPoint[0]), (line.endPoint[1] - line.startPoint[1])]
    lineDirection = [ 0.001 if i == 0 else i for i in lineDirection]
    nearX = (sqr.x - sqr.scale[0]/2 - line.startPoint[0]) / lineDirection[0]
    nearY = (sqr.y - sqr.scale[1]/2 - line.startPoint[1]) / lineDirection[1]
    farX = (sqr.x + sqr.scale[0]/2 - line.startPoint[0]) / lineDirection[0]
    farY = (sqr.y + sqr.scale[1]/2 - line.startPoint[1]) / lineDirection[1]

    #Sorting
    if(nearX > farX):
        temp = nearX
        nearX = farX
        farX = temp
    if (nearY > farY):
        temp = nearY
        nearY = farY
        farY = temp

    if(nearX>farY or nearY > farX): return False

    hitNearTime = max([nearX,nearY])
    hitFarTime = max([farX,farY])

    if(hitFarTime < 0 or hitNearTime > 1): return False



    contactPoint = [line.startPoint[0] + hitNearTime * lineDirection[0],line.startPoint[1] + hitNearTime * lineDirection[1]]
    circle.x=contactPoint[0]
    circle.y=contactPoint[1]
    circle.isVisible = True


    #Normal
    if(nearX>nearY):
        if(lineDirection[0] < 0):
            contactNormal = [1, 0]
        else:
            contactNormal = [-1, 0]
    elif(nearX<nearY):
        if (lineDirection[1] < 0):
            contactNormal = [0, 1]
        else:
            contactNormal = [0, -1]


    return True





def collision2D():
    from Attributes import BC
    for i in BC:
        pass
        i.BoxCollider.x = i.x + i.BoxCollider.localX
        i.BoxCollider.y = i.y + i.BoxCollider.localY
        i.BoxCollider.scale[0] = i.scale[0] + i.BoxCollider.localScale[0]
        i.BoxCollider.scale[1] = i.scale[1] + i.BoxCollider.localScale[1]


        i.BoxCollider.square.x = i.BoxCollider.x
        i.BoxCollider.square.y = i.BoxCollider.y
        i.BoxCollider.square.scale[0] = i.BoxCollider.scale[0]
        i.BoxCollider.square.scale[1] = i.BoxCollider.scale[1]
        i.BoxCollider.square.isVisible = i.BoxCollider.isVisible



        for j in BC:
            if i != j:
                if(AABB(i, j)):
                    i.BoxCollider.square.color = (255, 0, 0)
                    j.BoxCollider.square.color = (255, 0, 0)
                else:
                    i.BoxCollider.square.color = (0, 255, 0)
                    j.BoxCollider.square.color = (0, 255, 0)
