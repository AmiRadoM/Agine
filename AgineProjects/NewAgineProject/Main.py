from Agine_main import *
import threading

def update():
    while not crashed:
        pass


def start():
    pass

#Variables

start()

#threading
updateThread = threading.Thread(target=update,args=())
updateThread.start()

checkClose()