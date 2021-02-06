from Agine import *
import Agine.Agine_main as Agine_main
import os

projectsPath = "./AgineProjects"

class ProjectItem():
    def __int__(self, name):
        self.name = name

def NewProject(name="NewAgineProject"):
    newProjectMain = """from Agine import *


def update():
    pass


#Start



#Init
updateFunctions.append(update)
Main()"""

    print("Creating A New Project...")
    try:
        def Create(dir):
            with open(dir + "/Main.py", "w+") as p:
                p.write(newProjectMain)

        #if there is no projects directory, create one
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
    except:
        print("An Error Has Occurred While Trying to Create a New Project")
    else:
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



#Start
gameDisplay.SetScale(Vector2D(800,700))
gameDisplay.SetSettings(resizable=False)

cam = GameObject()
cam.addAttr('Camera')

title= GameObject()
title.addAttr("Text")
title.Text.text = "Agine"
title.Text.fontSize = 90
title.Text.color = [0,128,0]
title.Transform2D.position = Vector2D(-3.5, 4.2)

newProjectBtn = GameObject()
newProjectBtn.Transform2D.position = Vector2D(3.5,4.2)
newProjectBtn.Transform2D.scale = Vector2D(2,1)
newProjectBtn.addAttr("Button")
newProjectBtn.Button.onClick.append(NewProject)
newProjectBtn.addAttr("Square")
newProjectBtn.Square.color = [0,128,0]
newProjectBtn.addAttr("Text")
newProjectBtn.Text.text = "New Project"


#Init
updateFunctions.append(update)
Main()
