import doctest
from Groupe import *

class Cupidon :
    def __init__(self) :
        self.type = 'Cupidon'
        self.reveal = "Vous êtes Cupidon. Rendez amoureux qui vous souhaitez, leur amour sera mortel."
        
    def action(self):
        print("   Quel joueur 1 souhaites-tu rendre amoureux ? Son amour pour l'autre sera mortel. (Joueur X)")
        action_cupidon1 = input()
        while action_cupidon1 !=  "Joueur 1" and action_cupidon1 != "Joueur 2" and action_cupidon1 != "Joueur 3" and action_cupidon1 != "Joueur 4" and action_cupidon1 != "Joueur 5" and action_cupidon1 != "Joueur 6" and action_cupidon1 != "Joueur 7" and action_cupidon1 != "Joueur 8" :
            print("   Inscris la personne que tu souhaites rendre amoureuse. (Joueur X)")
            action_cupidon1 = input()
        print("   Quel joueur 2 souhaites-tu rendre amoureux ? Son amour pour l'autre sera mortel. (Joueur Y)")
        action_cupidon2 = input()
        while action_cupidon2 !=  "Joueur 1" and action_cupidon2 != "Joueur 2" and action_cupidon2 != "Joueur 3" and action_cupidon2 != "Joueur 4" and action_cupidon2 != "Joueur 5" and action_cupidon2 != "Joueur 6" and action_cupidon2 != "Joueur 7" and action_cupidon2 != "Joueur 8" :
            print("   Inscris la deuxième personne que tu souhaites rendre amoureuse. (Joueur Y)")
            if action_cupidon2 == action_cupidon1 :
                print("   Tu ne peux pas mettre deux fois la même personne en couple.")
            action_cupidon2 = input()
            
        for i in Village.liste_j :
            if action_cupidon1 == i.pseudo or action_cupidon2 == i.pseudo:
                Village.joueurs_amoureux.append(i)
        
C = Cupidon()

