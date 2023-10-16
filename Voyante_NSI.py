import doctest
from Groupe import *

class Voyante :
    def __init__(self) :
        self.type = 'Voyante'
        self.reveal = "Vous êtes la voyante. Utilisez vos talents de vision pour dénicher les loups-garous, mais ne vous faites pas dévorer."
        self.personnes_vues = []
        
    def action(self) :
        print("   Sur quel joueur souhaites-tu exploiter tes talents de vision ? (Joueur X)")
        voir = input()
        while voir !=  "Joueur 1" and voir != "Joueur 2" and voir != "Joueur 3" and voir != "Joueur 4" and voir != "Joueur 5" and voir != "Joueur 6" and voir != "Joueur 7" and voir != "Joueur 8" :
            print("   Inscris le joueur dont tu veux connaître le rôle. (Joueur X)")
            voir = input()
        if voir == "Joueur 1" :
            print("   Tu as découvert " + Village.liste_j[J1].pseudo + ". Il est " + Village.liste_j[J1].role.type + ".")
            self.personnes_vues.append(Village.liste_j[J1].pseudo)
        elif voir == "Joueur 2" :
            print("   Tu as découvert " + Village.liste_j[J2].pseudo + ". Il est " + Village.liste_j[J2].role.type + ".")
            self.personnes_vues.append(Village.liste_j[J2].pseudo)
        elif voir == "Joueur 3" :
            print("   Tu as découvert " + Village.liste_j[J3].pseudo + ". Il est " + Village.liste_j[J3].role.type + ".")
            self.personnes_vues.append(Village.liste_j[J3].pseudo)
        elif voir == "Joueur 4" :
            print("   Tu as découvert " + Village.liste_j[J4].pseudo + ". Il est " + Village.liste_j[J4].role.type + ".")
            self.personnes_vues.append(Village.liste_j[J4].pseudo)
        elif voir == "Joueur 5" :
            print("   Tu as découvert " + Village.liste_j[J5].pseudo + ". Il est " + Village.liste_j[J5].role.type + ".")
            self.personnes_vues.append(Village.liste_j[J5].pseudo)
        elif voir == "Joueur 6" :
            print("   Tu as découvert " + Village.liste_j[J6].pseudo + ". Il est " + Village.liste_j[J6].role.type + ".")
            self.personnes_vues.append(Village.liste_j[J6].pseudo)
        elif voir == "Joueur 7" :
            print("   Tu as découvert " + Village.liste_j[J7].pseudo + ". Il est " + Village.liste_j[J7].role.type + ".")
            self.personnes_vues.append(Village.liste_j[J7].pseudo)
        elif voir == "Joueur 8" :
            print("   Tu as découvert " + Village.liste_j[J8].pseudo + ". Il est " + Village.liste_j[J8].role.type + ".")
            self.personnes_vues.append(Village.liste_j[J8].pseudo)
            
V = Voyante()