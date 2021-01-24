from Objects2D import *
import Variables
from Attributes import *

def AABB(object1, object2):
    col1 = object1.BoxCollider
    col2 = object2.BoxCollider

    if(col1.position.x - col1.scale.x/2 < col2.position.x + col2.scale.x/2 and\
    col1.position.x + col1.scale.x/2 > col2.position.x - col2.scale.x/2 and\
    col1.position.y - col1.scale.y/2 < col2.position.y + col2.scale.y/2 and\
    col1.position.y + col1.scale.y/2 > col2.position.y - col2.scale.y/2):
        return True

    return False

def DynamicAABB(object1, object2):
    col1 = object1.BoxCollider
    col2 = object2.BoxCollider

    expandedColPosition = col2.position
    expandedColScale = col2.scale + col1.scale
    #line = Line(startPoint=Vector2D(col1.position.x,col1.position.y), endPoint = Vector2D(col1.position.x+object1.Rigidbody2D.velocity.x,col1.position.y+object1.Rigidbody2D.velocity.y), isVisible= True)
    endPoint = col1.position+object1.Rigidbody2D.velocity * Variables.deltaTime
    lineCol, hitNearTime, contactNormal  = LineVsSqr(col1.position, endPoint, expandedColPosition,expandedColScale)

    #line.delete()
    if(lineCol):
        if(hitNearTime<1):
            object1.Rigidbody2D.velocity += abs(object1.Rigidbody2D.velocity) * contactNormal
            return True

    return False







def LineVsSqr(startPoint, endPoint, sqrPosition, sqrScale):

    lineDirection = Vector2D((endPoint.x - startPoint.x), (endPoint.y - startPoint.y))
    if(lineDirection.x == 0):
        lineDirection.x = 0.0001
    if (lineDirection.y == 0):
        lineDirection.y = 0.0001
    nearX = (sqrPosition.x - sqrScale.x/2 - startPoint.x) / lineDirection.x
    nearY = (sqrPosition.y - sqrScale.y/2 - startPoint.y) / lineDirection.y
    farX = (sqrPosition.x + sqrScale.x/2 - startPoint.x) / lineDirection.x
    farY = (sqrPosition.y + sqrScale.y/2 - startPoint.y) / lineDirection.y

    #Sorting
    if(nearX > farX):
        temp = nearX
        nearX = farX
        farX = temp
    if (nearY > farY):
        temp = nearY
        nearY = farY
        farY = temp

    if(nearX>farY or nearY > farX): return False, None, None

    hitNearTime = max([nearX,nearY])
    hitFarTime = max([farX,farY])

    if(hitFarTime < 0 or hitNearTime > 1): return False, None, None



    contactPoint = Vector2D(startPoint.x + hitNearTime * lineDirection.x,startPoint.y + hitNearTime * lineDirection.y)


    #Normal
    contactNormal = Vector2D(0,0)

    if(nearX>nearY):
        if(lineDirection.x < 0):
            contactNormal = Vector2D(1,0)
        else:
            contactNormal = Vector2D(-1,0)
    elif(nearX<nearY):
        if (lineDirection.y < 0):
            contactNormal = Vector2D(0,1)
        else:
            contactNormal = Vector2D(0,-1)


    return True, hitNearTime, contactNormal





def collision2D():
    from Attributes import BC
    for i in BC:

        i.BoxCollider.position = i.position + i.BoxCollider.localPosition
        i.BoxCollider.scale = i.scale + i.BoxCollider.localScale


        i.BoxCollider.square.position = i.BoxCollider.position
        i.BoxCollider.square.scale = i.BoxCollider.scale
        i.BoxCollider.square.isVisible = i.BoxCollider.isVisible



        for j in BC:
            if i != j:

                if(AABB(i, j)):
                    if (hasattr(i, "Rigidbody2D")):
                        DynamicAABB(i, j)

                    i.BoxCollider.square.color = (255, 0, 0)
                    j.BoxCollider.square.color = (255, 0, 0)
                else:
                    i.BoxCollider.square.color = (0, 255, 0)
                    j.BoxCollider.square.color = (0, 255, 0)
