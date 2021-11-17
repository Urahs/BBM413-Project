import tkinter as tk


class GUI:
  def __init__(self):
    self.window = tk.Tk()
    self.window.state("zoomed")
    self.window_width = self.window.winfo_screenwidth()
    self.window_height = self.window.winfo_screenheight()
    self.greeting = tk.Label(text="Hello, Tkinter" + str(self.window_width ))
    self.greeting.pack()
    self.window.title("PIXDEER IMAGE EDITOR")
    self.window.mainloop()