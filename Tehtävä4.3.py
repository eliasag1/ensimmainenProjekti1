luvut = []
while True:
    luku = input("Anna luku: ")
    if luku == "":
        break

    try:
        luku = float(luku)
        luvut.append(luku)
    except ValueError:
        print("Syötä luku, kiitos.")

if luvut:
    pienin = min(luvut)
    suurin = max(luvut)
    print(f"Pienin luku: {pienin}")
    print(f"Suurin luku: {suurin}")
else:
    print("Et syöttänyt yhtään lukua.")