from datetime import *

priorytety = ["10", "12", "24", "48", "72"]


def dni_wolne():
    swieta = [date(2022, 1, 1), date(2022, 1, 6), date(2022, 5, 1), date(2022, 5, 3), date(2022, 8, 15),
              date(2022, 11, 1), date(2022, 11, 11), date(2022, 12, 25), date(2022, 12, 26)]
    for i in range(len(swieta)):
        swieta[i] = swieta[i].replace(year=int(data_przyj.year))

    wielkanoc = [date(2022, 4, 18), date(2023, 4, 10), date(2024, 4, 1), date(2025, 4, 21), date(2026, 4, 6),
                 date(2027, 3, 29), date(2028, 4, 17), date(2029, 4, 2), date(2030, 4, 22)]
    boze_cialo = []
    for j in wielkanoc:
        j = j + timedelta(days=59)
        boze_cialo.append(j)
    return swieta + wielkanoc + boze_cialo


def czas_naprawy(data_z, p, godz_z, godz_r, dw):
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


def main(data_przyj, p):
    if p in priorytety:
        dw = dni_wolne()
        priorytet = int(p)

        data_przyj = data_przyjecia(data_przyj, dw)
        data_zak = data_przyj

        czas_serwis = czas_naprawy(data_zak, priorytet, 20, 7, dw)
        czas_zabka = czas_naprawy(data_zak, priorytet, 22, 6, dw)

        if czas_serwis.hour == 7 and czas_serwis.minute == 0:
            if ((czas_serwis - timedelta(days=1)).isoweekday()) == 7 or (czas_serwis.date() - timedelta(days=1)) in dw:
                czas_serwis = czas_serwis - timedelta(days=1)
                czas_serwis = czas_serwis.replace(hour=15)
            else:
                czas_serwis= czas_serwis - timedelta(days= 1)
                czas_serwis= czas_serwis.replace(hour=21)

        if (czas_zabka.hour == 7 or czas_zabka.hour == 6) and czas_zabka.minute==0:
            if ((czas_zabka - timedelta(days=1)).isoweekday()) == 7 or (czas_zabka.date() - timedelta(days=1)) in dw:
                czas_zabka = czas_zabka - timedelta(days=1)
                czas_zabka = czas_zabka.replace(hour=15)
            else:
                czas_zabka = czas_zabka - timedelta(days=1)
                czas_zabka = czas_zabka.replace(hour=23)


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
