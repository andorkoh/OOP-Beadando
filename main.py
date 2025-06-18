import tkinter as tk
from tkinter import messagebox, Listbox, END
from datetime import date
from autokolcsonzo import Autokolcsonzo
from szemelyauto import Szemelyauto
from teherauto import Teherauto
from berles import Berles

egyenleg = 10000
kolcsonzo = Autokolcsonzo("Autókölcsönző")
kolcsonzo.autok = [
    Szemelyauto("ABC-123", "Toyota Corolla", 10000, 5),
    Szemelyauto("DEF-456", "Mazda RX-8", 12000, 4),
    Szemelyauto("PKR-234", "Opel Tigra", 10000, 2),
    Szemelyauto("MRS-677", "Mercedes Benz", 15000, 5),
    Teherauto("GHI-789", "Ford Transit", 15000, 3500),
    Teherauto("JKL-321", "Mercedes Sprinter", 18000, 3000),
    Teherauto("LFG-367", "Toyota Hilux", 20000, 3200)]

kolcsonzo.berlesek = [
    Berles(kolcsonzo.autok[0], date.today()),
    Berles(kolcsonzo.autok[1], date.today()),
    Berles(kolcsonzo.autok[2], date.today()),
    Berles(kolcsonzo.autok[6], date.today())]

def listafrissites():
    auto_listbox.delete(0, END)
    for auto in kolcsonzo.berelheto_autok():
        auto_listbox.insert(END, str(auto))

def berlesfrissites():
    berles_listbox.delete(0, END)
    for berles in kolcsonzo.berlesek:
        berles_listbox.insert(END, str(berles))

def egyenlegfrissites():
    egyenleg_label.config(text=f"Egyenleg: {egyenleg} Ft")

def autoberles():
    global egyenleg
    kivalasztott = auto_listbox.curselection()
    if not kivalasztott:
        messagebox.showwarning("Hiba", "Válassz ki egy autót!")
        return
    auto = kolcsonzo.berelheto_autok()[kivalasztott[0]]
    try:
        uj_berles, koltseg = Berles.uj_berles(auto, egyenleg, date.today())
        kolcsonzo.berlesek.append(uj_berles)
        egyenleg -= koltseg
        listafrissites()
        berlesfrissites()
        egyenlegfrissites()
        messagebox.showinfo("Siker", f"{auto.tipus} ({auto.rendszam}) bérlés megtörtént.")
    except ValueError as ve:
        messagebox.showerror("Hiba", str(ve))

def berleslemondas():
    global egyenleg
    kivalasztott = berles_listbox.curselection()
    if not kivalasztott:
        messagebox.showwarning("Hiba", "Válassz ki egy bérlést!")
        return
    auto = kolcsonzo.berlesek[kivalasztott[0]].auto
    vissza_auto = kolcsonzo.lemondas(auto.rendszam)
    egyenleg += vissza_auto.berleti_dij
    listafrissites()
    berlesfrissites()
    egyenlegfrissites()
    messagebox.showinfo("Siker", f"{auto.tipus} ({auto.rendszam}) bérlés lemondva.")

def tulajdonsagok():
    kivalasztott = auto_listbox.curselection() or berles_listbox.curselection()
    if not kivalasztott:
        messagebox.showwarning("Hiba", "Válassz ki egy autót vagy bérlést!")
        return
    if auto_listbox.curselection():
        auto = kolcsonzo.berelheto_autok()[auto_listbox.curselection()[0]]
    else:
        auto = kolcsonzo.berlesek[berles_listbox.curselection()[0]].auto

    if hasattr(auto, 'ulesek_szama'):
        messagebox.showinfo("Tulajdonságok", f"{auto.tipus} ({auto.rendszam}) - {auto.ulesek_szama} ülés")
    elif hasattr(auto, 'teherbiras'):
        messagebox.showinfo("Tulajdonságok", f"{auto.tipus} ({auto.rendszam}) - {auto.teherbiras} kg teherbírás")

root = tk.Tk()
root.title("Autókölcsönző")

egyenleg_label = tk.Label(root, text="")
egyenleg_label.grid(row=0, column=0)

tk.Label(root, text="Elérhető autók:").grid(row=1, column=0)
auto_listbox = Listbox(root, width=50)
auto_listbox.grid(row=2, column=0)

tk.Button(root, text="Autó bérlése", command=autoberles).grid(row=3, column=0)
tk.Button(root, text="Tulajdonságok", command=tulajdonsagok).grid(row=4, column=0)

tk.Label(root, text="Aktuális bérlések:").grid(row=5, column=0)
berles_listbox = Listbox(root, width=50)
berles_listbox.grid(row=6, column=0)

tk.Button(root, text="Bérlés lemondása", command=berleslemondas).grid(row=7, column=0)

listafrissites()
berlesfrissites()
egyenlegfrissites()
root.mainloop()
