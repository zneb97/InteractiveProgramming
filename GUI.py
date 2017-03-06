import tkinter as tk
from MJ_recursive_art_complex import generate_art
from tkinter import *
from PIL import ImageTk, Image

#TODO: Make a slider class, update functions based on system

#Classes
class myLabel:
    def __init__(self, frame,text,xGrid=0, yGrid=0, stick=None):
        self.label = Label(frame)
        self.label.config(text=text)
        self.label.grid(row=xGrid, column=yGrid, sticky=stick)

    def setPosition(self,xGrid,yGrid,stick=None):
        self.label.grid(row=xGrid, column=yGrid, sticky=stick)

class myCheckButton:
    def __init__(self, frame, text, xGrid=0, yGrid = 0, justify=LEFT, stick=None):
        self.var = IntVar()
        self.name = Checkbutton(frame, text=text, variable=self.var, justify=justify)
        self.name.grid(row= xGrid, column = yGrid, sticky=stick)

    def setPosition(self,xGrid,yGrid,stick=None):
        self.label.grid(row=xGrid, column=yGrid, sticky=stick)

class mySlider:
    def __init__(self, frame, xGrid=0, yGrid = 0, length = 200, start=1, end=10, orientation=HORIZONTAL):
        self.var = IntVar()
        self.depth = Scale(frame, from_=start, to=end, variable=self.var, orient=orientation, length = length)
        self.depth.grid(row=xGrid, column=yGrid)

#Functions
def regen():
    """
    Regenerate art based on user settings
    """
    #Functions to be used (0 No, 1 Yes)
    setFunctions = {'cos_pi':cosPiCheckbox.var.get()*cosPiSlider.var.get(),
                     'sin_pi':sinPiCheckbox.var.get()*sinPiSlider.var.get(),
                  'prod':multiCheckbox.var.get()*multiSlider.var.get(),
                  'avg':avgCheckbox.var.get()*avgSlider.var.get(),
                  'arctan':arcTanCheckbox.var.get()*arcTanSlider.var.get(),
                  'geomean':geoMeanCheckbox.var.get()*geoMeanSlider.var.get()}

    #Depth to recurse to
    #setDepth = depthSlider.var.get()
    #Number system to use (1 for Real, 0 for Imaginary)
    setSystem = numberSystem.get()

    #Get RGB Minimum Depth
    rgbMinDepths = [redMinDepthSlider.var.get(),
                    greenMinDepthSlider.var.get(),
                    blueMinDepthSlider.var.get()]
    #Get RGB Maximum Depth
    rgbMaxDepths = [redMaxDepthSlider.var.get(),
                    greenMaxDepthSlider.var.get(),
                    blueMaxDepthSlider.var.get()]

    #Pass settings into comp art project
    filename = "myArt" + str(initialImageFlag) + ".png"
    generate_art(filename, setSystem, 0, 0, 0, rgbMinDepths, rgbMaxDepths, setFunctions)

    #Regenrate Panel
    img = ImageTk.PhotoImage(file="myArt" + str(initialImageFlag) + ".png")
    panel = Label(root, image = img)
    panel.image = img
    panel.grid(row=2, column=3, rowspan = 11)

#Flag to know first image
initialImageFlag = 0;

#Create window
root = tk.Tk()
root.title("Computational Art")
root.resizable(width = False, height = False)
root.geometry("1250x500")

#Create grid system special rules (use for blank grid rows/columns)
root.grid_columnconfigure(0, minsize=150)
root.grid_columnconfigure(1, minsize=250)
root.grid_columnconfigure(2, minsize=350)
root.grid_columnconfigure(3, minsize=350)
root.grid_rowconfigure(3, minsize=25)

#Create labels
systemSelectLabel = myLabel(root, 'Select system to use:',0,0,W)
funcSelectLabel = myLabel(root, 'Select functions to use:',4,0,W)
depthSelectLabel = myLabel(root, 'Depth',0,2)
weightSelectLabel = myLabel(root, 'Select function weight:',4,1)

redMinDepthSelectLabel = myLabel(root, 'Red Min Depth',0,2)
redMaxDepthSelectLabel = myLabel(root, 'Red Max Depth',2,2)
greenMinDepthSelectLabel = myLabel(root, 'Green Min Depth',4,2)
greenMaxDepthSelectLabel = myLabel(root, 'Green Max Depth',6,2)
blueMinDepthSelectLabel = myLabel(root, 'Blue Min Depth',8,2)
blueMaxDepthSelectLabel = myLabel(root, 'Blue Max Depth',10,2)

#Create checkboxes
arcTanCheckbox = myCheckButton(root, 'ArcTangent',5,0, 'left', W)
geoMeanCheckbox= myCheckButton(root, 'Geometric Mean',6,0, 'left', W)
multiCheckbox = myCheckButton(root, 'Multiply',7,0, 'left', W)
avgCheckbox = myCheckButton(root, 'Average',8,0, 'left', W)
sinPiCheckbox = myCheckButton(root, 'Sin Pi',9,0, 'left', W)
cosPiCheckbox = myCheckButton(root, 'Cos Pi',10,0, 'left', W)

#Create sliders
redMinDepthSlider = mySlider(root, 1, 2, 200)
redMaxDepthSlider = mySlider(root, 3, 2, 200)
greenMinDepthSlider = mySlider(root, 5, 2, 200)
greenMaxDepthSlider = mySlider(root, 7, 2, 200)
blueMinDepthSlider = mySlider(root, 9, 2, 200)
blueMaxDepthSlider = mySlider(root, 11, 2, 200)

arcTanSlider = mySlider(root, 5, 1, 200)
geoMeanSlider = mySlider(root, 6, 1, 200)
multiSlider = mySlider(root, 7, 1, 200)
avgSlider = mySlider(root, 8, 1, 200)
sinPiSlider = mySlider(root, 9, 1, 200)
cosPiSlider = mySlider(root, 10, 1, 200)

#Create Mulitple Choice
numberSystem = IntVar()
Radiobutton(root, text="Real", variable=numberSystem, value=1).grid(row=1, column=0,sticky=W)
Radiobutton(root, text="Imaginary", variable=numberSystem, value=0).grid(row=2, column=0,sticky=W)

#Create button
b1 = tk.Button(root, text = "Generate Art", command = regen)
b1.grid(row=1, column=3)

#Initialize Image
if initialImageFlag==0:
    regen()
    initialImageFlag = 1

root.mainloop()
