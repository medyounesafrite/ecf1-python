import json
import os

# fonction pour enregistrer dans un fichier txt sans suppression de données
def enregistrer_fichier_txt(TXT_FILE, resulat):
    with open(TXT_FILE, mode='a', encoding='utf-8') as fichier:
        fichier.write(f"{resulat[0].upper()} : {resulat[2]} secondes.\n")

# construir un dictionnaire simple selon format JSON
def construir_json_dict(data, entity):
    dict = {}
    for index, row in enumerate(entity):
        dict[row] = data[index]
    return dict

#sauvegarder dans le fichier json
def enregistrer_fichier_json(JSON_FILE, resultat, entite):
    # try:
    liste_dict = []  # on va l'utiliser si le fichier JSON n'est pas vide
    dict = construir_json_dict(resultat, entite)

    # Verifer le fichier est vide ou non
    if os.stat(JSON_FILE).st_size == 0:
        liste_dict.append(dict)  # premier dictionnaire ajouter dans le fichier
    else:
        # fichier non vide , doncrécuperation des anciennes données
        with open(JSON_FILE, 'r') as fichier_read:
            liste_dict = json.load(fichier_read)
            # l'ajout de nouveau dictionnaire
            liste_dict.append(dict)
    # remplir le fichier de nouveau apres l'jout de nouveau dict
    with open(JSON_FILE, 'w', ) as fichier_write:
        json.dump(liste_dict, fichier_write, ensure_ascii=False, indent=4)