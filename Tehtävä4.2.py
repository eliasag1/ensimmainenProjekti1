tuumatcm = 2.54

while True:
    tuumat = float(input("Anna tuumat: "))
    if tuumat < 0:
        print("Annoit negatiivisen luvun, hävisit pelin.")
        break
    senttimetrit = tuumat * tuumatcm
    print(f"{tuumat} tuumaa on {senttimetrit:.2f} cm")