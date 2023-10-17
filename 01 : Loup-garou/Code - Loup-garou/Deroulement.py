import doctest
from time import *
from Groupe import *

class Deroulement :
    def __init__(self) :
        pass
    
    def __repr__(self):
        return Deroulement.revelation(self), Deroulement.bilan(self), Deroulement.vote(self)
        
    def revelation(self):
        for i in Village.liste_j :
            i.reveal()
            print('   Entre OK')
            ok = input()
            while ok != 'OK' :
                print('   Entre bien OK en majuscules.')
                ok = input()
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            sleep(5)
            
    def bilan(self):
        for i in Village.liste_j :
            if i.vivant == False :
                print("   Cette nuit ", i.pseudo, "est mort. Il était ", i.role.type, ". Débatez pour débusquer les loups-garous qui l'ont dévoré. Vous avez 1 minute.")
                Village.liste_j.remove(i)
                # sleep(60)
                
    def vote(self):
        print("   Débatez puis votez la personne que vous souhaitez éliminer. Lorsque la majorité a désignée une personne, inscrivez-la. (Joueur X)")
        votes = input()
        while votes !=  "Joueur 1" and votes != "Joueur 2" and votes != "Joueur 3" and votes != "Joueur 4" and votes != "Joueur 5" and votes != "Joueur 6" and votes != "Joueur 7" and votes != "Joueur 8" :
            print('   Inscrivez la personne que vous souhaitez éliminer. (Joueur X)')
            votes = input()
        if votes == "Joueur 1" :
            if Village.liste_j(J1).vivant == False :
                print("   Cette personne est déjà morte.")
                votes = input
            elif Village.liste_j(J1) not in Village.liste_j :
                print("   Cette personne est déjà morte.")
                votes = input
            else :
                Village.liste_j(J1).vivant = False
                Village.liste_j.remove(J1)
            print("""   La majorité a voté contre le joueur 1.""")
        elif votes == "Joueur 2" :
            if Village.liste_j(J2).vivant == False :
                print("   Cette personne est déjà morte.")
                votes = input
            elif Village.liste_j(J2) not in Village.liste_j :
                print("   Cette personne est déjà morte.")
                votes = input
            else :
                Village.liste_j(J2).vivant = False
                Village.liste_j.remove(J2)
            print("""   La majorité a voté contre le joueur 2.""")
        elif votes == "Joueur 3" :
            if Village.liste_j(J3).vivant == False :
                print("   Cette personne est déjà morte.")
                votes = input
            elif Village.liste_j(J3) not in Village.liste_j :
                print("   Cette personne est déjà morte.")
                votes = input
            else :
                Village.liste_j(J3).vivant = False
                Village.liste_j.remove(J3)
            print("""   La majorité a voté contre le joueur 3.""")
        elif votes == "Joueur 4" :
            if Village.liste_j(J4).vivant == False :
                print("   Cette personne est déjà morte.")
                votes = input
            elif Village.liste_j(J4) not in Village.liste_j :
                print("   Cette personne est déjà morte.")
                votes = input
            else :
                Village.liste_j(J4).vivant = False
                Village.liste_j.remove(J4)
            print("""   La majorité a voté contre le joueur 4.""")
        elif votes == "Joueur 5" :
            if Village.liste_j(J5).vivant == False :
                print("   Cette personne est déjà morte.")
                votes = input
            elif Village.liste_j(J5) not in Village.liste_j :
                print("   Cette personne est déjà morte.")
                votes = input
            else :
                Village.liste_j(J5).vivant = False
                Village.liste_j.remove(J5)
            print("""   La majorité a voté contre le joueur 5.""")
        elif votes == "Joueur 6" :
            if Village.liste_j(J6).vivant == False :
                print("   Cette personne est déjà morte.")
                votes = input
            elif Village.liste_j(J6) not in Village.liste_j :
                print("   Cette personne est déjà morte.")
                votes = input
            else :
                Village.liste_j(J6).vivant = False
                Village.liste_j.remove(J6)
            print("""   La majorité a voté contre le joueur 6.""")
        elif votes == "Joueur 7" :
            if Village.liste_j(J7).vivant == False :
                print("   Cette personne est déjà morte.")
                votes = input
            elif Village.liste_j(J7) not in Village.liste_j :
                print("   Cette personne est déjà morte.")
                votes = input
            else :
                Village.liste_j(J7).vivant = False
                Village.liste_j.remove(J7)
            print("""   La majorité a voté contre le joueur 7.""")
        elif votes == "Joueur 8" :
            if Village.liste_j(J8).vivant == False :
                print("   Cette personne est déjà morte.")
                votes = input
            elif Village.liste_j(J8) not in Village.liste_j :
                print("   Cette personne est déjà morte.")
                votes = input
            else :
                Village.liste_j(J8).vivant = False
                Village.liste_j.remove(J8)
            print("""   La majorité a voté contre le joueur 8.""")
            
D = Deroulement()
