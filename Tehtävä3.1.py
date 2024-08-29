kuhan_pituus = float(input("Syötä kuhan pituus senttimetreinä: "))
alamitta = 37.0
if kuhan_pituus < alamitta:
    puuttuva_pituus = alamitta - kuhan_pituus
    print(f"Kuha on alamittainen. Laske kuha takaisin järveen. Kuha on {puuttuva_pituus:.1f} cm liian lyhyt.")
else:
    print ("Kuha ei ole alamittainen")
