import random

määrä = int(input("Kuinka monta arpakuutiota heitetään? "))
summa = 0
for i in range(määrä):
    heitto = random.randint(1, 6)
    summa += heitto
print(f"Noppien summa on: {summa}")