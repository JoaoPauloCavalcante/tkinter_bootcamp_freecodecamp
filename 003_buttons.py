from tkinter import *

root = Tk()

def my_click():
    my_label = Label(root, text='Look! I clicked a button!')
    my_label.pack()

my_button = Button(root,text='Click me!', command=my_click, fg='white', bg='black')
my_button.pack()

root.mainloop()