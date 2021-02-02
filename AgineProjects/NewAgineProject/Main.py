from Variables import *
from Agine_main import *
import threading


def update():
    while not crashed.get("crashed"):
        pass


def start():
    pass

#Variables

start()

#threading
updateThread = threading.Thread(target=update,args=())
updateThread.start()
Main()