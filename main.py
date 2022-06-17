#To-do App on Tkinter GUI using Python 3

from colorama import Fore
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from time import sleep



tkinter = Tk()
tkinter.title("To-do App")
tkinter.geometry("480x500")
tkinter.configure(background='grey')


URL = ('/Users/mehmetkahya/Desktop/To-do/db.txt')
#Set the font of the listbox
def set_font():
    listbox.config(font='arial black'.get())



#Companents of the To-do App
Entry = ttk.Entry(tkinter, width=30)
Entry.pack()
Entry.insert(0, "Enter your To-do")
Entry.place(x=25, y=40)

Button = ttk.Button(tkinter, text="Add")
Button.pack()
Button.place(x=323, y=40)
Button.place(width=100, height=25)

listbox = Listbox(tkinter, width=30)
listbox.pack()
listbox.place(x=25, y=80)
listbox.place(width=400, height=300)



#add the txt file datas to the listbox
def load_items():
    with open(URL, 'r') as f:
        for line in f:
            listbox.insert(END, line)
        f.close()
        print("Loaded")
    messagebox.showinfo("Loaded", "Loaded")
            
  
#Create load button
load_button = ttk.Button(tkinter, text="Load", command=load_items)
load_button.place(x=323, y=110)
load_button.place(width=100, height=25)

#Selected listbox item deleting from the listbox and txt file
def delete_item():
    listbox.delete(listbox.curselection())
    with open(URL, 'r') as f:
        lines = f.readlines()
    with open(URL, 'w') as f:
        for line in lines:
            if line != listbox.get(listbox.curselection()) + '\n':
                f.write(line)

    messagebox.showinfo("Deleted", "Deleted")
            
  

deleteButton = ttk.Button(tkinter, text="Delete", command=delete_item)
deleteButton.pack()
deleteButton.place(x=323, y=80)
deleteButton.place(width=100, height=25)




#To get the value of the entry box and print the listbox
def get_entry():
    listbox.insert(END, Entry.get())
    Entry.delete(0, END)
Button.configure(command=get_entry)



#Listbox item saving the txt file
def save_item():
    with open(URL, 'a') as f:
        f.write(listbox.get(listbox.curselection()) + '\n')
        print(listbox.get(listbox.curselection()))
        print("Saved")
        messagebox.showinfo("Saved", "Saved")
            



saveButton = ttk.Button(tkinter, text="Save", command=save_item)
saveButton.pack()
saveButton.place(x=323, y=140)
saveButton.place(width=100, height=25)

tkinter.mainloop()
