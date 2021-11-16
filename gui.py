from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from PIL import Image, ImageTk


def ShowImage():

    global loadedLabel

    file = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetypes=(("JPG file", ".jpg"), ("PNG file", ".png")))
    myImage = Image.open(file)
    width, height = myImage.size
    myImage.thumbnail((380, 380))
    myImage = ImageTk.PhotoImage(myImage)
    loadedLabel.grid(ipadx=0, ipady=0, row=1, column=0, padx=10)
    
    if height>width:
        temp = (380*width)/height
        #TODO şurayı hallet


    """ if(width >= 380):
        loadedLabel.grid(ipadx=0, ipady=0, row=1, column=0, padx=10)
    else:
        print("aa")
        loadedLabel.grid(ipadx=0, ipady=0, row=1, column=0, padx=10+(360-width)) """
        
    loadedLabel.configure(image = myImage)      
    loadedLabel.image = myImage

root = Tk()
root.geometry("800x700")
root.maxsize(800,700)
root.minsize(800,700)

frame = LabelFrame(width=400, height=300, text="Test")
frame.grid(row=0, column=0)

frame2 = Frame(width=400, height=300)
frame2.grid(row=0, column=1)



loadedLabel = Label(root, bd=5, relief="sunken", text="Test")
loadedLabel.grid(ipadx=180, ipady=180, row=1, column=0, padx=10)

manipulatedLabel = Label(root, bd=5, relief="sunken")
manipulatedLabel.grid(ipadx=180, ipady=180, row=1, column=1, padx=(0,50))


button = Button(frame, text="Click", command=ShowImage).grid()


root.title("GUI")
root.mainloop()




















#loadedLabel1 = loadedLabel(root, text="Tatata").grid(row=0, column=0)
#button = Button(root, text="Bas", padx=100, pady=100, command=Print).grid()
