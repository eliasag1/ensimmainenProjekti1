def litroiksi (gallonat):
    litra=gallonat*3.785
    return litra
while True:
    gallonat=int(input("Bensiinin määrä gallonoina: "))
    if gallonat < 0:
        break
    litra=litroiksi(gallonat)
    print (f"{gallonat} gallonaa on {litra:.2f} litraa")


