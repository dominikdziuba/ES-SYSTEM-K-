from datetime import *
from tkinter import *
from tkinter import messagebox
priorytety = ["10", "12", "24", "48", "72"]

def dni_wolne(data_przyj):
    swieta = [date(2022, 1, 1), date(2022, 1, 6), date(2022, 5, 1), date(2022, 5, 3), date(2022, 8, 15),
              date(2022, 11, 1), date(2022, 11, 11), date(2022, 12, 25), date(2022, 12, 26)]
    for i in range(len(swieta)):
        swieta[i] = swieta[i].replace(year=int(data_przyj.year))
    a=24
    if int(data_przyj.year)<2100 and int(data_przyj.year)>=1900:
        b=5
    elif int(data_przyj.year) < 2200 and int(data_przyj.year) >=2100:
        b=6

    w1 = int(data_przyj.year)%19
    w2 = int(data_przyj.year)%4
    w3 = int(data_przyj.year)%7
    w1 = (19*w1+a)%30
    w2 = (2*w2+4*w3+6*w1+b)%7

    if w1==29 and w2 == 6:
        wielkanoc = date(int(data_przyj.year),4,20)
    elif w1==28 and w2 == 6:
        wielkanoc = date(int(data_przyj.year),4,19)
    else:
        wielkanoc = date(int(data_przyj.year), 3, 22) + timedelta(days=(w1 + w2 + 1))

    boze_cialo = wielkanoc + timedelta(days=59)
    swieta.append(wielkanoc)
    swieta.append(boze_cialo)
    return swieta

def data_przyjecia(data_p, dw):
    dzien_tyg_p = data_p.isoweekday()
    if dzien_tyg_p == 7 or data_p.date() in dw:
        if data_p.hour >= 15:
            data_p += timedelta(days=1)
            data_p = data_p.replace(hour=7, minute=0)
        elif data_p.hour < 7:
            data_p = data_p.replace(hour=7, minute=0)
    else:
        if data_p.hour >= 21:
            data_p += timedelta(days=1)
            data_p = data_p.replace(hour=7, minute=0)
        elif data_p.hour < 7:
            data_p = data_p.replace(hour=7, minute=0)
    return data_p

def czas_naprawy(data_z, p, godz_z, godz_r, dw, data_przyj):
    for i in range(p):
        dzien_tyg_z = data_z.isoweekday()
        if dzien_tyg_z == 7 or data_z.date() in dw or data_z.date() == date(int(data_z.year),1,1):
            if data_z.hour >= 14:
                if (data_z + timedelta(days=1)).date() in dw:
                    data_z += timedelta(days=1)
                    data_z = data_z.replace(hour=7)
                elif (data_z + timedelta(days=1)).isoweekday() == 7:
                    data_z += timedelta(days=1)
                    data_z = data_z.replace(hour=7)
                elif (data_z + timedelta(days=1)).date() == date(int(data_przyj.year) + 1, 1,1):
                    data_z += timedelta(days=1)
                    data_z = data_z.replace(hour=7)
                else:
                    data_z += timedelta(days=1)
                    data_z = data_z.replace(hour=godz_r)
            else:
                data_z += timedelta(hours=1)
        elif (data_z + timedelta(days=1)).date() in dw and data_z.hour >= godz_z:
            data_z += timedelta(days=1)
            data_z = data_z.replace(hour=7)
        elif (data_z + timedelta(days=1)).isoweekday() == 7 and data_z.hour >= godz_z:
            data_z += timedelta(days=1)
            data_z = data_z.replace(hour=7)
        elif ((data_z + timedelta (days= 1)).date() == date(int(data_przyj.year)+1,1,1)) and data_z.hour >= godz_z:
            data_z += timedelta(days=1)
            data_z = data_z.replace(hour=7)

        else:
            if data_z.hour >= godz_z:
                data_z += timedelta(days=1)
                data_z = data_z.replace(hour=godz_r)
            else:
                data_z += timedelta(hours=1)
    return data_z

