
TARIF_LETTRE_VERTE = {20: 1.16, 100: 2.32, 250: 4.00, 500: 6.00, 1000: 7.50, 3000: 10.50}
TARIF_LETTRE_PRIORITAIRE = {20: 1.43, 100: 2.86, 250: 5.26, 500: 7.89, 3000: 10.50}
TARIF_ENVOIE_ECOPLIE = {20: 1.14, 100: 2.28, 250: 3.92}
TARIF_COLISSIMO_OUTRE_MER = {500: 8.35, 1000: 11.20, 2000: 14.10, 5000: 23.65, 10000: 37.50, 15000: 75.85,
                             30000: 87.40}
TARIF_COLISSIMO_CECOGRAMME = {5000: 0}


def main():
    """
    Fonction demandant le type de colis et son poids pour calculer son prix.
    :return: void
    """
    choix_type = choix_type_et_verif()
    choix_poids = choix_poids_et_verif()

    if choix_type == "LETTRE VERTE":
        prix = verif_prix(choix_poids, TARIF_LETTRE_VERTE)

    elif choix_type == "LETTRE PRIORITAIRE":
        prix = verif_prix(choix_poids, TARIF_LETTRE_PRIORITAIRE)

    elif choix_type == "ECOPLI":
        prix = verif_prix(choix_poids, TARIF_ENVOIE_ECOPLIE)

    elif choix_type == "COLISSIMO ECO OUTRE-MER":
        prix = verif_prix(choix_poids, TARIF_COLISSIMO_OUTRE_MER)

    else:
        prix = verif_prix(choix_poids, TARIF_COLISSIMO_CECOGRAMME)
    print(prix)
    if prix >= 0:
        print(f"le prix est : {prix} euros")
    else:
        print("Le colis est trop grands")


def choix_type_et_verif() -> str:
    """
    Fonction vérifiant la validité et récupérant le type de colis de l'utilisateur.
    :return: choix_type (str) : choix du type de colis par l'utilisateur
    """
    choix_type_ok = False
    choix_type = "error"
    while not choix_type_ok:
        choix_type = input("faîtes votre choix parmi (LETTRE VERTE, LETTRE PRIORITAIRE, COLISSIMO ECO OUTRE"
                           "-MER, CÉCOGRAMME): ")
        if choix_type in ["LETTRE VERTE", "LETTRE PRIORITAIRE", "COLISSIMO ECO OUTRE-MER",
                          "CÉCOGRAMME"]:
            choix_type_ok = True
        else:
            print("Je n'ai pas compris votre réponse")

    return choix_type


def choix_poids_et_verif() -> float:
    """
    Fonction de mandant le poids et vérifiant que l'input de l'utilisateur est bien un nombre positif
    :return: choix_poids (float) : poids choisis par l'utilisateur
    """
    while True:
        choix_poids = input("quel poids (en grammes) : ")
        try:
            choix_poids = int(choix_poids)
        except:
            print("utilisez des nombres !")
            continue
        if choix_poids < 1:
            print("utilisez des nombres positifs!")
            continue
        break
    return choix_poids


def verif_prix(poids: float, dico_prix: dict) -> float:
    """
    Vérifie le prix d'un colis en fonction de son poids et de son prix
    :param poids: flo
    :param dico_prix: dict(int:float) dictionnaire décrivant les intervalles de poids et leur prix respectifs lié à un
    type de colis
    :return: float décrivant le prix du colis ou -1 en cas d'érreurs
    """
    for i in dico_prix:
        if poids < i:
            return dico_prix[i]
    return -1


main()
