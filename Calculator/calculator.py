from tkinter import *
import other



root = Tk()
root.title('CALCULATOR')
root.geometry('500x410+410+120')
root.resizable(False,False)
# root.minsize('500x410')
# root.maxsize('500x410')
root.config(bg='#ffcc99')

def calculate():
    try :
        evaluated = eval(other.expression)
        l1.config(text=evaluated)
        other.expression = ''
    except:
        l1.config(text='Wrong Format...')
        other.expression = ''

def btn1():
    msg = '1'
    l1.config(text=msg)
    other.expression += msg

    
def btn2():
    msg = '2'
    l1.config(text=msg)
    other.expression += msg

def btn3():
    msg = '3'
    l1.config(text=msg)
    other.expression += msg

def btn4():
    msg = '4'
    l1.config(text=msg)
    other.expression += msg

def btn5():
    msg = '5'
    l1.config(text=msg)
    other.expression += msg

def btn6():
    msg = '6'
    l1.config(text=msg)
    other.expression += msg

def btn7():
    msg = '7'
    l1.config(text=msg)
    other.expression += msg

def btn8():
    msg = '8'
    l1.config(text=msg)
    other.expression += msg

def btn9():
    msg = '9'
    l1.config(text=msg)
    other.expression += msg

def btn0():
    msg = '0'
    l1.config(text=msg)
    other.expression += msg

def plus():
    msg = '+'
    l1.config(text=msg)
    other.expression += msg
    

def minus():
    msg = '-'
    l1.config(text=msg)
    other.expression += msg

def mul():
    msg = '*'
    l1.config(text=msg)
    other.expression += msg

def div():
    msg = '/'
    l1.config(text=msg)
    other.expression += msg



l1 = Label(root, text='0', width=55, height=2, bg='#a0a0a0', borderwidth=3, border=3)
l1.pack(pady=30)

f = Frame(root, bg='#808080', width=400, height=400, borderwidth=5)
f.pack(pady=15)

b1 = Button(f, text='7', width=10, height=2, border=5, command=btn7)
b1.grid(row=0, column=0, padx=5, pady=5)

b2 = Button(f, text='8', width=10, height=2, border=5, command=btn8)
b2.grid(row=0, column=1, padx=5, pady=5)

b3 = Button(f, text='9', width=10, height=2, border=5, command=btn9)
b3.grid(row=0, column=2, padx=5, pady=5)

b4 = Button(f, text='4', width=10, height=2, border=5, command=btn4)
b4.grid(row=1, column=0, padx=5, pady=5)

b5 = Button(f, text='5', width=10, height=2, border=5, command=btn5)
b5.grid(row=1, column=1, padx=5, pady=5)

b6 = Button(f, text='6', width=10, height=2, border=5, command=btn6)
b6.grid(row=1, column=2, padx=5, pady=5)

b7 = Button(f, text='1', width=10, height=2, border=5, command=btn1)
b7.grid(row=2, column=0, padx=5, pady=5)

b8 = Button(f, text='2', width=10, height=2, border=5, command=btn2)
b8.grid(row=2, column=1, padx=5, pady=5)

b9 = Button(f, text='3', width=10, height=2, border=5, command=btn3)
b9.grid(row=2, column=2, padx=5, pady=5)

b10 = Button(f, text='*', width=10, height=2, border=5, command=mul)
b10.grid(row=3, column=0, padx=5, pady=5)

b11 = Button(f, text='0', width=10, height=2, border=5, command=btn0)
b11.grid(row=3, column=1, padx=5, pady=5)

b12 = Button(f, text='/', width=10, height=2, border=5, command=div)
b12.grid(row=3, column=2, padx=5, pady=5)

b13 = Button(f, text='+', width=10, height=2, border=5, command=plus)
b13.grid(row=0, column=3, padx=5, pady=5)

b14 = Button(f, text='-', width=10, height=2, border=5, command=minus)
b14.grid(row=1, column=3, padx=5, pady=5)

b15 = Button(root, text='=', width=10, height=5, border=5, pady=6, command=calculate)
b15.place(x=350, y=239)








root.mainloop()



