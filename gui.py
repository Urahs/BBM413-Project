from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from PIL import Image, ImageTk


def ShowImage():

    global loadedLabel

    file = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetypes=(("JPG file", ".jpg"), ("PNG file", ".png")))
    myImage = Image.open(file)
    #myImage.thumbnail((700, 700))
    myImage = ImageTk.PhotoImage(myImage)   
    loadedLabel.configure(image = myImage)      
    loadedLabel.image = myImage

root = Tk()
root.geometry("800x700")


frame = Frame(width=400, height=300 )
frame.grid(row=0, column=0)

frame2 = Frame(width=400, height=300)
frame2.grid(row=0, column=1)



loadedLabel = Label(root, bd=5, relief="sunken")
loadedLabel.grid(ipadx=180, ipady=180, row=1, column=0)

manipulatedLabel = Label(root, bd=5, relief="sunken")
manipulatedLabel.grid(ipadx=180, ipady=180, row=1, column=1)


#button = Button(root, text="Click", command=ShowImage).grid()


root.title("GUI")
root.mainloop()




















#loadedLabel1 = loadedLabel(root, text="Tatata").grid(row=0, column=0)
#button = Button(root, text="Bas", padx=100, pady=100, command=Print).grid()
