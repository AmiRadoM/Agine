from Agine import *
import os
import sys

projectsPath = "./AgineProjects"

class ProjectItem():
    def __int__(self, name):
        self.name = name

def NewProject(name="NewAgineProject"):
    newProjectMain = """from Agine import *


def update():
    pass


#Start
cam = GameObject()
cam.addAttr("Camera")


#Init
updateFunctions.append(update)
Main()"""

    print("Creating A New Project...")
    def Create(dir):
        with open(dir + "/Main.py", "w+") as p:
            p.write(newProjectMain)

    #if there is no projects directory, Create one
    try:
        os.mkdir(projectsPath)
    except:
        pass
    try:
        os.mkdir(projectsPath + "/" + name)
        Create(projectsPath + "/" + name)
    except:
        i = 1
        while (os.path.exists(projectsPath + "/" + name + str(i))):
            i += 1
        os.mkdir(projectsPath + "/" + name + str(i))
        Create(projectsPath + "/" + name + str(i))
        del i

    print("Created a New Project Successfully :)")
    OpenProject("NewAgineProject")

def OpenProject( name ):
    # __import__(projectsPath[2:]+"."+name+".Main")
    pygame.quit()

    #__import__("AgineProjects.NewAgineProject.Main")
    os.system('python Agine.py AgineProjects/NewAgineProject/Main.py')
    quit()


def update():

    pass

if not sys.platform == "win32":
    raise Exception("AgineMenu is only available for Windows operating system")

#Start
gameDisplay.SetScale(Vector2D(800,700))
gameDisplay.SetSettings(resizable=False)

cam = GameObject()
cam.Camera = Camera()

title = GameObject()
title.Text = Text()
title.Text.text = "Agine"
title.Text.fontSize = 90
title.Text.color = [0,128,0]
title.Transform.position = Vector3D(-3.5, 4.2)

newProjectBtn = GameObject()
newProjectBtn.Transform.position = Vector3D(3.5,4.2)
newProjectBtn.Transform.scale = Vector3D(2,1)
newProjectBtn.Button = Button()
newProjectBtn.Button.onClick.append(NewProject)
newProjectBtn.Square = Square()
newProjectBtn.Square.color = [0,128,0]
newProjectBtn.Text = Text()
newProjectBtn.Text.text = "New Project"


#Init
updateFunctions.append(update)
Main()
