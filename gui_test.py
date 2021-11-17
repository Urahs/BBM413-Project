import tkinter as tk
from tkinter import Frame, Label

class GUI:
  def __init__(self):
    self.window = tk.Tk()
    self.window.state("zoomed")
    self.get_window_size()
    self.frame1()
    self.frame2()
    self.frame3()
    self.frame4()
  
  def frame1(self):
    self.frame1 = Frame(self.window, width=int(self.window_width * 0.5), height=int(self.window_height * 0.3), bg="red")
    self.frame1.grid(row=0, column=0)

  def frame2(self):
    self.frame2 = Frame(self.window, width=int(self.window_width * 0.5), height=int(self.window_height * 0.3), bg="purple")
    self.frame2.grid(row=0, column=1)
  
  def frame3(self):
    self.frame3 = Frame(self.window, width=int(self.window_width * 0.5), height=int(self.window_height * 0.7), bg="blue")
    self.frame3.grid(row=1, column=0)

  def frame4(self):
    self.frame4 = Frame(self.window, width=int(self.window_width * 0.5), height=int(self.window_height * 0.7), bg="green")
    self.frame4.grid(row=1, column=1)

  def get_window_size(self):
    self.window_width = self.window.winfo_screenwidth()
    self.window_height = self.window.winfo_screenheight()

  # def load_layout_1(self):


  def main(self):
    self.window.title("PIXDEER IMAGE EDITOR")
    self.window.mainloop()