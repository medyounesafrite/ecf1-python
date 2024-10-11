import json
import os


def afficher_liste_par_nom_txt(TXT_FILE, nom):
    data_txt = []
    # traitement du cas ou le fichier est vide
    if os.stat(TXT_FILE).st_size == 0:
        print("Fichier Vide")
    else:
        with open(TXT_FILE, 'r') as fichier_read:
            print(f"Liste des essais pour l'utilisateur : {nom}")
            for ligne in fichier_read:
                if str(nom).lower() in str(ligne.strip().lower()):
                    print(f"  {ligne.strip()}")
            print("")
            print("Fin Lecture  Fichier")


def afficher_liste_par_nom_json(JSON_FILE, nom):
    data_json = []
    # traitement du cas ou le fichier est vide
    if os.stat(JSON_FILE).st_size == 0:
        print("Fichier Vide")
    else:
        with open(JSON_FILE, 'r') as fichier_read:
            data_json = json.load(fichier_read)
        print(f"Liste des essais : {nom}")
        print("")
        for ligne in data_json:
            if str(nom).lower() in str(ligne['nom'].lower()):
                print(
                    f"   Nom : {ligne['nom']}, Valeur Chercher : {ligne['valeur_chercher']}, Nombre de tentatives : {ligne['tentative']}, Temps : {ligne['temps']}")
        print("")
        print("Fin Lecture  Fichier")
