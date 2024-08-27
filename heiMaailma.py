print ("Hei, maailma!")
käyttäjä = input ("Anna nimesi:")
print("Hauska tavata, " + käyttäjä +"!")
# Luetaan syötteet
kanta=float(input("Anna kolmion kanta: "))
korkeus=float(input("Anna kolmion korkeus: "))
# Lasketaan ala syötteiden perusteella
ala = (kanta * korkeus) / 2
# Tulostetaan vastaus
#print("Kolmion ala on: "+ str(ala))
print(f"Kolmion ala on{ala:10.2f}")

