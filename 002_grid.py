from tkinter import *

root = Tk()

# Creating a label widget
my_label1 = Label(root, text='Hello, world!')
my_label2 = Label(root, text='Im JP!')

# Placing the widget on the window
my_label1.grid(row=0, column=0)
my_label2.grid(row=1, column=5)

root.mainloop()