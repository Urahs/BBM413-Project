import tkinter as tk
from tkinter import Frame, Label, Canvas
from PIL import Image, ImageTk

class GUI:
  def __init__(self):
    self.window = tk.Tk()
    self.window.state("zoomed")
    self.window.resizable(False, False)
    self.get_window_size()
    self.frame1()
    self.frame2()
    self.frame3()
    self.frame4()
  
  def frame1(self):
    self.frame_1 = Frame(self.window, width=int(self.window_width * 0.5), height=int(self.window_height * 0.3), bg="red")
    self.frame_1.grid(row=0, column=0)

  def frame2(self):
    self.frame_2 = Frame(self.window, width=int(self.window_width * 0.5), height=int(self.window_height * 0.3), bg="purple")
    self.frame_2.grid(row=0, column=1)
  
  def frame3(self):
    #ADD frame_3 TO window<
    self.frame_3 = Frame(self.window,  width=int(self.window_width * 0.5), height=int(self.window_height * 0.7))
    self.frame_3.grid(row=1, column=0)
    #ADD frame_3 TO window>

    loaded_image = Image.open(r"C:\Users\MONSTER\OneDrive\Pictures\Screenshots\rooooot.jpg")
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