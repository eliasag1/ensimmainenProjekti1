import random

def noppa(tahkot):
    luku = random.randint(1,tahkot)
    return luku

tahkojenmäärä=int(input("Anna tahkojen määrä: "))

while True:
    luku = noppa(tahkojenmäärä)
    print(luku)
    if luku == tahkojenmäärä:
        break
