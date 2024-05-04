from random import *
from tkinter import *

def generate():
    # global pw
    no_of_chars = no_of_char_ent.get()

    try:
        no_of_chars = int(no_of_chars) 
        pw = "".join(chr(randint(33, 126)) for _ in range(no_of_chars))
        lf2_label.config(state=NORMAL)
        lf2_label.delete(0, END)
        lf2_label.insert(0, pw)
        lf2_label.config(state='readonly')

    except ValueError:
        lf2_label.config(state=NORMAL)
        lf2_label.delete(0, END)  
        lf2_label.insert(0, "Invalid input!")
        lf2_label.config(state='readonly')



r = Tk()
r.geometry("450x300")
r.resizable(False,False)
r.configure(background='gray')

bg_img = PhotoImage(file="bg.png")
bg_label = Label( r , image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

lf1 = LabelFrame( r , text="      No of characters of your password" , bg="#05002D" , fg="white", font=("Arial bold", 12) , border=0 , height=400 , width=225)
lf1.place( relwidth= 0.7, relheight= 0.4, relx=0.5, rely=0.35 ,  anchor=CENTER )

no_of_char_ent = Entry( lf1  , border=0  , font=("Arial", 12) )
no_of_char_ent.pack(pady=15)

lf1_button = Button(lf1 , text="Generate" , bg="#000239", fg="white", font=("Arial", 12), command=generate )
lf1_button.pack()


lf2 = LabelFrame( r , text="                  Generated Password" , bg="#05002D" , fg="white", font=("Arial bold", 12) , height=400 , width=225 , border=0)
lf2.place( relwidth= 0.7, relheight= 0.25, relx=0.5, rely=0.72 ,  anchor=CENTER )

lf2_label = Entry( lf2 , font=("Arial", 12) , state='readonly' )
lf2_label.pack()


r.mainloop()

