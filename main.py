from datetime import *

while True:
    data_przyj = datetime.now()
    data_przyj = data_przyj.replace(second=0,microsecond=0)
    data_przyj = data_przyj.replace(day=6,hour=21)
    czas = int(input("Podaj czas naprawy"))

    dzien_tyg_p = data_przyj.isoweekday()

    if dzien_tyg_p == 7:
        if data_przyj.hour >= 15:
            data_przyj += timedelta(days=1)
            data_przyj = data_przyj.replace(hour=7, minute=0)
        elif data_przyj.hour < 7:
            data_przyj = data_przyj.replace(hour=7, minute=0)
    else:
        if data_przyj.hour >= 21:
            data_przyj += timedelta(days=1)
            data_przyj = data_przyj.replace(hour=7, minute=0)
        elif data_przyj.hour < 7:
            data_przyj = data_przyj.replace(hour=7, minute=0)

    data_zak = data_przyj

    for i in range(czas):
        dzien_tyg_z = data_zak.isoweekday()
        if dzien_tyg_z == 7:
            if data_zak.hour < 14:
                data_zak += timedelta(hours=1)
            else:
                data_zak += timedelta(days=1)
                data_zak = data_zak.replace(hour=7)
        else:
            if data_zak.hour < 20:
                data_zak += timedelta(hours=1)
            else:
                data_zak += timedelta(days=1)
                data_zak = data_zak.replace(hour=7)


    # print ("Pozostaly czas: " + str(czas))
    print("Data przyjecia: " + str(data_przyj))
    print("Data_zakonczenia: " + str(data_zak))
