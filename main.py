from tkinter import *
#from tkinter.ttk import *

root = Tk()
root.title("KOMIS")
root.iconbitmap('favicon.ico')
root.geometry("500x500")

#s = Style()
#s.configure('My.TFrame', background='red')

def foo():
    print('nice')

up_menu = Menu(root)
root.config(menu=up_menu)

pliki_menu = Menu(up_menu)
raport_menu = Menu(up_menu)
up_menu.add_cascade(label="Pliki", menu=pliki_menu)
up_menu.add_cascade(label="Raporty", menu=raport_menu)
pliki_menu.add_command(label="Pokwitowanie", command=foo)
pliki_menu.add_command(label="Paragon", command=foo)
pliki_menu.add_separator()
pliki_menu.add_command(label="Faktura VAT", command=foo)
pliki_menu.add_command(label="Faktura bez VATu", command=foo)


raport_menu.add_command(label="Konmtrahenci", command=foo)
raport_menu.add_command(label="Miesięczny", command=foo)
raport_menu.add_separator()
raport_menu.add_command(label="Dzienny", command=foo)




frame1 = Frame(root, width=100, high=500, bg="red")

frame2 = Frame(root)
goodmorning = Label(frame1, text="Dzień dobry.\n Wybierz:")
button = Button(frame2, text="Button")
button.pack()
goodmorning.pack()
frame1.pack(side=LEFT)
frame2.pack(side=RIGHT)
root.mainloop()