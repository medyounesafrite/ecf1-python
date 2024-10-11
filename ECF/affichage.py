import os, json


# affichier  tout le contenu du fichier JSON
def afficher_fichier_json(JSON_FILE):
    # traitement du cas ou le fichier est vide
    if os.stat(JSON_FILE).st_size == 0:
        print("Fichier Vide")
    else:
        with open(JSON_FILE, 'r') as fichier_read:
            data_json = json.load(fichier_read)
            liste_trier = sorted(data_json, key=lambda x: x["temps"], reverse=False)

        print(f"Liste des essais : ")
        print("")
        # condtion ou il a selectionné un nom à chercher
        for ligne in liste_trier:
            print(
                f"   Nom : {ligne['nom']}, Valeur Chercher : {ligne['valeur_chercher']}, Nombre de tentatives : {ligne['tentative']}, Temps : {ligne['temps']}")
        print("")
        print("Fin Lecture  Fichier")


# affichier tout le contenu du fichier texte
def afficher_fichier_txt(TXT_FILE):
    # traitement du cas ou le fichier est vide
    if os.stat(TXT_FILE).st_size == 0:
        print("Fichier Vide")
    else:
        with open(TXT_FILE, 'r') as fichier_read:
            print(f"Liste des essais :")
            for ligne in fichier_read:
                print(f"  {ligne.strip()}")

            print("")
            print("Fin Lecture  Fichier")


# Afficher le menu principal avec la récuperation d'une valeur de retour
def afficher_menu_principale():
    print("------------- Juste Prix ------------- Menu de démarrage")
    print("1- Résultat")
    print("2- Nouvelle Partie")
    print("3- Quitter")
    print("Entrez Votre choix SVP :")
    return input()


# afficher le menu resultats et recuperer le choix
def afficher_menu_resultats():
    print("------------- Selectionnez le type de sauvegarde à affichier")
    while True:
        try:
            print("1- Fichier Texte")
            print("2- Fichier JSON")
            print("Tapez 'exit' pour retourner au menu principal")
            reponse = input()
            if str(reponse).lower() == "exit":
                return 0
            elif isinstance(int(reponse), int) and (4 > int(reponse) > 0):
                return int(reponse)
            else:

                raise ValueError

        except ValueError as msg:

            print("Votre Choix est incorrect !! Merci de reselectionner 2 !")


# Fonction pour recuperer le nom du joueur avant de commencer le jeu
def get_nom_joueur():
    Nom_joueur = ""
    while len(Nom_joueur) == 0:
        print("Tapez Votre Nom SVP :")
        resultat = input("")
        if len(resultat) == 0 or resultat.lower() == "exit" or ":" in resultat:
            print("Votre choix est incorrect")
        else:
            Nom_joueur = resultat
    return Nom_joueur


# fonction pour verifier s'il veut chercher avec un nom du joueur ou non avec le retour du nom si oui ou vide
def get_nom_pour_chercher_ses_resultats():

    while True:
        print("Vous Voulez Chercher avec un non ? oui/non")
        try:
            reponse = input("")
            if isinstance(str(reponse), str):
                if str(reponse).lower() == "oui":
                    print("Tapez le Nom à chercher")
                    nom = input()
                    return nom
                elif str(reponse).lower() == "non":
                    return ""
                else:
                    raise ValueError
            else:
                raise ValueError

        except ValueError:
            print("Votre Choix est incorrect !! oui/non !")
