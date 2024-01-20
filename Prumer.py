def vazeny_prumer(prvky, vahy):

    vazen_sum = sum(xi * wi for xi, wi in zip(prvky, vahy))

    soucet_vah = sum(vahy)

    vazeny_prumer = vazen_sum / soucet_vah

    return vazeny_prumer

prvky_input = input("Zadejte znamky oddelene carkou: ")
vahy_input = input("Zadejte vahy oddelene carkou: ")

prvky = [float(prvek.strip()) for prvek in prvky_input.split(',')]
vahy = [float(vaha.strip()) for vaha in vahy_input.split(',')]

vazeny_prumer_vysledek = vazeny_prumer(prvky, vahy)
print(f"Prumer: {vazeny_prumer_vysledek}")
input("pro ukoncni stisknete jakekoli tlacitko... ")