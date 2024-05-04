from tkinter import *
from tkinter.messagebox import *
import os


def clear_frame():
    for widget in frame.winfo_children():
        widget.destroy()

def back_to_options():
    clear_frame()
    options()


def options():
    global b1,b2,b3,b4,b5

    options_frame = Frame(frame, bg="#00004f")

    b1 = Button(options_frame, text="Add a Contact", command=add_contact , bg="#000239", fg="white", font=("Arial", 15))
    b1.place(relx=0.5, rely=0.15, anchor=CENTER)

    b2 = Button(options_frame, text="View Contact List" , command=view_contacts , bg="#000239", fg="white", font=("Arial", 15))
    b2.place(relx=0.5, rely=0.30, anchor=CENTER)

    b3 = Button(options_frame, text="Search Contact" , command=search_contact ,bg="#000239", fg="white", font=("Arial", 15))
    b3.place(relx=0.5, rely=0.45, anchor=CENTER)

    b4 = Button(options_frame, text="Update a Contact" , command=update, bg="#000239", fg="white", font=("Arial", 15))
    b4.place(relx=0.5, rely=0.60, anchor=CENTER)

    b5 = Button(options_frame, text="Delete a Contact" ,command=delete , bg="#000239", fg="white", font=("Arial", 15))
    b5.place(relx=0.5, rely=0.75, anchor=CENTER)


    options_frame.pack(fill=BOTH, expand=True)



def add_contact():

    clear_frame()


    add_contact_frame = Frame(frame, bg="#00004f")

    global bc1, bc2, bc3, bc4

    c1 = Label(add_contact_frame, text="Name:", bg="#000239", fg="white", font=("Arial", 15))
    c1.place(relx=0.5, rely=0.05, anchor=CENTER)
    
    bc1 = Entry(add_contact_frame)
    bc1.place(relx=0.5, rely=0.12, anchor=CENTER)

    c2 = Label(add_contact_frame, text="Phone Number:", bg="#000239", fg="white", font=("Arial", 15))
    c2.place(relx=0.5, rely=0.20, anchor=CENTER)
    
    bc2 = Entry(add_contact_frame)
    bc2.place(relx=0.5, rely=0.27, anchor=CENTER)

    c3 = Label(add_contact_frame, text="Email:", bg="#000239", fg="white", font=("Arial", 15))
    c3.place(relx=0.5, rely=0.35, anchor=CENTER)
    
    bc3 = Entry(add_contact_frame)
    bc3.place(relx=0.5, rely=0.42, anchor=CENTER)

    c4 = Label(add_contact_frame, text="Address:", bg="#000239", fg="white", font=("Arial", 15))
    c4.place(relx=0.5, rely=0.50, anchor=CENTER)
    
    bc4 = Entry(add_contact_frame)
    bc4.place(relx=0.5, rely=0.57, anchor=CENTER)



    add_button = Button(add_contact_frame, text="Add" , bg="#000239", fg="white", font=("Arial", 15) , command=add_to_database)
    add_button.place(relx=0.5 , rely=0.7 , anchor=CENTER)

    back_button = Button(add_contact_frame, text="Back to Options", command=back_to_options, bg="#000239", fg="white", font=("Arial", 15))
    back_button.pack(anchor="s" , side=BOTTOM)


    add_contact_frame.pack(fill=BOTH, expand=True)



def add_to_database():
    name = bc1.get()
    phone_number = bc2.get()
    email = bc3.get()
    address = bc4.get()



    if name.strip() == "" or phone_number.strip() == "" or email.strip() == "" or address.strip() == "":
        showwarning(title="Error", message="Fields can not be empty!")
        return

    if not phone_number.isdigit():
        showwarning(title="Error", message="Phone number can not contain alphabetic characters!")
        return
    
    if '@' not in email or '.' not in email:
        showwarning(title="Error", message="Email format not correct!")
        return


    with open ("database.csv" , "a+") as f:
        f.seek(0)
        f_read = f.readlines()

        numbers_list = []

        for i in f_read:
            name_read , number_read , email_read , address_read = i.split(",")
            numbers_list.append(number_read)

        for num in numbers_list:
            if num == phone_number:
                showwarning(title="Error", message="Phone number already exists!")
                return
            
        f.seek(0, os.SEEK_END)

        f.write(f"{name},{phone_number},{email},{address}\n")
        showinfo(title="Successful" , message="Contact added successfully!")



