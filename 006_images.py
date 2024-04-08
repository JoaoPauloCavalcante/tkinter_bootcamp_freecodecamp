from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to code at Codemy.com')

my_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Joao Paulo\OneDrive\Área de Trabalho\Picture1.png"))
my_label = Label(image=my_img)
my_label.pack()


root.mainloop()