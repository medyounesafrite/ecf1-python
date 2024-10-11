import time, random, os
import affichage
import donnees as DATA
from Resultats.gestion import sauvegarde, recherche



# fonction jouer
def jouer(valeur_chercher):
    trouver = False
    # le jeux est commencé
    debut_de_compteur = time.time()
    valeur_recuperer = ""
    resulat_joueur = []
    tentative = 0
    print("C'est Partie !!")
    os.system('cls')  # commande pour supprimer l'historique du console mais elle marche que sur l'invite de commande
    # time.sleep(2)
    print("Donnez Votre Proposition: ")
    # tant que n'a pas trouvé repter la boucle while
    while not trouver:
        try:

            # os.system('cls')
            valeur_recuperer = input("")
            tentative += 1
            if isinstance(int(valeur_recuperer), int):

                if int(valeur_recuperer) == int(valeur_chercher):
                    # if True:
                    fin_de_compteur = time.time()
                    print("Bravo ! Vous avez trouvé le Juste Prix ")
                    resulat_joueur = [tentative, round(fin_de_compteur - debut_de_compteur, 4)]
                    trouver = True
                elif int(valeur_recuperer) < int(valeur_chercher):
                    print("C'est plus")
                else:
                    print("C'est moins")
            else:
                raise ValueError
        except ValueError as msg:
            print("Votre Choix est incorrect !! Merci d'inserer un nouveau chiffre !")

    # boucle pour ecrire que le mot "entrée" afin de sortir vers le menu principal, gestion de jouer de nouveau n'a pas été developpé
    while True:
        try:
            print("Tapez Entrée pour retourner au menu principale ")
            sortie = input()
            if isinstance(str(sortie), str) and str(sortie.lower()) == "entrée":
                return resulat_joueur
            else:
                raise ValueError

        except ValueError as msg:
            print("Votre Choix est incorrect !! Merci de reselectionner 1 !")


# appel de la fonction main()
def main():
    choix = False  # c'est par defaut non pour la selction d'un nom à chercher dans le fichier
    if __name__ == "__main__":
        while True:
            # gestion des erreurs du clavier
            try:
                reponse = affichage.afficher_menu_principale()
                if isinstance(int(reponse), int) and (4 > int(reponse) > 0):
                    # il doit etre entier et entre 0 et 3 uniquement si non declanche un erreur

                    if int(reponse) == 3:
                        # pour quitter le programme
                        print("...........................Fin du Jeu.................................")
                        break
                    elif int(reponse) == 1:
                        # pour aficher les resultats dans les fichiers

                        c = affichage.afficher_menu_resultats()  # recuperation du choix d'affichage par text/json
                        if int(c) == 1:  # afficher resultat fichhier  text

                            affichage.afficher_fichier_txt(
                                DATA.TXT_FILE)  # afficher pa defaut le contenu du fichier txt
                            choix = affichage.get_nom_pour_chercher_ses_resultats()  # recuperation du chioix de rechercher par nom
                            if len(choix) > 0:
                                recherche(DATA.TXT_FILE, choix)
                        elif int(c) == 2:  # afficher resultat fichhie1r  JSON

                            affichage.afficher_fichier_json(
                                DATA.JSON_FILE)  # afficher pa defaut le contenu du fichier json
                            choix = affichage.get_nom_pour_chercher_ses_resultats()  # recuperation du chioix de rechercher par nom
                            if len(choix) > 0:
                                recherche(DATA.JSON_FILE, choix)
                    elif int(reponse) == 2:
                        nom_joueur = ""
                        # print("nouvelle partie")
                        nom_joueur = (affichage.get_nom_joueur())  # Tapez le nom du jouer
                        valeur_chercher = random.randint(DATA.VALEUR_MINI,
                                                         DATA.VALEUR_MAXI)  # recuperation le juste prix
                        # la liste resltat contient nombre tentatives et temps
                        resulat = jouer(valeur_chercher)  # resultat du jeux
                        sauvegarde(DATA.TXT_FILE,[nom_joueur, resulat[0], resulat[1], valeur_chercher],[])  # sauvegarder dans un fichier txt
                        sauvegarde(DATA.JSON_FILE,[nom_joueur, resulat[0], resulat[1], valeur_chercher], DATA.HEAD_FICHIER_JSON)  # sauvegarder dans un fichier json
                else:
                    # s' il a tapez un nombre supreirer à 4 ou inferieur 0
                    raise ValueError

            except ValueError as msg:
                print("Votre Choix est incorrect !! Merci de reselectionner 2 !")




"""
main.py : fichier principal
package Resultats : contient fichier gestion.py ou il y a deux fonctions "recherche" et "sauvegarde" pour les deux fichier json et txt
donnees.py : contient les declarations
affichage.py : contient les fonctions d'affichages (menus, données de fichiers,...)
"""

# programme principal
main()
