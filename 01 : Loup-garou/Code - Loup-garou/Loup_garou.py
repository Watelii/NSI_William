import doctest
from Groupe import *

class Loup_garou :
    def __init__(self) :
        self.type = 'Loup-garou'
        self.reveal = "Vous êtes un loup-garou. Dévorez le village et restez à l'abris des suspicions."
    
    def action(self) :
        print("   Qui souhaitez-vous dévorer ? (Joueur X)")
        manger = input()
        while manger !=  "Joueur 1" and manger != "Joueur 2" and manger != "Joueur 3" and manger != "Joueur 4" and manger != "Joueur 5" and manger != "Joueur 6" and manger != "Joueur 7" and manger != "Joueur 8" :
            print("   Inscrivez le joueur que vous souhaitez dévorer. (Joueur X)")
            manger = input()
        if manger == "Joueur 1" :
            Village.liste_j[J1].vivant = False
            print("""   Vous avez choisi de dévorer le joueur 1.""")
        elif manger == "Joueur 2" :
            Village.liste_j[J2].vivant = False
            print("""   Vous avez choisi de dévorer le joueur 2.""")
        elif manger == "Joueur 3" :
            Village.liste_j[J3].vivant = False
            print("""   Vous avez choisi de dévorer le joueur 3.""")
        elif manger == "Joueur 4" :
            Village.liste_j[J4].vivant = False
            print("""   Vous avez choisi de dévorer le joueur 4.""")
        elif manger == "Joueur 5" :
            Village.liste_j[J5].vivant = False
            print("""   Vous avez choisi de dévorer le joueur 5.""")
        elif manger == "Joueur 6" :
            Village.liste_j[J6].vivant = False
            print("""   Vous avez choisi de dévorer le joueur 6.""")
        elif manger == "Joueur 7" :
            Village.liste_j[J7].vivant = False
            print("""   Vous avez choisi de dévorer le joueur 7.""")
        elif manger == "Joueur 8" :
            Village.liste_j[J8].vivant = False
            print("""   Vous avez choisi de dévorer le joueur 8.""")
        
        