def format_zabka(czas_zabka, dw):
    if (czas_zabka.hour == 7 and czas_zabka.date().isoweekday() == 7 or czas_zabka.hour == 6) and czas_zabka.minute == 0:
        if ((czas_zabka - timedelta(days=1)).isoweekday()) == 7 or (czas_zabka.date() - timedelta(days=1)) in dw:
            czas_zabka = czas_zabka - timedelta(days=1)
            czas_zabka = czas_zabka.replace(hour=15)
        else:
            czas_zabka = czas_zabka - timedelta(days=1)
            czas_zabka = czas_zabka.replace(hour=23)
    return czas_zabka

def format_serwis(czas_serwis,dw):
    if czas_serwis.hour == 7 and czas_serwis.minute == 0:
        if ((czas_serwis - timedelta(days=1)).isoweekday()) == 7 or (czas_serwis.date() - timedelta(days=1)) in dw:
            czas_serwis = czas_serwis - timedelta(days=1)
            czas_serwis = czas_serwis.replace(hour=15)
        else:
            czas_serwis = czas_serwis - timedelta(days=1)
            czas_serwis = czas_serwis.replace(hour=21)
    return czas_serwis

def dzisiaj():
    teraz = datetime.now().strftime("%Y-%m-%d %H:%M")
    e1.delete(0,END)
    e1.insert(0, teraz)
    return

def getlist(p_lista):
    values = p_lista.curselection()
    if values:
        i = values[0]
        priorytet = p_lista.get(i)
    return priorytet
def oblicz():
    try:
        gl = getlist(p_lista)
        data_przyj = datetime.strptime(e1.get(), "%Y-%m-%d %H:%M")
        dw = dni_wolne(data_przyj)
        dp = data_przyjecia(data_przyj, dw)
        data_zak = data_przyj
        czas_serwis = czas_naprawy(data_zak, int(gl), 20, 7, dw, data_przyj)
        czas_zabka = czas_naprawy(data_zak, int(gl), 22, 6, dw, data_przyj)
        fs = format_serwis(czas_serwis, dw)
        fz = format_zabka(czas_zabka, dw)
    except ValueError:
        messagebox.showerror('BŁĄD',"Nieprawidłowy format daty")
    except UnboundLocalError:
        messagebox.showerror("Błąd", "Wybierz priorytet")
    dp2_text.delete(0.0, END)
    dp2_text.insert(END,dp.strftime("%Y-%m-%d %H:%M"))
    ds_text.delete(0.0,END)
    ds_text.insert(END,fs.strftime("%Y-%m-%d %H:%M"))
    dz_text.delete(0.0,END)
    dz_text.insert(END,fz.strftime("%Y-%m-%d %H:%M"))


root = Tk()
root.title('Priorytety')
root.geometry("500x330")
dp_label = Label(root,text="Podaj nową datę w formacie rok-mies-dzien godz:min:")
dp_label.grid(row=0, column=0)
e1= Entry(root, width= 20)
e1.grid(row=0, column=1)
p_label = Label(root,text="Wybierz priorytet naprawy: ",)
p_label.grid(row=1, column=0)
p_lista = Listbox(root, height= 5)
p_lista.grid(row=1, column=1)

for i in priorytety:
    p_lista.insert(END,i)

przerwa = Label(root)
przerwa.grid(row=2)
przerwa2= Label(root)
przerwa2.grid(row= 4)
b1 = Button(root,text="Teraz",command=lambda:dzisiaj())
b1.grid(row=0, column=2)
dp2_label = Label(root,text="Data przyjecia:")
dp2_label.grid(row=6, column=0)
ds_label = Label(root,text="Data zakończenia dla serwisu:")
ds_label.grid(row=7, column=0)
dz_label = Label(root, text="Data zakończenia dla żabki:")
dz_label.grid(row=8, column=0)
dp2_text = Text(root, height=1, width=18)
dp2_text.grid(row=6, column=1)
ds_text = Text(root, height=1, width=18)
ds_text.grid(row=7, column=1)
dz_text = Text(root, height=1, width=18)
dz_text.grid(row=8,column=1)
b2 = Button(root, text="Oblicz", height=3, width=10, command=oblicz)
b2.grid(row=3, column=1)


root.mainloop()
