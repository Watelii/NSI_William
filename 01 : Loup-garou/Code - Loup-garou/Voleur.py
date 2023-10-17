import doctest
from Groupe import *

class Voleur :
    def __init__(self) :
        self.type = 'Voleur'
    
    def action(self) :
        print("   Qui souhaites-tu voler le rôle ? (Joueur X)")
        voler = input()
        while voler !=  "Joueur 1" and voler != "Joueur 2" and voler != "Joueur 3" and voler != "Joueur 4" and voler != "Joueur 5" and voler != "Joueur 6" and voler != "Joueur 7" and voler != "Joueur 8" :
            print("   Inscris le joueur dont tu voler le rôle. (Joueur X)")
            voler = input()
        if voler == "Joueur 1" :
            print("   Tu as échangé ton rôle avec le joueur ", Village.liste_j[0], ". Tu es désormais ", Village.liste_j[0].role.type, ".")
            Village.vol[0].role.type = Village.liste_j[0].role.type
            Village.liste_j[0].role.type = 'Voleur'
        elif voler == "Joueur 2" :
            print("   Tu as échangé ton rôle avec le joueur ", Village.liste_j[1], ". Tu es désormais ", Village.liste_j[1].role.type, ".")
            Village.vol[0].role.type = Village.liste_j[1].role.type
            Village.liste_j[1].role.type = 'Voleur'
        elif voler == "Joueur 3" :
            print("   Tu as échangé ton rôle avec le joueur ", Village.liste_j[2], ". Tu es désormais ", Village.liste_j[2].role.type, ".")
            Village.vol[0].role.type = Village.liste_j[2].role.type
            Village.liste_j[2].role.type = 'Voleur'
        elif voler == "Joueur 4" :
            print("   Tu as échangé ton rôle avec le joueur ", Village.liste_j[3], ". Tu es désormais ", Village.liste_j[3].role.type, ".")
            Village.vol[0].role.type = Village.liste_j[3].role.type
            Village.liste_j[3].role.type = 'Voleur'
        elif voler == "Joueur 5" :
            print("   Tu as échangé ton rôle avec le joueur ", Village.liste_j[4], ". Tu es désormais ", Village.liste_j[4].role.type, ".")
            Village.vol[0].role.type = Village.liste_j[4].role.type
            Village.liste_j[4].role.type = 'Voleur'
        elif voler == "Joueur 6" :
            print("   Tu as échangé ton rôle avec le joueur ", Village.liste_j[5], ". Tu es désormais ", Village.liste_j[5].role.type, ".")
            Village.vol[0].role.type = Village.liste_j[5].role.type
            Village.liste_j[5].role.type = 'Voleur'
        elif voler == "Joueur 7" :
            print("   Tu as échangé ton rôle avec le joueur ", Village.liste_j[6], ". Tu es désormais ", Village.liste_j[6].role.type, ".")
            Village.vol[0].role.type = Village.liste_j[6].role.type
            Village.liste_j[6].role.type = 'Voleur'
        elif voler == "Joueur 8" :
            print("   Tu as échangé ton rôle avec le joueur ", Village.liste_j[7], ". Tu es désormais ", Village.liste_j[7].role.type, ".")
            Village.vol[0].role.type = Village.liste_j[7].role.type
            Village.liste_j[7].role.type = 'Voleur'
        
            
            
            
Vo = Voleur()