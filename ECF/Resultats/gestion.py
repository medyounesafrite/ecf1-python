import json
import os


# construir un dictionnaire simple selon format JSON
def construir_json_dict(data, entity):
    dict = {}
    for index, row in enumerate(entity):
        dict[row] = data[index]
    return dict


# fonction recherche dans un fichier TXT ou JSON par un NOM
def recherche(FILE, nom):
    if "txt" in FILE:
        data_txt = []
        # traitement du cas ou le fichier est vide
        if os.stat(FILE).st_size == 0:
            print("Fichier Vide")
        else:
            with open(FILE, 'r') as fichier_read:
                print(f"Liste des essais pour l'utilisateur : {nom}")
                for ligne in fichier_read:
                    if str(nom).lower() in str(ligne.strip().lower()):
                        print(f"  {ligne.strip()}")
                print("")
                print("Fin Lecture  Fichier")

    else:
        data_json = []
        # traitement du cas ou le fichier est vide
        if os.stat(FILE).st_size == 0:
            print("Fichier Vide")
        else:
            with open(FILE, 'r') as fichier_read:
                data_json = json.load(fichier_read)
                liste_trier = sorted(data_json, key=lambda x: x["temps"], reverse=False) #trier par nombre de tentatives
            print(f"Liste des essais : {nom}")
            print("")
            for ligne in liste_trier:
                if str(nom).lower() in str(ligne['nom'].lower()):
                    print(
                        f"   Nom : {ligne['nom']}, Valeur Chercher : {ligne['valeur_chercher']}, Nombre de tentatives : {ligne['tentative']}, Temps : {ligne['temps']}")
            print("")
            print("Fin Lecture  Fichier")


# fonction sauvegarde
def sauvegarde(FILE, resultat, entity):
    if len(entity) == 0:
        with open(FILE, mode='a', encoding='utf-8') as fichier:
            fichier.write(f"{resultat[0].upper()} : {resultat[2]} secondes.\n")
    else:
        # sauvegarder dans le fichier json
        # try:
        liste_dict = []  # on va l'utiliser si le fichier JSON n'est pas vide
        dict = construir_json_dict(resultat, entity)

        # Verifer le fichier est vide ou non
        if os.stat(FILE).st_size == 0:
            liste_dict.append(dict)  # premier dictionnaire ajouter dans le fichier
        else:
            # fichier non vide , donc récuperation des anciennes données
            with open(FILE, 'r') as fichier_read:
                liste_dict = json.load(fichier_read)
                # l'ajout de nouveau dictionnaire
                liste_dict.append(dict)
        # remplir le fichier de nouveau apres l'jout de nouveau dict
        with open(FILE, 'w', ) as fichier_write:
            json.dump(liste_dict, fichier_write, ensure_ascii=False, indent=4)
