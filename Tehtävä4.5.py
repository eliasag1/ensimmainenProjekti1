oikeatunnus = "python"
oikeasalasana = "rules"

yritykset = 0
maxyritykset = 5

while yritykset < maxyritykset:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

    if tunnus == oikeatunnus and salasana == oikeasalasana:
        print("Tervetuloa!")
        break
    else:
        yritykset += 1
        print("Väärä käyttäjätunnus tai salasana. Yritä uudelleen.")

    if yritykset == maxyritykset:
        print("Pääsy evätty.")