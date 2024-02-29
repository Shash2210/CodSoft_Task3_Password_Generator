#!/usr/bin/env python
# coding: utf-8

# In[6]:


from tkinter import *
from tkinter import messagebox
import random
import string

def passwordGen():
    try:
        length = int(entry.get())
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please Enter an Integer")
        return
    if length <= 0:
        messagebox.showwarning("Invalid Length", "Please enter a valid password length.")
        return

    lowercase = string.ascii_lowercase if lowercase_var.get() else ''
    uppercase = string.ascii_uppercase if uppercase_var.get() else ''
    digits = string.digits if numbers_var.get() else ''
    special_characters = string.punctuation if special_var.get() else ''

    character_set = lowercase + uppercase + digits + special_characters

    if not character_set:
        messagebox.showwarning("No Character Set Selected", "Please select at least one CheckBox.")
        return

    password = ''.join(random.choices(character_set, k=length))

    result_label.config(text=f"Generated Password: {password}",font=("Helvetica", 14))

def show_frame2():
    frame1.pack_forget()
    frame2.pack(side='top')

def exitgen():
    exit_confirmation = messagebox.askyesno("Exit Password Generator", "Do you really want to exit?")
    if exit_confirmation:
        root.destroy()
    

root = Tk()
root.title("Password Generator")
root.geometry("570x600")

frame1=Frame(root)
frame1.pack()

label = Label(frame1, text="Welcome to Password Generator!",font=("Helvetica", 16))
label.pack(pady=(100,50))
b=Button(frame1,text="Begin",command=show_frame2,font=("Helvetica", 16))
b.pack(pady=30)

exit1=Button(frame1, text="Exit",command=exitgen,font=("Helvetica", 16))
exit1.pack()

frame2=Frame(root)

notelabel =Label(frame2, text="Note: It's secure to have a password of length greater than 8",font=("Helvetica", 15),fg='red')
notelabel.pack(side="top",pady=(80,0))

length_label =Label(frame2, text="Please enter the length of Password:",font=("Helvetica", 14))
length_label.pack(pady=(30,10))

entry=Entry(frame2, font=("Helvetica", 14))
entry.pack(side='top')
entry_text="Password Length"
entry.insert(0,entry_text)


def on_entry_click(event):
    if entry.get() == entry_text:
        entry.delete(0, END)
        
entry.bind("<FocusIn>", on_entry_click)

frame3=Frame(frame2)
frame3.pack(pady=20)
lowercase_var = BooleanVar()
lowercase_checkbox = Checkbutton(frame3, text="Include Lowercase", font=("Helvetica", 14), variable=lowercase_var)
lowercase_checkbox.pack()

uppercase_var = BooleanVar()
uppercase_checkbox = Checkbutton(frame3, text="Include Uppercase", font=("Helvetica", 14), variable=uppercase_var)
uppercase_checkbox.pack()

numbers_var = BooleanVar()
numbers_checkbox = Checkbutton(frame3, text="Include Numbers", font=("Helvetica", 14), variable=numbers_var)
numbers_checkbox.pack()

special_var = BooleanVar()
special_checkbox = Checkbutton(frame3, text="Include Special Characters",font=("Helvetica", 14), variable=special_var)
special_checkbox.pack(padx=5)

generate_button = Button(frame3, text="Generate Password", font=("Helvetica", 14), command=passwordGen)
generate_button.pack(pady=(20,10))

result_label = Label(frame3, text="",fg='blue')
result_label.pack(pady=10)

exit2=Button(frame3, text="Exit",command=exitgen,font=("Helvetica", 14))
exit2.pack()

root.mainloop()






# In[ ]:




