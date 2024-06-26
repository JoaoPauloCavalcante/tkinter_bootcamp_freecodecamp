from tkinter import *

root = Tk()
root.title('Simple Calculator')

entry = Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current_value = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current_value) + str(number))

def button_clear():
    entry.delete(0, END)

def button_add():
    first_number = entry.get()
    global first_num
    global math
    math = 'addition'
    first_num = int(first_number)
    entry.delete(0, END)
    
def button_equal():
    second_number = entry.get()
    entry.delete(0,END)
    
    if math == 'addition':
        entry.insert(0,first_num + int(second_number))
    elif math == 'subtraction':
        entry.insert(0,first_num - int(second_number))
    elif math == 'multiplication':
        entry.insert(0,first_num * int(second_number))
    elif math == 'division':
        entry.insert(0,first_num / int(second_number))

def button_subtract():
    first_number = entry.get()
    global first_num
    global math
    math = 'subtraction'
    first_num = int(first_number)
    entry.delete(0, END)

def button_multiply():
    first_number = entry.get()
    global first_num
    global math
    math = 'multiplication'
    first_num = int(first_number)
    entry.delete(0, END)

def button_divide():
    first_number = entry.get()
    global first_num
    global math
    math = 'division'
    first_num = int(first_number)
    entry.delete(0, END)

# Defining buttons:

button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))
button_addition = Button(root, text='+',padx=39, pady=20, command=button_add)
button_equal = Button(root, text='=',padx=91, pady=20, command=button_equal)
button_clear = Button(root, text='Clear',padx=79, pady=20, command=button_clear)

button_subtraction = Button(root, text='-',padx=41, pady=20, command=button_subtract)
button_multiplication = Button(root, text='*',padx=40, pady=20, command=button_multiply)
button_division = Button(root, text='/',padx=40, pady=20, command=button_divide)

# Positioning the buttons on the screen:
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)

button_clear.grid(row=4, column=1, columnspan=2)
button_addition.grid(row=5, column=0)
button_equal.grid(row=5, column=1,columnspan=2)

button_subtraction.grid(row=6,column=0)
button_multiplication.grid(row=6,column=1)
button_division.grid(row=6,column=2)

root.mainloop()