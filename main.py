from datetime import *
#import pytz
while True:
    data_przyj = datetime.now()
    data_przyj = data_przyj.replace(day=6)
    """
    tz = pytz.timezone("Europe/Warsaw")
    data_przyj = data_przyj.astimezone(tz)
    """
    czas = int(input("Podaj czas naprawy"))

    dzien_tyg_p = data_przyj.isoweekday()

    if dzien_tyg_p == 7:
        if data_przyj.hour > 15:
            data_przyj += timedelta(days=1)
            data_przyj = data_przyj.replace(hour=7)
        elif data_przyj.hour < 7:
            data_przyj = data_przyj.replace(hour=7)
    else:
        if data_przyj.hour > 21:
            data_przyj += timedelta(days=1)
            data_przyj = data_przyj.replace(hour=7)
        elif data_przyj.hour < 7:
            data_przyj = data_przyj.replace(hour=7)

    data_zak = data_przyj

    for i in range(czas, 0, -1):
        dzien_tyg_z = data_zak.isoweekday()
        print(dzien_tyg_z)
        if dzien_tyg_z == 7:
            if data_zak.hour > 14:
                data_zak += timedelta(days=1)
                data_zak = data_zak.replace(hour=7)
                data_zak += timedelta(hours=1)
            else:
                data_zak += timedelta(hours=1)
        else:
            if data_zak.hour < 21:
                data_zak += timedelta(hours=1)
            else:
                data_zak += timedelta(days=1)
                data_zak = data_zak.replace(hour=7)
                data_zak += timedelta(hours=1)

    # print ("Pozostaly czas: " + str(czas))
    print("Data przyjecia: " + str(data_przyj))
    print("Data_zakonczenia: " + str(data_zak))
