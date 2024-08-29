sukupuoli = input("Antakaa biologinen sukupuolenne, nainen/mies: ")
hemoglobiini = float(input("Antakaa hemoglobiiniarvonne, g/l: "))

if sukupuoli == "nainen":
    if hemoglobiini < 117:
        print("Hemoglobiiniarvonne on alhainen.")
    elif 117 <= hemoglobiini <= 175:
        print("Hemoglobiiniarvonne on normaali.")
    else:
        print("Hemoglobiiniarvonne on korkea.")
elif sukupuoli == "mies":
    if hemoglobiini < 134:
        print("Hemoglobiiniarvonne on alhainen.")
    elif 134 <= hemoglobiini <= 195:
        print("Hemoglobiiniarvonne on normaali.")
    else:
        print("Hemoglobiiniarvonne on korkea.")
else:
    print("Syötä sukupuoli pienin kirjaimin, kiitos")