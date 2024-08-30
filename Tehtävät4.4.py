import random

random_luku = random.randint(1, 10)

while True:
    try:
        arvaus = int(input("Arvaa luku väliltä 1-10: "))
    except ValueError:
        print("Syötä kokonaisluku.")
        continue

    if arvaus < random_luku:
        print("Liian pieni luku")
    elif arvaus > random_luku:
        print("Liian suuri luku")
    else:
        print("Oikein! Voitit pelin!")
        break