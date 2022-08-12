from datetime import *
priorytety = ["10", "12", "24", "48", "72"]
rok_biezacy = date.today()
rok_biezacy = int(rok_biezacy.year)
swieta = [date(2022, 1, 1), date(2022, 1, 6), date(2022, 5, 1), date(2022, 5, 3), date(2022, 8, 15),
          date(2022, 11, 1), date(2022, 11, 11), date(2022, 12, 25), date(2022, 12, 26)]
for i in range(len(swieta)):
    swieta[i] = swieta[i].replace(year= rok_biezacy)
    print(swieta[i])

wielkanoc = [date(2022, 4, 18), date(2023, 4, 10), date(2024, 4, 1), date(2025, 4, 21), date(2026, 4, 6),
             date(2027, 3, 29), date(2028, 4, 17), date(2029, 4, 2), date(2030, 4, 22)]
boze_cialo = []
for j in wielkanoc:
    j = j + timedelta(days=59)
    boze_cialo.append(j)


def czas_naprawy(data_z, cz, godz_z, godz_r, swieta, wielkanoc, boze_cialo):
    for i in range(cz):
        print(data_z)
        dzien_tyg_z = data_z.isoweekday()
        if dzien_tyg_z == 7 or data_z.date() in swieta or data_z.date() in wielkanoc or data_z.date() in boze_cialo:
            if data_z.hour >=14:
                data_z +=timedelta(days=1)
                data_z = data_z.replace(hour=godz_r)
            else:
                data_z += timedelta(hours=1)
        elif ((data_z + timedelta(days= 1)).date() in swieta or (data_z + timedelta(days= 1)).date() in wielkanoc or (data_z + timedelta(days= 1)).date() in boze_cialo) and data_z.hour >= godz_z :
                data_z +=timedelta(days=1)
                data_z = data_z.replace(hour=7)
        else:
            if data_z.hour >= godz_z:
                data_z += timedelta(days=1)
                data_z = data_z.replace(hour=godz_r)
            else:
                data_z += timedelta(hours=1)
    return data_z

def data_przyjecia(data_p, swieta, wielkanoc, boze_cialo):
    dzien_tyg_p = data_p.isoweekday()
    if dzien_tyg_p == 7 or data_p.date() in swieta or data_p.date() in wielkanoc or data_p.date() in boze_cialo:
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
def main(data_przyj, p):
    if p in priorytety:
        priorytet = int(p)
        data_przyj = data_przyjecia(data_przyj, swieta, wielkanoc, boze_cialo)
        data_zak = data_przyj

        czas_serwis = czas_naprawy(data_zak, priorytet, 20, 7, swieta, wielkanoc, boze_cialo)
        czas_zabka = czas_naprawy(data_zak, priorytet, 22, 6, swieta, wielkanoc, boze_cialo)

        data_przyj = data_przyj.strftime("%Y-%m-%d %H:%M")
        czas_serwis = czas_serwis.strftime("%Y-%m-%d %H:%M")
        czas_zabka = czas_zabka.strftime("%Y-%m-%d %H:%M")

        print("Data przyjecia: " + str(data_przyj))
        print("Data zakończenia dla serwisu: " + str(czas_serwis))
        print("Data zakończenia dla żabki: " + str(czas_zabka))
    else:
        print("Nie ma takiego priorytetu. Spróbuj jeszcze raz.")
while True:
    try:

        nowa_data = (input("Podaj nową datę w formacie rok-mies-dzien godz:min "))
        if nowa_data == "":
            data_przyj = datetime.now()
            priorytet = input("Podaj priorytet naprawy: ")
            main(data_przyj, priorytet)
            print()

        else:
            nowa_data = datetime.strptime(nowa_data, "%Y-%m-%d %H:%M")
            priorytet = input("Podaj priorytet naprawy: ")
            data_przyj = nowa_data
            main(data_przyj, priorytet)
            print()

    except ValueError:
        print("Niepoprawny format daty, sprawdź czy nie ma przypadkowej spacji i spróbuj jeszcze raz.")
    except KeyboardInterrupt as e:
        print()
        continue
