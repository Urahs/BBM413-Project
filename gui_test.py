import tkinter as tk
from tkinter import Button, Frame, Label, Canvas, LabelFrame, filedialog
from tkinter.constants import ANCHOR, LEFT
from PIL import Image, ImageTk
import os

class GUI:
  def __init__(self):
    self.window = tk.Tk()
    self.window.resizable(False, False)
    self.window.state("zoomed")
    self.window.resizable(False, False)
    self.get_window_size()
    self.frame1()
    self.frame2()
    self.frame3(r".\images\default_image.jpg")
    self.frame4()
  
  def frame1(self):
    self.frame_1 = Frame(self.window, width=int(self.window_width * 0.5), height=int(self.window_height * 0.3))
    self.frame_1.grid()
    
    self.frame_internal_file = LabelFrame(self.frame_1, text="File Operations")
    self.frame_internal_file.grid(row=0, column=0)

    self.frame_internal_process = LabelFrame(self.frame_1, text="Image Process")
    self.frame_internal_process.grid(row=0, column=1, padx=(int(self.window_width * 0.05)))
    
    self.loadButton = Button(self.frame_internal_file, text="Load Image", command=self.load_image).grid(row=0, column=0, sticky="w")
    self.saveButton = Button(self.frame_internal_file, text="Save Image").grid(row=1, column=0, sticky="w")



    self.blurButton = Button(self.frame_internal_process, text="Blur Image").grid(row=0, column=2, sticky="w")
    self.deblurButton = Button(self.frame_internal_process, text="Deblur Image").grid(row=1, column=2, sticky="w")
    self.grayscaleButton = Button(self.frame_internal_process, text="Grayscale Image").grid(row=2, column=2, sticky="w")
    self.cropButton = Button(self.frame_internal_process, text="Crop Image").grid(row=3, column=2, sticky="w")
    self.flipButton = Button(self.frame_internal_process, text="Flip Image").grid(row=4, column=2, sticky="w")
    self.mirrorButton = Button(self.frame_internal_process, text="Mirror Image").grid(row=5, column=2, sticky="w")
    self.rotateButton = Button(self.frame_internal_process, text="Rotate Image").grid(row=6, column=2, sticky="w")
    self.reverseColorButton = Button(self.frame_internal_process, text="Reverse Color Image").grid(row=7, column=2, sticky="w")
    #self.Button = Button(self.frame_internal_process, text="").grid(row=, column=2, sticky="w")
    self.changeColorBalanceButton = Button(self.frame_internal_process, text="Change Color Balance Image").grid(row=8, column=2, sticky="w")



    self.brightButton = Button(self.frame_internal_process, text="Adjust Brightness of Image").grid(row=0, column=3, sticky="w")
    self.contrastButton = Button(self.frame_internal_process, text="Adjust Contrast of Image").grid(row=1, column=3, sticky="w")
    self.saturationButton = Button(self.frame_internal_process, text="Adjust Saturation of Image").grid(row=2, column=3, sticky="w")
    self.noiseButton = Button(self.frame_internal_process, text="Add Noise to Image").grid(row=3, column=3, sticky="w")
    self.detectEdgesButton = Button(self.frame_internal_process, text="Detect Edges of Image").grid(row=3, column=3, sticky="w")

  def frame2(self):
    self.frame_2 = Frame(self.window, width=int(self.window_width * 0.5), height=int(self.window_height * 0.3), bg="purple")
    self.frame_2.grid(row=0, column=1)
  
  def frame3(self, image_path):
    #ADD frame_3 TO window<
    self.frame_3 = Frame(self.window,  width=int(self.window_width * 0.5), height=int(self.window_height * 0.7))
    self.frame_3.grid(row=1, column=0)
    #ADD frame_3 TO window>

    loaded_image = Image.open(image_path)
    #why -5, ask to asim:)
    loaded_image.thumbnail((self.get_responsive_width(0.5), self.get_responsive_height(0.7)))    
    loaded_image = ImageTk.PhotoImage(loaded_image)
    image_label = Label(self.frame_3, image=loaded_image, width=self.get_responsive_width(0.5), height=self.get_responsive_height(0.7))
    image_label.image = loaded_image
    image_label.grid(row=0, column=0)


  def frame4(self):
    self.frame_4 = Frame(self.window, width=int(self.window_width * 0.5), height=int(self.window_height * 0.7))
    self.frame_4.grid(row=1, column=1)

    edited_image = Image.open(r".\images\default_image.jpg")
    #why -5, ask to asim:)
    edited_image.thumbnail((self.get_responsive_width(0.5), self.get_responsive_height(0.7)))    
    edited_image = ImageTk.PhotoImage(edited_image)
    image_label = Label(self.frame_4, image=edited_image, width=self.get_responsive_width(0.5), height=self.get_responsive_height(0.7))
    image_label.image = edited_image
    image_label.grid(row=0, column=0)

  def load_image(self):
    image_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetypes=(("JPG file", ".jpg"), ("PNG file", ".png")))
    self.frame3(image_path)

  def get_window_size(self):
    self.window_width = self.window.winfo_screenwidth()
    self.window_height = self.window.winfo_screenheight()

  def get_responsive_width(self, ratio):
    return int(self.window_width * ratio)

  def get_responsive_height(self, ratio):
    return int(self.window_height * ratio)

  def main(self):
    self.window.title("PIXDEER IMAGE EDITOR")
    self.window.mainloop()