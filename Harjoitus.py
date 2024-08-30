lkm=int(input("Montako kaveria sinulla on?: "))

kaverit=[]
for luku in range(lkm):
    nimi=input ("Anna kaverin nimi: ")
    kaverit.append(nimi)

print("KAVERILISTA:")
for kaveri in kaverit:
    print(kaveri)