def view_contacts():

    clear_frame()


    view_contact_frame = Frame(frame, bg="#00004f")

    back_button = Button(view_contact_frame, text="Back to Options", command=back_to_options, bg="#000239", fg="white", font=("Arial", 15))

    back_button.pack(anchor="s" , side=BOTTOM)


    scroller = Scrollbar ( view_contact_frame )
    scroller.pack(side = RIGHT, fill=Y)

    con_list = Listbox(view_contact_frame, yscrollcommand=scroller.set, bg="#00004f", fg="white", font=("Arial", 10) , bd=0)

    scroller.config( command = con_list.yview )

    con_list.pack(side=LEFT, fill=BOTH, expand=True )

    with open("database.csv", "r") as f:
        for line in f:
            name, phone_number, email, address = line.strip().split(",")
            contact_info = f"Name: {name}, Phone: {phone_number}, Email: {email}, Address: {address}"
            con_list.insert(END, contact_info)

    view_contact_frame.pack(fill=BOTH , expand=True)



def search_contact():
    clear_frame()


    global search_entry, search_label , search_button , search_contact_frame

    search_contact_frame = Frame(frame, bg="#00004f")

    back_button = Button(search_contact_frame, text="Back to Options", command=back_to_options, bg="#000239", fg="white", font=("Arial", 15))
    back_button.pack(side=BOTTOM)

    



    search_label = Label(search_contact_frame, text="Name:", bg="#000239", fg="white", font=("Arial", 15))
    search_label.place(relx=0.5, rely=0.23, anchor=CENTER)
    
    search_entry = Entry(search_contact_frame)
    search_entry.place(relx=0.5, rely=0.33, anchor=CENTER)



    search_button = Button(search_contact_frame, text="Search" , bg="#000239", fg="white", font=("Arial", 15) , command=search_from_database)
    search_button.place(relx=0.5 , rely=0.43 , anchor=CENTER)


    search_contact_frame.pack(fill=BOTH , expand=True)


    
def search_from_database():
    search_entry.pack_forget()
    search_label.pack_forget() 
    search_button.pack_forget()


    contact_name = search_entry.get()

    found = False

    if hasattr(search_contact_frame, "contact_label"):
        search_contact_frame.contact_label.destroy()


    with open("database.csv", "r") as f:
        for line in f:
            name, _, _, _ = line.strip().split(",")
            if contact_name == name:
                contact_found = Label(search_contact_frame, text=line, bg="#00004f", fg="white", font=("Arial", 8))
                contact_found.place(relx=0.5 , rely=0.54 ,anchor=CENTER)
                found = True
                search_contact_frame.contact_label = contact_found
                break

    if not found:
        showinfo(title="Unsuccessful" , message="No contact found!")
        return




def update():
    clear_frame()

    global update_contact_frame

    update_contact_frame = Frame(frame, bg="#00004f")
    update_contact_frame.pack(fill=BOTH , expand=True)


    global search_entry2, search_label2 , search_button2

    search_label2 = Label(update_contact_frame, text="Search the contact by phone number:", bg="#000239", fg="white", font=("Arial", 14))
    search_label2.pack()

    search_entry2 = Entry(update_contact_frame)
    search_entry2.pack(pady=20)

    search_button2 = Button(update_contact_frame, text= "Search" , bg="#000239", fg="white", font=("Arial", 15) , command=update_from_database)
    search_button2.pack()


    back_button = Button(update_contact_frame, text="Back to Options", command=back_to_options, bg="#000239", fg="white", font=("Arial", 15))
    back_button.pack(side=BOTTOM)






def update_from_database():
    global  search_entry2, search_label2, search_button2, phone_given_to_update

    

    phone_update = search_entry2.get()
    found = False


    contact_to_update = []

    with open("database.csv", "r") as f:
        for line in f:
            details = line.strip().split(',')
            if phone_update == details[1]:
                phone_given_to_update = line
                contact_to_update.append(phone_given_to_update)
                found = True
                update_options()
                break

    if not found:
        showinfo(title="Unsuccessful" , message="No contact found!")
        return





