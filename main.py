import pickle
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from tkinter import filedialog
import pickle


root = Tk()
root.geometry('750x500')
frame = Frame(root)
my_font = Font(font = ('Arial', 10, 'bold'))
lb = Listbox(frame, font=('Arial', 14, 'bold'), fg = 'red', bg = 'black', height=5,width=15, border=0, highlightthickness=0,  activestyle= 'none')
sb_v = Scrollbar(frame)
sb_h = Scrollbar(frame, orient= 'horizontal')

l = Label(root,font= ('Arial', 14, 'bold'), fg = 'Red',bg = 'black',  text = 'Todo App')
button_frame = Frame(root)
entry_box = Entry(root, font=('Arial', 12, 'bold'), fg = 'red', bg = 'black', )
var = IntVar()


def add_func():
    task = entry_box.get()
    if task != "":
        lb.insert(END, task)
        entry_box.delete(0, END)
    else:
        messagebox.showwarning('Please enter a valid item.')

def del_func():
    lb.delete(ANCHOR)

def complete_func():
    lb.itemconfig(lb.curselection(),
                  fg= '#dedede')
    lb.selection_clear(0, END)

def uncomplete_func():
    lb.itemconfig(lb.curselection(),
                  fg='')
    lb.selection_clear(0, END)

def save_list():
    file_name = filedialog.asksaveasfilename(initialdir=r'C:\Users\taylo\PycharmProjects\ToDo App' , title = 'Save File',
                                             filetypes=(('Dat Files', '*.dat' ), ('All Files', '*.')))
    if file_name:
        if file_name.endswith('.dat'):
            pass
        else:
            file_name = (f'{file_name}.dat')

    #get stuff
    stuff = lb.get(0, END)

    #open file
    output_file = open(file_name, 'wb')

    #actually add stuff to file
    pickle.dump(stuff, output_file)


def open_list():
    file_name = filedialog.askopenfilename(initialdir=r'C:\Users\taylo\PycharmProjects\ToDo App' , title = 'Open File',
                                             filetypes=(('Dat Files', '*.dat' ), ('All Files', '*.')))
    if file_name:
        lb.delete(0, END)

        # open file
        input_file = open(file_name, 'rb')

        #load data
        stuff = pickle.load(input_file)

        #output stuff
        for item in stuff:
            lb.insert(END, item)

task = []
for i in task:
    lb.insert(END, i)

my_menu = Menu(root)
root.config(menu = my_menu)

file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label = 'File', menu = file_menu)
file_menu.add_command(label='Save', command=save_list)
file_menu.add_command(label='Open', command=open_list)



add_button = Button(button_frame, text = 'Add Item', command=add_func,  height=5, width=15, fg = 'red', bg= 'black', font = my_font).pack(fill = BOTH, side = LEFT)
delete_button = Button(button_frame, text = 'Delete Item',command=del_func,  height=5, width=15, fg = 'red', bg= 'black', font = my_font).pack(fill = BOTH, side = LEFT)
complete_button = Button(button_frame, text = 'Completed', command = complete_func, height=5, width=15, fg = 'red', bg= 'black', font = my_font  ).pack(fill=BOTH, side= LEFT)
uncomplete_button = Button(button_frame, text = 'UnCompleted', command = uncomplete_func, height=5, width=15, fg = 'red', bg= 'black', font = my_font).pack(fill=BOTH, side= LEFT)

l.pack()
frame.pack(pady=10, fill= BOTH, expand= True)
lb.pack(pady = 25, padx = 25, side = LEFT, fill= BOTH, expand= True)
sb_v.pack(side=RIGHT, fill= BOTH)
sb_h.pack(side= BOTTOM, fill= BOTH)
lb.config(yscrollcommand = sb_v.set)
lb.config(xscrollcommand = sb_h.set)
sb_v.config(command= lb.yview)
sb_h.config(command= lb.xview)
entry_box.pack(pady = 20, padx = 20, fill= BOTH)
button_frame.pack(pady = 20)

root = mainloop()
