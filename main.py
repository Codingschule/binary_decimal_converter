#found on website: https://www.programmieraufgaben.ch/aufgabe/zahlensystemumrechner-dual-binaer-hexadezimal-und-dezimal/wbc93sou

import tkinter as tk

def dezi():
    if len(dez_Entry.get())>0:
        dual_Entry.delete(0,"end")
        hex_Entry.delete(0,"end")
        dual_output = bin(int(dez_Entry.get()))
        hex_output=hex(int(dez_Entry.get()))
        
        dual_Entry.insert(0, dual_output)
        hex_Entry.insert(0, hex_output)
        print("Binärzahl:", dual_output, "Hexadezimalzahl:", hex_output)
def hexa():
    if len(hex_Entry.get())>0:
        dez_Entry.delete(0,"end")
        dual_Entry.delete(0,"end")
        dez_output = int(hex_Entry.get(), 16)
        dual_output = bin(int(hex_Entry.get(), 16))
        
        dez_Entry.insert(0, dez_output)
        dual_Entry.insert(0, dual_output)
        print("Binärzahl:", dual_output, "Dezimalzahl:", dez_output)
def dual():
    if len(dual_Entry.get())>0:
        dez_Entry.delete(0,"end")
        hex_Entry.delete(0,"end")
        dez_output = int(dual_Entry.get(),2)
        hex_output=hex(int(dual_Entry.get(),2))
        
        dez_Entry.insert(0, dez_output)
        hex_Entry.insert(0, hex_output)
        print("Dezimalzahl:", dez_output, "Hexazdezimalzahl:", hex_output)
        
                         

main = tk.Tk()
main.title("Binär-Hexadezimal-Dezimal-Rechner")

dez_label = tk.LabelFrame(main, text = "Dezimalzahl")
dez_label.grid()
dez_Entry = tk.Entry(dez_label)
dez_Entry.grid()

hex_label = tk.LabelFrame(main, text = "Hexadezimalzahl")
hex_label.grid()
hex_Entry = tk.Entry(hex_label)
hex_Entry.grid()

dual_label = tk.LabelFrame(main, text = "Binärzahl")
dual_label.grid()
dual_Entry = tk.Entry(dual_label)
dual_Entry.grid()

button_dezi = tk.Button(main, text = "Von Dezimal nach Dual und Hexadezimal", command = dezi)
button_dezi.grid()

button_hexa = tk.Button(main, text = "Von Hexadzimal nach Dual und Dezimal", command = hexa)
button_hexa.grid()

button_dual = tk.Button(main, text = "Von Dual nach Dezimal und Hexadezimal", command = dual)
button_dual.grid()


main.mainloop()
