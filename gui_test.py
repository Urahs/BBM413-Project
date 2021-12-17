import tkinter as tk
from tkinter import Button, Entry, Frame, IntVar, Label, LabelFrame, Radiobutton, filedialog, Scale
from tkinter.constants import HORIZONTAL
from typing import Text
from PIL import Image, ImageTk
import os

from functions import grayscale, reverse_color, mirror, flip, brightness, contrast, sharpness, saturation, rotation, noise, crop, blur, edge_detection, color_balance
from tkinter.filedialog import asksaveasfile

class GUI:
  def __init__(self):
    self.window = tk.Tk()
    self.window.resizable(False, False)
    self.window.state("zoomed")
    self.window.resizable(False, False)
    self.get_window_size()
    self.loaded_image = None
    self.edited_image = None
    self.temp_image = None
    self.frame2Tools = ["sharpness", "saturation", "rotation", "brightness", "contrast", "noise"] 
    self.frame1()
    self.frame2("none")
    self.frame3(self.loaded_image)
    self.frame4(self.edited_image)
    
    self.load_file_types = [('All Files', '*.*'), ("JPG file", ".jpg"), ("PNG file", ".png"), ("JPEG file", ".jpeg")]
    self.save_file_types = [("JPG file", ".jpg"), ("PNG file", ".png"), ("JPEG file", ".jpeg")]
    self.sliderValue = 0
    self.radio_var = IntVar()

  
  def frame1(self):
    self.frame_1 = Frame(self.window, width=int(self.window_width * 0.5), height=int(self.window_height * 0.3))
    self.frame_1.grid()
    
    self.frame_internal_file = LabelFrame(self.frame_1, text="File Operations")
    self.frame_internal_file.grid(row=0, column=0)

    self.frame_internal_process = LabelFrame(self.frame_1, text="Image Process")
    self.frame_internal_process.grid(row=0, column=1, padx=(int(self.window_width * 0.05)))
    
    self.loadButton = Button(self.frame_internal_file, text="Load Image", command=self.load_image).grid(row=0, column=0, sticky="w")
    self.saveButton = Button(self.frame_internal_file, text="Save Image", command=self.save_image).grid(row=1, column=0, sticky="w")
    self.resetButton = Button(self.frame_internal_file, text="Reset Image", command=self.reset_image).grid(row=2, column=0, sticky="w")



    self.blurButton = Button(self.frame_internal_process, text="Blur Image", command=self.blur_image).grid(row=0, column=2, sticky="w")
    self.deblurButton = Button(self.frame_internal_process, text="Deblur Image", command=self.sharpness).grid(row=1, column=2, sticky="w")
    self.grayscaleButton = Button(self.frame_internal_process, text="Grayscale Image", command=self.grayscale_image).grid(row=2, column=2, sticky="w")
    self.cropButton = Button(self.frame_internal_process, text="Crop Image", command=self.crop).grid(row=3, column=2, sticky="w")
    self.flipButton = Button(self.frame_internal_process, text="Flip Image", command=self.flip).grid(row=4, column=2, sticky="w")
    self.mirrorButton = Button(self.frame_internal_process, text="Mirror Image", command=self.mirror).grid(row=5, column=2, sticky="w")
    self.rotateButton = Button(self.frame_internal_process, text="Rotate Image", command=self.rotation).grid(row=6, column=2, sticky="w")
    self.reverseColorButton = Button(self.frame_internal_process, text="Reverse Color Image", command=self.reverse_color_image).grid(row=7, column=2, sticky="w")
    self.changeColorBalanceButton = Button(self.frame_internal_process, text="Change Color Balance Image", command=self.color_balance).grid(row=8, column=2, sticky="w")



    self.brightButton = Button(self.frame_internal_process, text="Adjust Brightness of Image").grid(row=0, column=3, sticky="w")
    self.contrastButton = Button(self.frame_internal_process, text="Adjust Contrast of Image").grid(row=1, column=3, sticky="w")
    self.saturationButton = Button(self.frame_internal_process, text="Adjust Saturation of Image").grid(row=2, column=3, sticky="w")
    self.noiseButton = Button(self.frame_internal_process, text="Add Noise to Image").grid(row=3, column=3, sticky="w")
    self.brightButton = Button(self.frame_internal_process, text="Adjust Brightness of Image", command=self.brightness).grid(row=0, column=3, sticky="w")
    self.contrastButton = Button(self.frame_internal_process, text="Adjust Contrast of Image", command=self.contrast).grid(row=1, column=3, sticky="w")
    self.saturationButton = Button(self.frame_internal_process, text="Adjust Saturation of Image", command=self.saturation).grid(row=2, column=3, sticky="w")
    self.noiseButton = Button(self.frame_internal_process, text="Add Noise to Image", command=self.noise).grid(row=3, column=3, sticky="w")
    self.detectEdgesButton = Button(self.frame_internal_process, text="Detect Edges of Image", command=self.detected_edges_image).grid(row=4, column=3, sticky="w")


  def apply(self, val, condition):
    self.sliderValue = val
    if condition == "brightness":
      self.edited_image = brightness.brightness(self.temp_image, self.sliderValue)
    elif condition == "contrast":
      self.edited_image = contrast.contrast(self.temp_image, self.sliderValue)
    elif condition == "sharpness":
      self.edited_image = sharpness.sharpness(self.temp_image, self.sliderValue)
    elif condition == "saturation":
      self.edited_image = saturation.saturation(self.temp_image, self.sliderValue)
    elif condition == "noise":
      self.edited_image = noise.noise(self.temp_image, self.sliderValue, self.radio_var.get())
    elif condition == "rotation":
      self.edited_image = rotation.rotation(self.temp_image, self.sliderValue)
      

    self.frame4(self.edited_image)


  def apply_crop(self, x1, x2, y1, y2):

    # destroy the error mesage if it exists
    try:
      self.exception_label.grid_forget()
    except:
      None

    inputs = [x1, x2, y1, y2]

    # error detection part is here
    for i in inputs:
      try:
        val = int(i)    #if input is not string
        if val < 0:     #if input is smaller than 0
          val = 0/0     #to pass the exception part
        if i == inputs[0]:        #if x coordinate bounds are overlapping
          if val+int(inputs[1]) >= 100:
            val = 0/0
        elif i == inputs[2]:      #if x coordinate bounds are overlapping
          if val+int(inputs[3]) >= 100:
            val = 0/0
      except:
        self.exception_label = Label(self.frame_2_2, text="""Please enter a valid input
■ values must be greater than 0
■ values must be an integer
■ sum of the same coordinate values must be smaller than 100""", font=("Arial", 13), anchor="e")
        self.exception_label.grid()
        return

    self.edited_image = crop.crop(self.temp_image, inputs)
    self.frame4(self.edited_image)


  def frame2(self, condition):

    self.frame_2 = Frame(self.window, width=int(self.window_width * 0.5), height=int(self.window_height * 0.3))
    self.frame_2.grid(row=0, column=1)
    self.temp_image = self.edited_image

    if condition in self.frame2Tools:
      
      if condition == "noise":
        R1 = Radiobutton(self.frame_2, text="Gaussian", variable = self.radio_var, value=1)
        R1.grid()
        R2 = Radiobutton(self.frame_2, text="Speckle", variable = self.radio_var, value=2)
        R2.grid()
        R3 = Radiobutton(self.frame_2, text="Salt&Pepper", variable = self.radio_var, value=3)
        R3.grid()

      if condition == "rotation":
        slider = Scale(self.frame_2, from_=0, to=360, orient=HORIZONTAL, length=600, tickinterval=45)
      else:
        slider = Scale(self.frame_2, from_=0, to=100, orient=HORIZONTAL, length=600, tickinterval=100)
      
      slider.set(50)
      if condition == self.frame2Tools[0] or condition == self.frame2Tools[2]: # if condition is sharpness or rotation
        slider.set(0)
      if condition == self.frame2Tools[1]: # if condition is saturation
        slider.set(30)



      slider.grid()
        

      applyButton = Button(self.frame_2, text="Apply", command= lambda: self.apply(slider.get(), condition))
      applyButton.grid()

    
    elif condition == "crop":

      self.frame_2_1 = Frame(self.frame_2, width=int(self.window_width * 0.5), height=int(self.window_height * 0.3)/2)
      self.frame_2_1.grid()
      self.frame_2_2 = Frame(self.frame_2, width=int(self.window_width * 0.5), height=int(self.window_height * 0.3)/2)
      self.frame_2_2.grid()

      L1 = Label(self.frame_2_1, text="X coordinate from left")
      L1.grid(row=0, column=0)
      entryBox_x1 = Entry(self.frame_2_1, width=2)
      entryBox_x1.grid(row=0, column=1, padx=(5,0))

      L2 = Label(self.frame_2_1, text="X coordinate from right")
      L2.grid(row=0, column=3, padx=(50,0))
      entryBox_x2 = Entry(self.frame_2_1, width=2)
      entryBox_x2.grid(row=0, column=4, padx=(5,0))
    
      
      
      L3 = Label(self.frame_2_1, text="Y coordinate from top")
      L3.grid(row=1, column=0, pady=20)
      entryBox_y1 = Entry(self.frame_2_1, width=2)
      entryBox_y1.grid(row=1, column=1, padx=(5,0))

      L4 = Label(self.frame_2_1, text="Y coordinate from bottom")
      L4.grid(row=1, column=3, padx=(50,0))
      entryBox_y2 = Entry(self.frame_2_1, width=2)
      entryBox_y2.grid(row=1, column=4, padx=(5,0))


      applyButton = Button(self.frame_2_2, text="Apply", command= lambda: self.apply_crop(entryBox_x1.get(), entryBox_x2.get(), entryBox_y1.get(), entryBox_y2.get()))
      applyButton.grid()

    elif condition == "color_balance":
      slider_R = Scale(self.frame_2, from_=0, to=255, orient=HORIZONTAL, length=600, tickinterval=255, label="R VALUE")
      slider_G = Scale(self.frame_2, from_=0, to=255, orient=HORIZONTAL, length=600, tickinterval=255, label="G VALUE")  
      slider_B = Scale(self.frame_2, from_=0, to=255, orient=HORIZONTAL, length=600, tickinterval=255, label="B VALUE")
      slider_R.set(255)
      slider_G.set(255)
      slider_B.set(255)
      slider_R.grid()
      slider_G.grid()
      slider_B.grid()
      applyButton = Button(self.frame_2, text="Apply", command= lambda: self.apply_color_balance(slider_R.get(), slider_G.get(), slider_B.get()))
      applyButton.grid()
      
    
  def clear_old_frames(self):
    try:
      self.frame_2.grid_forget()
      self.frame_2_1.grid_forget()
      self.frame_2_2.grid_forget()
    except:
      None


  def frame3(self, image):
    #ADD frame_3 TO window<
    self.frame_3 = Frame(self.window,  width=int(self.window_width * 0.5), height=int(self.window_height * 0.7))
    self.frame_3.grid(row=1, column=0)
    #ADD frame_3 TO window>

    if image == None: image = Image.open(r".\images\default_image.jpg")
    image.thumbnail((self.get_responsive_width(0.5), self.get_responsive_height(0.7)))    
    image = ImageTk.PhotoImage(image)
    image_label = Label(self.frame_3, image=image, width=self.get_responsive_width(0.5), height=self.get_responsive_height(0.7))
    image_label.image = image
    image_label.grid(row=0, column=0)

  def frame4(self, image):
    #ADD frame_4 TO window>
    self.frame_4 = Frame(self.window, width=int(self.window_width * 0.5), height=int(self.window_height * 0.7))
    self.frame_4.grid(row=1, column=1)
    #ADD frame_4 TO window>

    if image == None: image = Image.open(r".\images\default_image.jpg")
    #why -5, ask to asim:)
    image.thumbnail((self.get_responsive_width(0.5), self.get_responsive_height(0.7)))    
    image = ImageTk.PhotoImage(image)
    image_label = Label(self.frame_4, image=image, width=self.get_responsive_width(0.5), height=self.get_responsive_height(0.7))
    image_label.image = image
    image_label.grid(row=0, column=0)

  def load_image(self): 
    image_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetypes = self.load_file_types)
    self.loaded_image = Image.open(image_path)
    self.edited_image = self.loaded_image.copy()
    self.frame3(self.loaded_image)
    self.frame2("none")

  def save_image(self):
    file = asksaveasfile(initialdir=os.getcwd(), title="Save Image", initialfile="resulted_image", filetypes = self.save_file_types, defaultextension = self.save_file_types)
    self.edited_image.save(file.name)

  def reset_image(self):
    self.clear_old_frames()
    self.edited_image = self.loaded_image.copy()
    self.frame4(self.edited_image)
    self.frame2("none")

  def grayscale_image(self):
    self.clear_old_frames()
    self.edited_image = grayscale.grayscale(self.edited_image)
    self.frame4(self.edited_image)
    self.frame2("none")

  def reverse_color_image(self):
    self.clear_old_frames()
    self.edited_image = reverse_color.reverse_color(self.edited_image)
    self.frame4(self.edited_image)
    self.frame2("none")
  
  def mirror(self):
    self.clear_old_frames()
    self.edited_image = mirror.mirror(self.edited_image)
    self.frame4(self.edited_image)
    self.frame2("none")

  def flip(self):
    self.clear_old_frames()
    self.edited_image = flip.flip(self.edited_image)
    self.frame4(self.edited_image)
    self.frame2("none")

  def brightness(self):
    self.clear_old_frames()
    self.frame2("brightness")

  def contrast(self):
    self.clear_old_frames()
    self.frame2("contrast")

  def sharpness(self):
    self.clear_old_frames()
    self.frame2("sharpness")
  
  def saturation(self):
    self.clear_old_frames()
    self.frame2("saturation")

  def crop(self):
    self.clear_old_frames()
    self.frame2("crop")

  def noise(self):
    self.clear_old_frames()
    self.frame2("noise")
  
  def rotation(self):
    self.clear_old_frames()
    self.frame2("rotation")

  def color_balance(self):
    self.clear_old_frames()
    self.frame2("color_balance")

  def apply_color_balance(self, sliderR_value, sliderG_value, sliderB_value):
    self.edited_image = color_balance.color_balance(self.temp_image, sliderR_value, sliderG_value, sliderB_value)
    self.frame4(self.edited_image)

  def blur_image(self):
    self.clear_old_frames()
    self.edited_image = blur.blur(self.edited_image)
    self.frame4(self.edited_image)
    self.frame2("none")

  def detected_edges_image(self):
    self.clear_old_frames()
    self.edited_image = edge_detection.edge_detection(self.edited_image)
    self.frame4(self.edited_image)
    self.frame2("none")

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