from Agine_main import *
from Physics2D import *
from Variables import *

s = Square()
s.addAttr("Rigidbody2D")

while not crashed.get("crashed"):
    P()
    renderer()
    checkC()

    print(clock.get_fps())
    clock.tick(fps)




