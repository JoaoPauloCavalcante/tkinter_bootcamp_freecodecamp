from tkinter import *

'''
Tkinter is all about placing widgets on a window. First you define the widget and then you place it on the main window.
'''

root = Tk()

# Creating a label widget
my_label = Label(root, text='Hello, world!')

# Placing the widget on the window
my_label.pack()

root.mainloop()