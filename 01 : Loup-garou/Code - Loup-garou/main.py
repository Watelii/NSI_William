import random
import doctest

from Groupe import *
from Loup_garou import *
from Sorciere import *
from Voyante_NSI import *
from Voleur import *
from Cupidon import *
from Villageois import *
from Deroulement import *

### Lancement des objets joueurs et du groupe village ###
roles = [Voyante(), Sorciere(), Cupidon(), Villageois(), Villageois(), Loup_garou(), Loup_garou(), Voleur()]

choix = random.choice(roles)
William = Joueur('William',choix)
roles.remove(choix)

choix2 = random.choice(roles)
Léo = Joueur('Léo',choix2)
roles.remove(choix2)

choix3 = random.choice(roles)
Enzo = Joueur('Enzo',choix3)
roles.remove(choix3)

choix4 = random.choice(roles)
Baptiste = Joueur('Baptiste',choix4)
roles.remove(choix4)

choix5 = random.choice(roles)
Bilel = Joueur('Bilel',choix5)
roles.remove(choix5)

choix6 = random.choice(roles)
Dimitri = Joueur('Dimitri',choix6)
roles.remove(choix6)

choix7 = random.choice(roles)
Ethan = Joueur('Ethan',choix7)
roles.remove(choix7)

choix8 = random.choice(roles)
Paul = Joueur('Paul',choix8)
roles.remove(choix8)

Village = Village(William,Léo,Enzo,Baptiste,Bilel,Dimitri,Ethan,Paul)
#########################################################
    
while Village.p == True :
    for i in Village.liste_j :
        if i.vivant == False :
            Village.liste_j.remove(i)
        if i.role.type == 'Loup-garou' not in Village.liste_j :
            Village.p = False
            print("   Les loups-garous ont gagnés !")
            break
        elif Village.liste_joueur_lg == Village.liste_j :
            Village.p = False
            print("   Le village a vaincu les loups-garous !")
            break
        
while Village.p == True :
    if Village.joueurs_amoureux[0].vivant == False :
        Village.joueurs_amoureux[-1].vivant = False
        for i in Village.liste_j :
            if i.vivant == False :
                Village.liste_j.remove(i)
    elif Village.joueurs_amoureux[-1].vivant == False :
        Village.joueurs_amoureux[0].vivant = False 
        for i in Village.liste_j :
            if i.vivant == False :
                Village.liste_j.remove(i)