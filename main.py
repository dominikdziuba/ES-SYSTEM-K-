from datetime import *
def czas_naprawy(d_z, cz, godz_z_d, g_r):
    for i in range(cz):
        dzien_tyg_z = d_z.isoweekday()
        if dzien_tyg_z == 7:
            if d_z.hour < 14:
                d_z += timedelta(hours=1)
            else:
                d_z += timedelta(days=1)
                d_z = d_z.replace(hour=7)
        else:
            if d_z.hour < godz_z_d:
                d_z += timedelta(hours=1)
            else:
                d_z += timedelta(days=1)
                d_z = d_z.replace(hour=g_r)
    return d_z

def data_przyjecia(d_p):
    dzien_tyg_p = d_p.isoweekday()

    if dzien_tyg_p == 7:
        if d_p.hour >= 15:
            d_p += timedelta(days=1)
            d_p = d_p.replace(hour=7, minute=0)
        elif d_p.hour < 7:
            d_p = d_p.replace(hour=7, minute=0)
    else:
        if d_p.hour >= 21:
            d_p += timedelta(days=1)
            d_p = d_p.replace(hour=7, minute=0)
        elif d_p.hour < 7:
            d_p = d_p.replace(hour=7, minute=0)
    return d_p


while True:
    data_przyj = datetime.now()

    priorytet = int(input("Podaj czas naprawy"))
    data_przyj = data_przyjecia(data_przyj)
    data_zak = data_przyj

    rok_biezacy = date.today()
    rok_biezacy = int(rok_biezacy.year)
    swieta = [date(2022,1,1),date(2022,1,6),date(2022,5,1),date(2022,5,3),date(2022,8,15),date(2022,11,1),date(2022,11,11),date(2022,12,25),date(2022,12,26)]
    for i  in swieta:
        i=i.replace(year=rok_biezacy)
    wielkanoc = [date(2023,4,10),date(2024,4,1), date(2025,4,21), date(2026,4,6), date(2027,3,29),date(2028,4,17), date(2029,4,2), date(2030,4,22)]
    boze_cialo = []
    for j in wielkanoc:
        j = j +timedelta(days=59)
        boze_cialo.append(j)

    czas_serwis= czas_naprawy(data_zak, priorytet, 20, 7)
    czas_zabka = czas_naprawy(data_zak, priorytet, 22, 6)

    data_przyj = data_przyj.strftime("%Y-%m-%d %H:%M")
    czas_serwis= czas_serwis.strftime("%Y-%m-%d %H:%M")
    czas_zabka= czas_zabka.strftime("%Y-%m-%d %H:%M")

    print("Data przyjecia: " + str(data_przyj))
    print("Data zakończenia dla serwisu: " + str(czas_serwis))
    print("Data zakończenia dla żabki: " + str(czas_zabka))

