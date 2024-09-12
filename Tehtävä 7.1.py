vuodenajat={
    "talvi":(12,1,2),
    "kevät":(3,4,5),
    "kesä":(6,7,8),
    "syksy":(9,10,11),
}

while True:
    try:
        kuukausi=int(input("Anna kuukauden numero (1-12): "))
        for vuodenaika, kuukaudet in vuodenajat.items():
            if kuukausi in kuukaudet:
                print(f"Kuukausi {kuukausi} kuuluu vuodenaikaan: {vuodenaika.capitalize()}")
                break
    except ValueError:
        print ("Anna luku 1-12 väliltä")









