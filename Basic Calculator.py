# Basic Calculator using Basic Calculator

# Importing required libraries
from tkinter import *

expression = ""


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def clear():
    global expression
    expression = ""
    equation.set(expression)


def equal():
    global expression
    result = str(eval(expression))
    equation.set(result)
    expression = ""


if __name__ == '__main__':
    # Creating Window
    window = Tk()

    # Giving Title
    window.title("Basic Calculator")

    # Applying Geometry
    window.geometry("325x328")
    window.resizable(0, 0)

    # Adding Background Color
    window.configure(background='#fdffcf')

    # Creating instances of StringVara()
    equation = StringVar()

    # Creating a Frame for the Input Field
    input_frame = Frame(window, width=316, height=272.5, bd=0, highlightbackground='black', highlightcolor='black')
    input_frame.pack(side='top', pady=2, padx=2)

    # Creating a Input Field inside Frame
    input_field = Entry(input_frame, font='arial 20', textvariable=equation, width=40, bg='#FFF', bd=0,
                        borderwidth=1)
    input_field.grid(row=0, column=0)
    input_field.pack(padx=1)

    # Creating another Frame for Button
    btn_frame1 = Frame(window, width=316, height=272.5, bg='#dfffcf')
    btn_frame1.pack(pady=1)
    btn_frame2 = Frame(window, width=316, height=272.5, bg='#dfffcf')
    btn_frame2.pack(pady=1)
    btn_frame3 = Frame(window, width=316, height=272.5, bg='#dfffcf')
    btn_frame3.pack(pady=1)

    # First Row
    clear = Button(btn_frame1, text="C", fg='black', width=33, height=3, bd=0, bg='#fff', cursor='hand2', command=clear,
                   borderwidth=1)
    clear.grid(row=2, column=0, padx=1, pady=1)
    divide = Button(btn_frame1, text="/", fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
                    command=lambda: press('/'), borderwidth=1)
    divide.grid(row=2, column=1, padx=1, pady=1)

    # Second Row
    seven = Button(btn_frame2, text="7", fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
                   command=lambda: press(7), borderwidth=1)
    seven.grid(row=3, column=0, padx=1, pady=1)
    eight = Button(btn_frame2, text="8", fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
                   command=lambda: press(8), borderwidth=1)
    eight.grid(row=3, column=1, padx=1, pady=1)
    nine = Button(btn_frame2, text="9", fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
                  command=lambda: press(9), borderwidth=1)
    nine.grid(row=3, column=2, padx=1, pady=1)
    mul = Button(btn_frame2, text="x", fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
                 command=lambda: press('*'), borderwidth=1)
    mul.grid(row=3, column=3, padx=1, pady=1)

    # Third Row
    four = Button(btn_frame2, text="4", fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
                  command=lambda: press(4), borderwidth=1)
    four.grid(row=4, column=0, padx=1, pady=1)
    five = Button(btn_frame2, text="5", fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
                  command=lambda: press(5), borderwidth=1)
    five.grid(row=4, column=1, padx=1, pady=1)
    six = Button(btn_frame2, text="6", fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
                 command=lambda: press(6), borderwidth=1)
    six.grid(row=4, column=2, padx=1, pady=1)
    add = Button(btn_frame2, text="+", fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
                 command=lambda: press('+'), borderwidth=1)
    add.grid(row=4, column=3, padx=1, pady=1)

    # Fourth Row
    one = Button(btn_frame2, text="1", fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
                 command=lambda: press(1), borderwidth=1)
    one.grid(row=5, column=0, padx=1, pady=1)
    two = Button(btn_frame2, text="2", fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
                 command=lambda: press(2), borderwidth=1)
    two.grid(row=5, column=1, padx=1, pady=1)
    three = Button(btn_frame2, text="3", fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
                   command=lambda: press(3), borderwidth=1)
    three.grid(row=5, column=2, padx=1, pady=1)
    minus = Button(btn_frame2, text="-", fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
                   command=lambda: press('-'), borderwidth=1)
    minus.grid(row=5, column=3, padx=1, pady=1)

    # Fifth Row
    zero = Button(btn_frame3, text="0", fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
                  command=lambda: press(0), borderwidth=1)
    zero.grid(row=6, column=0, padx=1, pady=1)
    dot = Button(btn_frame3, text=".", fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
                 command=lambda: press('.'), borderwidth=1)
    dot.grid(row=6, column=1, padx=1, pady=1)
    equal = Button(btn_frame3, text="=", fg='black', width=21, height=3, bd=0, bg='#fff', cursor='hand2',
                   command=equal, borderwidth=1)
    equal.grid(row=6, column=3, padx=3, pady=1)

    # Executing main loop
    window.mainloop()
