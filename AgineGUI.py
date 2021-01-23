import tkinter as tk
import tkinter.font as tkFont
import os


#Variables
projectsPath = "./AgineProjects"

newProjectMain = """from Variables import *
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
Main()"""

##########
#Functions
##########

def NewProject(name = "NewAgineProject"):
    
    def Create(dir):
        with open(dir + "/Main.py", "w+") as p:
                p.write(newProjectMain)
    
    try:
        os.mkdir(projectsPath)
    except:
        pass
    try:
        os.mkdir(projectsPath+"/"+name)
        Create(projectsPath + "/" + name)
    except:
        i = 1
        while(os.path.exists(projectsPath+"/"+name+ str(i))):
            i+=1
        os.mkdir(projectsPath+"/"+name+str(i))
        Create(projectsPath + "/" + name + str(i))
        del i

def openProject( name = None):
    if name != None:
        root.withdraw()
        __import__(projectsPath[2:]+"."+name+".Main")
        root.deiconify()


########
#TKinter
########

root = tk.Tk(screenName="Agine",baseName="Agine")
root.title("Agine")
root.geometry("800x600")
root.resizable(False,False)

#Frames
MainFrame = tk.Frame(root)
ProjectsFrame = tk.Frame(MainFrame,bg = "white")

#Fonts
mainTitleFont = tkFont.Font(family = "Rubik", size = "37")
titleFont = tkFont.Font(family = "Rubik", size = "24")
textFont = tkFont.Font(family = "Rubik", size = "10")
buttonFont = tkFont.Font(family = "Rubik", size = "14")

#################
#Create Elements
#################

#Labels
mainTitle = tk.Label(MainFrame,text = "Agine",fg = "#008000",font=mainTitleFont)
projectTitleLabel = tk.Label(MainFrame,text = "Projects", fg = "#008000",font=titleFont)
projectNameLabel = tk.Label(ProjectsFrame,text = "Project Name",bg = "white",font = textFont)


#Buttons
createProjectButton = tk.Button(MainFrame, text = "New Project",width = 10, height = 1, bg = "#90EE90",font = buttonFont,command = NewProject)

#ListBoxes
projectsListBox = tk.Listbox(ProjectsFrame)

#ScrollBars
projectsScrollBar = tk.Scrollbar(ProjectsFrame)

##########
#Config
##########

#ListBoxes
projectsListBox.config(yscrollcommand = projectsScrollBar.set)
projectsListBox.bind('<Double-1>', lambda event:openProject(projectsListBox.get(projectsListBox.curselection())))

#ScrollBars
projectsScrollBar.config(command = projectsListBox.yview)



#Show all Projects in ProjectFrame()
i = 0
for proj in os.scandir(projectsPath):
    projectsListBox.insert(i,proj.name)
    i+=1
del i

########################
#Put Elements to Screen
########################

#Frames
ProjectsFrame.place(relwidth = 0.65, relheight=0.7,relx = 0.3,rely = 0.25)

#Titles
mainTitle.place(relx=0.05, rely = 0)
projectTitleLabel.place(relx=0.295, rely = 0.17)
projectNameLabel.place(relx=-0.005,rely = 0.01)

#Buttons
createProjectButton.place(relx=0.8,rely=0.17)

#ListBoxes
projectsListBox.place(relw = 1, relh = 0.93,rely = 0.07)

#ScrollBars
projectsScrollBar.place( relh = 0.93,rely = 0.07,relx = 0.97)



MainFrame.place(relwidth = 1, relheight=1)



root.mainloop()