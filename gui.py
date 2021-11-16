from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from PIL import Image, ImageTk


def ShowImage():

    global myLabel

    file = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetypes=(("JPG file", ".jpg"), ("PNG file", ".png")))    #test
    myImage = Image.open(file)
    myImage.thumbnail((700, 700))
    myImage = ImageTk.PhotoImage(myImage)   
    myLabel.configure(image = myImage)      
    myLabel.image = myImage                 

root = Tk()


myLabel = Label(root)
myLabel.pack()

button = Button(root, text="Click", command=ShowImage).pack()



root.geometry("400x400")
root.title("GUI")
root.mainloop()




















#myLabel1 = myLabel(root, text="Tatata").grid(row=0, column=0)
#button = Button(root, text="Bas", padx=100, pady=100, command=Print).grid()
