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
    endPoint = col1.position+object1.Rigidbody2D.velocity * Variables.deltaTime + 0.000000001
    lineCol, hitNearTime, contactNormal, contactPoint  = LineVsSqr(col1.position, endPoint, expandedColPosition,expandedColScale)

    
    #line.delete()
    if(lineCol):
        if(-hitNearTime<1):
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


    return True, hitNearTime, contactNormal, contactPoint





def collision2D():
    from Attributes import boxcollider
    for i in boxcollider:

        i.BoxCollider.position = i.position + i.BoxCollider.localPosition
        if(type(i) != Circle):
            i.BoxCollider.scale = i.scale + i.BoxCollider.localScale
        if(type(i) == Circle):
            i.BoxCollider.scale =  i.BoxCollider.localScale + i.radius * 2



        i.BoxCollider.square.position = i.BoxCollider.position
        i.BoxCollider.square.scale = i.BoxCollider.scale
        i.BoxCollider.square.isVisible = i.BoxCollider.isVisible


        flag = False
        for j in boxcollider:
            if i != j:

                if (hasattr(i, "Rigidbody2D")  and (not i.BoxCollider.isTrigger and not j.BoxCollider.isTrigger)):
                    collisions = []
                    collided, contactNormal, contactTime = DynamicAABB(i, j)
                    if (collided):
                        collisions.append([j, contactNormal, contactTime])
                    collisions.sort(key=lambda x: x[2])
                    for c in collisions:
                        v1 = i.Rigidbody2D.velocity
                        m1 = i.Rigidbody2D.mass

                        i.Rigidbody2D.velocity += abs(v1) * c[1]


                        if (hasattr(j, "Rigidbody2D")):

                            v2 = j.Rigidbody2D.velocity
                            m2 = j.Rigidbody2D.mass

                            j.Rigidbody2D.velocity = (v2 * ((m2 - m1) / (m1 + m2))) + (v1 * ((2 * m1) / (m1 + m2))) * abs(c[1])

                            # So They Would't Get Stuck
                            # i.Rigidbody2D.velocity += c[1]











                else:
                    if(AABB(i, j) and i.BoxCollider.isTrigger):
                        flag = True



        if (flag):
            i.BoxCollider.square.color = (255, 0, 0)
        else:
            i.BoxCollider.square.color = (0, 255, 0)
            pass
