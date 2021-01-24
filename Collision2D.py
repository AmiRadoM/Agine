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
    from Agine_main import Draw
    #line = Line(startPoint=Vector2D(col1.position.x,col1.position.y), endPoint = Vector2D(col1.position.x+object1.Rigidbody2D.velocity.x,col1.position.y+object1.Rigidbody2D.velocity.y), isVisible= True)
    endPoint = col1.position+object1.Rigidbody2D.velocity * Variables.deltaTime + 0.0001
    lineCol, hitNearTime, contactNormal, contactPoint  = LineVsSqr(col1.position, endPoint, expandedColPosition,expandedColScale)

    
    #line.delete()
    if(lineCol):
        if(hitNearTime<1):
            return True, contactNormal,hitNearTime


    return False, None, None







def LineVsSqr(startPoint, endPoint, sqrPosition, sqrScale):

    lineDirection = Vector2D((endPoint.x - startPoint.x), (endPoint.y - startPoint.y))
    if(lineDirection.x == 0):
        return False, None, None, None
    if (lineDirection.y == 0):
        return False, None, None, None
    nearTime = (sqrPosition + Vector2D(-sqrScale.x/2,sqrScale.y/2) - startPoint) / lineDirection

    farTime = (Vector2D(sqrScale.x/2, - sqrScale.y/2) + sqrPosition  - startPoint) / lineDirection

    #Sorting
    if(nearTime.x > farTime.x):
        temp = nearTime.x
        nearTime.x = farTime.x
        farTime.x = temp
    if (nearTime.y > farTime.y):
        temp = nearTime.y
        nearTime.y = farTime.y
        farTime.y = temp

    if(nearTime.x>farTime.y or nearTime.y > farTime.x): return False, None, None, None

    hitNearTime = max([nearTime.x,nearTime.y])
    hitFarTime = max([farTime.x,farTime.y])

    if(hitFarTime < 0 or hitNearTime > 1): return False, None, None, None



    contactPoint = Vector2D(startPoint.x + hitNearTime * lineDirection.x,startPoint.y + hitNearTime * lineDirection.y)

    #Normal
    contactNormal = Vector2D(0,0)

    if(nearTime.x>nearTime.y):
        if(lineDirection.x < 0):
            contactNormal = Vector2D(1,0)
        else:
            contactNormal = Vector2D(-1,0)
    elif(nearTime.x<nearTime.y):
        if (lineDirection.y < 0):
            contactNormal = Vector2D(0,1)
        else:
            contactNormal = Vector2D(0,-1)


    return True, -hitNearTime, contactNormal, contactPoint





def collision2D():
    from Attributes import BC
    for i in BC:

        i.BoxCollider.position = i.position + i.BoxCollider.localPosition
        if(type(i) != Circle):
            i.BoxCollider.scale = i.scale + i.BoxCollider.localScale
        if(type(i) == Circle):
            i.BoxCollider.scale =  i.BoxCollider.localScale + i.radius * 2



        i.BoxCollider.square.position = i.BoxCollider.position
        i.BoxCollider.square.scale = i.BoxCollider.scale
        i.BoxCollider.square.isVisible = i.BoxCollider.isVisible



        for j in BC:
            if i != j:

                if (hasattr(i, "Rigidbody2D") and (not i.BoxCollider.isTrigger and not j.BoxCollider.isTrigger)):
                    collisions = []
                    collided, contactNormal, contactTime = DynamicAABB(i, j)
                    if (collided):
                        collisions.append([j, contactNormal, contactTime])
                    collisions.sort(key=lambda x: x[2])
                    for c in collisions:
                        i.Rigidbody2D.velocity += abs(i.Rigidbody2D.velocity) * c[1]

                else:
                    if(AABB(i, j)):


                        i.BoxCollider.square.color = (255, 0, 0)
                        j.BoxCollider.square.color = (255, 0, 0)
                    else:
                        i.BoxCollider.square.color = (0, 255, 0)
                        j.BoxCollider.square.color = (0, 255, 0)