def update_options():

    clear_frame()


    update_options_frame = Frame(frame, bg="#00004f")

    global name_f , phone_f , email_f , address_f, cont_details , ph_upd_list

    ph_upd_list = phone_given_to_update.split(',')

    cont_details = ph_upd_list
    

    back_button = Button(update_options_frame, text="Back to Options", command=back_to_options, bg="#000239", fg="white", font=("Arial", 15))
    back_button.pack(side=BOTTOM)


    name_up = Label(update_options_frame, text="Name:", bg="#000239", fg="white", font=("Arial", 15))
    name_up.place(relx=0.5, rely=0.10, anchor=CENTER)
    
    name_f = Entry(update_options_frame)
    name_f.place(relx=0.5, rely=0.18, anchor=CENTER)

    phone_up = Label(update_options_frame, text="Phone Number:", bg="#000239", fg="white", font=("Arial", 15))
    phone_up.place(relx=0.5, rely=0.25, anchor=CENTER)
    
    phone_f = Entry(update_options_frame)
    phone_f.place(relx=0.5, rely=0.33, anchor=CENTER)

    email_up = Label(update_options_frame, text="Email:", bg="#000239", fg="white", font=("Arial", 15))
    email_up.place(relx=0.5, rely=0.40, anchor=CENTER)
    
    email_f = Entry(update_options_frame)
    email_f.place(relx=0.5, rely=0.48, anchor=CENTER)

    address_up = Label(update_options_frame, text="Address:", bg="#000239", fg="white", font=("Arial", 15))
    address_up.place(relx=0.5, rely=0.55, anchor=CENTER)
    
    address_f = Entry(update_options_frame)
    address_f.place(relx=0.5, rely=0.63, anchor=CENTER)



    update_now = Button(update_options_frame, text="Update" , bg="#000239", fg="white", font=("Arial", 15) , command=update_fields_now )
    update_now.place(relx=0.5 , rely=0.75 , anchor=CENTER)


    update_options_frame.pack(fill=BOTH , expand=True)

def update_fields_now():
    name_given = name_f.get()
    phone_given = phone_f.get()
    email_given = email_f.get()
    address_given = address_f.get()

    if name_given.strip() == "" or phone_given.strip() == "" or email_given.strip() == "" or address_given.strip() == "":
        showwarning(title="Error", message="Fields cannot be empty!")
        return

    if not phone_given.isdigit():
        showwarning(title="Error", message="Phone number cannot contain alphabetic characters!")
        return
    
    if '@' not in email_given or '.' not in email_given:
        showwarning(title="Error", message="Email format is not correct!")
        return


    updated_contact_info = f"{name_given},{phone_given},{email_given},{address_given}"



    updated_lines = []
    with open("database.csv", "r") as f:
        for line in f:
            details = line.strip().split(',')
            if details[1] == ph_upd_list[1]:
                updated_lines.append(updated_contact_info + '\n')
            else:
                updated_lines.append(line)


    with open("database.csv", "w") as f:
        f.writelines(updated_lines)

    showinfo(title="Successful", message="Contact updated successfully!")




def delete():
    clear_frame()



    delete_frame = Frame(frame, bg="#00004f")

    global delete_button, delete_entry , delete_label

    back_button = Button(delete_frame, text="Back to Options", command=back_to_options, bg="#000239", fg="white", font=("Arial", 15))
    back_button.pack(anchor="s" , side=BOTTOM)

    delete_label = Label(delete_frame, text="Search the contact by phone number:", bg="#000239", fg="white", font=("Arial", 14))
    delete_label.pack()
    
    delete_entry = Entry(delete_frame)
    delete_entry.pack(pady=20)

    delete_button = Button(delete_frame, text= "Delete" , bg="#000239", fg="white", font=("Arial", 15) , command=delete_now)
    delete_button.pack()

    
    delete_frame.pack(fill=BOTH , expand=True)



def delete_now():
    contact_to_delete = delete_entry.get()
    contact_found = False
    updated_contacts = []



    with open("database.csv", "r") as f:
        for line in f:
            contacts = line.strip().split(',')

            if contacts[1] == contact_to_delete:
                contact_found = True
            else:
                updated_contacts.append(line) 

    if not contact_found:
        showinfo(title="Unsuccessful", message="Contact not found!")
        return

    with open("database.csv", "w") as f:
        f.writelines(updated_contacts)

    showinfo(title="Successful", message="Contact deleted successfully!")




 







r = Tk()
r.title("My Contact Book")
r.geometry("400x500")
r.config(bg="#00004f")


bg_cb = PhotoImage(file="cb.png" )
img_bg = Label(r , image=bg_cb , borderwidth=0)
img_bg.pack()

frame = Frame(r, bg="#00004f")
frame.pack(fill=BOTH, expand=True)


options()

r.mainloop()