luvut = []
while True:
    syöte = input("Anna luku: ")
    if syöte == "":
        break
    luvut.append(int(syöte))
luvut.sort(reverse=True)
print("Viisi suurinta lukua ovat:")
for luku in luvut[:5]:
    print(luku)