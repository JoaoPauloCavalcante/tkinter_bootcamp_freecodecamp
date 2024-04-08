from tkinter import *

root = Tk()

entry = Entry(root, width=50, borderwidth=3, fg='black', bg='#999999')
entry.pack()
entry.insert(0, 'Enter Your Name') # This command sets the default text of the entry box.

def my_click():
    hello = 'Hello, ' + entry.get() + '!'
    my_label = Label(root, text=hello)
    my_label.pack()

my_button = Button(root,text='Enter Your Name', command=my_click, fg='white', bg='black')
my_button.pack()

root.mainloop()