from tkinter import *
import Pmw
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




frame1 = Frame(root, borderwidth=2, relief='ridge', padx=29, pady=50)#, padx=100, pady=350

frame2 = Frame(root, borderwidth=2, relief='ridge', padx=25, pady=50)#, padx=400, pady=350
goodmorning = Label(frame1, text="Dzień dobry.\n Wybierz:")
button_pokwitowanie = Button(frame1, text='Pokwitowanie', padx=5, pady=10, command=foo)
button_paragon = Button(frame1, text='Paragon', padx=21, pady=10, command=foo)
button_faktura_vat = Button(frame1, text='Faktura VAT', padx=12, pady=10, command=foo)
button_faktura_bez_vat = Button(frame1, text='Faktura bez VAT', pady=10, command=foo)
button = Button(frame2, text="Button")

frame3 = Frame(root, borderwidth=2, relief='ridge', padx=15, pady=15)
button_find = Button(frame3, text="Szukaj", padx=10, command=foo)

obiekty = ["kontrahenci", "przedmioty"]
v = StringVar()
v.set("kontrahenci")
for el in obiekty:
    dot = Radiobutton(frame3, text=el, variable=v, value=el)
    dot.pack()

wyszukaj = Entry(frame3)
frame1.grid(row=0, column=0)

goodmorning.pack()
button_pokwitowanie.pack()
button_paragon.pack()
button_faktura_vat.pack()
button_faktura_bez_vat.pack()
#frame1.pack(side=LEFT)
frame2.grid(row=0, column=10)
#frame2.pack(side=RIGHT)
button.pack()
frame3.grid(row=1, column=0)
wyszukaj.pack()
button_find.pack()

root.mainloop()