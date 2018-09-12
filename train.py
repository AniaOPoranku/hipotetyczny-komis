from tkinter import *

root = Tk()

root.iconbitmap("favicon.ico")

def foo():
    print('nice')
my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="file", menu=file_menu)

file_menu.add_command(label="New notebook", command=foo)
file_menu.add_command(label="open", command=foo)
file_menu.add_separator()
file_menu.add_command(label="make a copy", command=foo)

edit_menu = Menu(my_menu)

edit_menu.add_command(label="cut cells", command=foo)
edit_menu.add_command(label="copy cells", command=foo)
edit_menu.add_separator()
edit_menu.add_command(label="paste cells", command=foo)

my_menu.add_cascade(label="Edit", menu=edit_menu)
root.mainloop()