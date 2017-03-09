"""
This is the GUI side of Ben and MJ's Software Design
Mini Project 4, Interactive programming. It takes in settings from the user
and passes it to the computational art program to generate new imaginary and
real number based art.
"""

import tkinter as tk
from tkinter import ttk
from ComputationalArt import generate_art_real
from ComputationalArt import generate_art_imaginary
from tkinter import *
from PIL import ImageTk, Image
import platform

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
        self.name.select()

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

    Pulls in settings from various widgets
    """

    filename = "myArt" + str(initialImageFlag) + ".png"
    setSystem = numberSystem.get()

    #Real
    if setSystem:

        #Set custom colors, defaults RGB
        color1 =[int(redRewriteR.get()),int(redRewriteG.get()),int(redRewriteB.get())]
        color2 = [int(greenRewriteR.get()),int(greenRewriteG.get()),int(greenRewriteB.get())]
        color3 =[int(blueRewriteR.get()),int(blueRewriteG.get()),int(blueRewriteB.get())]

        #Set recursive depth
        mins = [minSliderRed.var.get(),minSliderGreen.var.get(),minSliderBlue.var.get()]
        maxes = [maxSliderRed.var.get(),maxSliderGreen.var.get(),maxSliderBlue.var.get()]

        #Functions to be used and weight for red
        redFreq = {'cos_pi':cosPiCheckboxRed.var.get()*cosPiSliderRed.var.get(),
                         'sin_pi':sinPiCheckboxRed.var.get()*sinPiSliderRed.var.get(),
                      'prod':multiCheckboxRed.var.get()*multiSliderRed.var.get(),
                      'avg':avgCheckboxRed.var.get()*avgSliderRed.var.get(),
                      'arctan':arcTanCheckboxRed.var.get()*arcTanSliderRed.var.get(),
                      'geomean':geoMeanCheckboxRed.var.get()*geoMeanSliderRed.var.get()}

        #Functions to be used and weight for green
        greenFreq = {'cos_pi':cosPiCheckboxGreen.var.get()*cosPiSliderGreen.var.get(),
                         'sin_pi':sinPiCheckboxGreen.var.get()*sinPiSliderGreen.var.get(),
                      'prod':multiCheckboxGreen.var.get()*multiSliderGreen.var.get(),
                      'avg':avgCheckboxGreen.var.get()*avgSliderGreen.var.get(),
                      'arctan':arcTanCheckboxGreen.var.get()*arcTanSliderGreen.var.get(),
                      'geomean':geoMeanCheckboxGreen.var.get()*geoMeanSliderGreen.var.get()}

        #Functions to be used and weight for blue
        blueFreq = {'cos_pi':cosPiCheckboxBlue.var.get()*cosPiSliderBlue.var.get(),
                         'sin_pi':sinPiCheckboxBlue.var.get()*sinPiSliderBlue.var.get(),
                      'prod':multiCheckboxBlue.var.get()*multiSliderBlue.var.get(),
                      'avg':avgCheckboxBlue.var.get()*avgSliderBlue.var.get(),
                      'arctan':arcTanCheckboxBlue.var.get()*arcTanSliderBlue.var.get(),
                      'geomean':geoMeanCheckboxBlue.var.get()*geoMeanSliderBlue.var.get()}

        generate_art_real(filename, color1, color2, color3, mins, maxes, redFreq, greenFreq, blueFreq)

    #Imaginary
    else:
        #Recursive min/max depth
        minsImagine = [minSliderImagine.var.get()]
        maxesImagine = [maxSliderImagine.var.get()]

        #Functions to be used and weight
        frequencyImagine = {'sum':sumCheckboxImagine.var.get()*sumSliderImagine.var.get(),
                        'mult':multiCheckboxImagine.var.get()*multiSliderImagine.var.get(),
                        'cos':cosCheckboxImagine.var.get()*cosSliderImagine.var.get(),
                        'exp':expCheckboxImagine.var.get()*expSliderImagine.var.get()}

        generate_art_imaginary(filename, maxesImagine, minsImagine, frequencyImagine)

    #Regenrate Panel
    img = ImageTk.PhotoImage(file="myArt" + str(initialImageFlag) + ".png")
    panel = Label(root, image = img)
    panel.image = img
    panel.grid(row=2, column=1, rowspan = 15)

#Flag to know first image
initialImageFlag = 0

#Create windows --------------------------------------------------------------
root = tk.Tk()
root.title("Computational Art")
root.resizable(width = False, height = False)
root.geometry("850x600")

notebook = ttk.Notebook(root)
frameRed = ttk.Frame(notebook)
frameGreen = ttk.Frame(notebook)
frameBlue = ttk.Frame(notebook)
frameImagine = ttk.Frame(notebook)
notebook.add(frameRed, text='Red Settings')
notebook.add(frameGreen, text='Green Settings')
notebook.add(frameBlue, text='Blue Settings')
notebook.add(frameImagine, text = 'Imaginary Settings')
notebook.grid(row =4, column = 0, rowspan=15, stick=W)

#Create grid system special rules (use for blank grid rows/columns)------------
root.grid_columnconfigure(0, minsize=450)
root.grid_columnconfigure(1, minsize=250)
root.grid_rowconfigure(3, minsize=25)
frameRed.grid_columnconfigure(0, minsize= 200)
frameGreen.grid_columnconfigure(0, minsize= 200)
frameBlue.grid_columnconfigure(0, minsize= 200)
frameImagine.grid_columnconfigure(0, minsize= 200)

#Create geneal labels---------------------------------------------------------
systemSelectLabel = myLabel(root, 'Select system to use:',0,0,W)
systemSelectLabel = myLabel(root, 'MJ MCMillen & Ben Ziemann',17,1)
systemSelectLabel = myLabel(root, 'Software Design Project 4',18,1)

#Color Setting tabs ----------------------------------------------------------

#Red Tab
redFuncLabel = myLabel(frameRed, 'Select functions to use:',0,0,W)
redWeightLabel = myLabel(frameRed, 'Select function weight:',0,1,W)

    #Checkboxes
arcTanCheckboxRed = myCheckButton(frameRed, 'ArcTangent',1,0, 'left', W)
geoMeanCheckboxRed = myCheckButton(frameRed, 'Geometric Mean',2,0, 'left', W)
multiCheckboxRed = myCheckButton(frameRed, 'Multiply',3,0, 'left', W)
avgCheckboxRed = myCheckButton(frameRed, 'Average',4,0, 'left', W)
sinPiCheckboxRed = myCheckButton(frameRed, 'Sin Pi',5,0, 'left', W)
cosPiCheckboxRed = myCheckButton(frameRed, 'Cos Pi',6,0, 'left', W)

    #Slider
arcTanSliderRed = mySlider(frameRed, 1, 1, 200)
geoMeanSliderRed = mySlider(frameRed, 2, 1, 200)
multiSliderRed = mySlider(frameRed, 3, 1, 200)
avgSliderRed = mySlider(frameRed, 4, 1, 200)
sinPiSliderRed = mySlider(frameRed, 5, 1, 200)
cosPiSliderRed = mySlider(frameRed, 6, 1, 200)

    #Color Rewrite
redRewriteLabel = myLabel(frameRed, 'New Color, R value:',9,0,W)
redRewriteR = Entry(frameRed)
redRewriteR.grid(row =9, column= 1)
redRewriteR.insert(0, '255')
redRewriteLabel = myLabel(frameRed, 'New Color, G value:',10,0,W)
redRewriteG = Entry(frameRed)
redRewriteG.grid(row =10, column= 1)
redRewriteG.insert(0, '0')
redRewriteLabel = myLabel(frameRed, 'New Color, B value:',11,0,W)
redRewriteB = Entry(frameRed)
redRewriteB.grid(row =11, column= 1)
redRewriteB.insert(0, '0')

    #Depth
redDepthLabel = myLabel(frameRed, 'Min Depth:',13,0,W)
redDepthLabel = myLabel(frameRed, 'Max Depth:',14,0,W)
minSliderRed = mySlider(frameRed, 13, 1, 200)
maxSliderRed = mySlider(frameRed, 14, 1, 200)

#Green Tab
greenFuncLabel = myLabel(frameGreen, 'Select functions to use:',0,0,W)
greenWeightLabel = myLabel(frameGreen, 'Select function weight:',0,1,W)

    #Checkboxes
arcTanCheckboxGreen = myCheckButton(frameGreen, 'ArcTangent',1,0, 'left', W)
geoMeanCheckboxGreen = myCheckButton(frameGreen, 'Geometric Mean',2,0, 'left', W)
multiCheckboxGreen = myCheckButton(frameGreen, 'Multiply',3,0, 'left', W)
avgCheckboxGreen = myCheckButton(frameGreen, 'Average',4,0, 'left', W)
sinPiCheckboxGreen = myCheckButton(frameGreen, 'Sin Pi',5,0, 'left', W)
cosPiCheckboxGreen = myCheckButton(frameGreen, 'Cos Pi',6,0, 'left', W)

    #Slider
arcTanSliderGreen = mySlider(frameGreen, 1, 1, 200)
geoMeanSliderGreen = mySlider(frameGreen, 2, 1, 200)
multiSliderGreen = mySlider(frameGreen, 3, 1, 200)
avgSliderGreen = mySlider(frameGreen, 4, 1, 200)
sinPiSliderGreen = mySlider(frameGreen, 5, 1, 200)
cosPiSliderGreen = mySlider(frameGreen, 6, 1, 200)

    #Color Rewrite
greenRewriteLabel = myLabel(frameGreen, 'New Color, R value:',9,0,W)
greenRewriteR = Entry(frameGreen)
greenRewriteR.grid(row =9, column= 1)
greenRewriteR.insert(0, '0')
greenRewriteLabel = myLabel(frameGreen, 'New Color, G value:',10,0,W)
greenRewriteG = Entry(frameGreen)
greenRewriteG.grid(row =10, column= 1)
greenRewriteG.insert(0, '255')
greenRewriteLabel = myLabel(frameGreen, 'New Color, B value:',11,0,W)
greenRewriteB = Entry(frameGreen)
greenRewriteB.grid(row =11, column= 1)
greenRewriteB.insert(0, '0')

    #depth
greenDepthLabel = myLabel(frameGreen, 'Min Depth:',13,0,W)
greenDepthLabel = myLabel(frameGreen, 'Max Depth:',14,0,W)
minSliderGreen = mySlider(frameGreen, 13, 1, 200)
maxSliderGreen = mySlider(frameGreen, 14, 1, 200)

#Blue Tab
blueFuncLabel = myLabel(frameBlue, 'Select functions to use:',0,0,W)
blueWeightLabel = myLabel(frameBlue, 'Select function weight:',0,1,W)

    #Checkboxes
arcTanCheckboxBlue = myCheckButton(frameBlue, 'ArcTangent',1,0, 'left', W)
geoMeanCheckboxBlue = myCheckButton(frameBlue, 'Geometric Mean',2,0, 'left', W)
multiCheckboxBlue = myCheckButton(frameBlue, 'Multiply',3,0, 'left', W)
avgCheckboxBlue = myCheckButton(frameBlue, 'Average',4,0, 'left', W)
sinPiCheckboxBlue = myCheckButton(frameBlue, 'Sin Pi',5,0, 'left', W)
cosPiCheckboxBlue = myCheckButton(frameBlue, 'Cos Pi',6,0, 'left', W)

    #Sliders
arcTanSliderBlue = mySlider(frameBlue, 1, 1, 200)
geoMeanSliderBlue = mySlider(frameBlue, 2, 1, 200)
multiSliderBlue = mySlider(frameBlue, 3, 1, 200)
avgSliderBlue = mySlider(frameBlue, 4, 1, 200)
sinPiSliderBlue = mySlider(frameBlue, 5, 1, 200)
cosPiSliderBlue = mySlider(frameBlue, 6, 1, 200)

    #Color Rewrite
blueRewriteLabel = myLabel(frameBlue, 'New Color, R value:',9,0,W)
blueRewriteR = Entry(frameBlue)
blueRewriteR.grid(row =9, column= 1)
blueRewriteR.insert(0, '0')
blueRewriteLabel = myLabel(frameBlue, 'New Color, G value:',10,0,W)
blueRewriteG = Entry(frameBlue)
blueRewriteG.grid(row =10, column= 1)
blueRewriteG.insert(0, '0')
blueRewriteLabel = myLabel(frameBlue, 'New Color, B value:',11,0,W)
blueRewriteB = Entry(frameBlue)
blueRewriteB.grid(row =11, column= 1)
blueRewriteB.insert(0, '255')

    #Depth
blueDepthLabel = myLabel(frameBlue, 'Min Depth:',13,0,W)
blueDepthLabel = myLabel(frameBlue, 'Max Depth:',14,0,W)
minSliderBlue = mySlider(frameBlue, 13, 1, 200)
maxSliderBlue = mySlider(frameBlue, 14, 1, 200)

#Imagine Tab
imagineFuncLabel = myLabel(frameImagine, 'Select functions to use:',0,0,W)
imagineWeightLabel = myLabel(frameImagine, 'Select function weight:',0,1,W)

    #Checkboxes
sumCheckboxImagine = myCheckButton(frameImagine, 'Sum',1,0, 'left', W)
multiCheckboxImagine = myCheckButton(frameImagine, 'Multiply',2,0, 'left', W)
cosCheckboxImagine = myCheckButton(frameImagine, 'Cosine',3,0, 'left', W)
expCheckboxImagine = myCheckButton(frameImagine, 'Exponent',4,0, 'left', W)
expCheckboxImagine.name.deselect()

    #Sliders
sumSliderImagine = mySlider(frameImagine, 1, 1, 200)
multiSliderImagine = mySlider(frameImagine, 2, 1, 200)
cosSliderImagine = mySlider(frameImagine, 3, 1, 200)
expSliderImagine = mySlider(frameImagine, 4, 1, 200)

    #Depth
imagineDepthLabel = myLabel(frameImagine, 'Min Depth:',6,0,W)
imagineDepthLabel = myLabel(frameImagine, 'Max Depth:',7,0,W)
minSliderImagine = mySlider(frameImagine, 6, 1, 200)
maxSliderImagine = mySlider(frameImagine, 7, 1, 200)

#Create Mulitple Choice -------------------------------------------------------
numberSystem = IntVar()
Radiobutton(root, text="Imaginary", variable=numberSystem, value=0).grid(row=2, column=0,sticky=W)
Radiobutton(root, text="Real", variable=numberSystem, value=1).grid(row=1, column=0,sticky=W)
numberSystem.set(1)

#Create button
b1 = tk.Button(root, text = "Generate Art", command = regen)
b1.grid(row=1, column=1)

#Initialize Image
if initialImageFlag==0:
    regen()
    initialImageFlag = 1

root.mainloop()
