import doctest
from Groupe import *

class Sorciere :
    def __init__(self) :
        self.type = 'Sorcière'
        self.reveal = 'Vous êtes la sorcière, utilisez vos potions à bon escient.'
        self.potion_mort = 1
        self.potion_vie = 1
                
    ##############################
    ### Actions de la sorcière ###
    def action(self,liste_j) :
        for i in Village.liste_j :
            if i.vivant == False :
                
                #################################################
                ### Plus de potion de vie mais potion de mort ###
                if self.potion_vie == 0 :
                    print(i.pseudo + """ est mort, il était """ + i.role.type + """. Malheureusement, tu ne peux plus le réssuciter.
   Choisis-tu de ne rien faire (R) ou de tuer une autre personne (T) ?""")
                    reponse1 = input()
                    while reponse1 != "R" and reponse1 != "T" :
                        print("   Choisis-tu de ne rien faire (R) ou de tuer une autre personne (T) ?")
                        reponse1 = input()
                    
                    # Ne rien faire
                    if reponse1 == "R" :
                        print("   Tu as choisis de ne rien faire.")
   
                    # Tuer une autre personne
                    elif reponse1 == "T" :
                        print("""   Qui souhaites-tu tuer ? (Joueur X)""")
                        tuer = input()
                        while tuer !=  "Joueur 1" and tuer != "Joueur 2" and tuer != "Joueur 3" and tuer != "Joueur 4" and tuer != "Joueur 5" and tuer != "Joueur 6" and tuer != "Joueur 7" and tuer != "Joueur 8" :
                            print("   Inscris le joueur que tu souhaites empoisonner. (Joueur X)")
                            tuer = input()
                        if tuer == "Joueur 1" :
                            Village.liste_j[J1].vivant = False
                            self.potion_mort -= 1
                            print("""   Tu as choisis de tuer le joueur 1.""")
                        elif tuer == "Joueur 2" :
                            Village.liste_j[J2].vivant = False
                            self.potion_mort -= 1
                            print("""   Tu as choisis de tuer le joueur 2.""")
                        elif tuer == "Joueur 3" :
                            Village.liste_j[J3].vivant = False
                            self.potion_mort -= 1
                            print("""   Tu as choisis de tuer le joueur 3.""")
                        elif tuer == "Joueur 4" :
                            Village.liste_j[J4].vivant = False
                            self.potion_mort -= 1
                            print("""   Tu as choisis de tuer le joueur 4.""")
                        elif tuer == "Joueur 5" :
                            Village.liste_j[J5].vivant = False
                            self.potion_mort -= 1
                            print("""   Tu as choisis de tuer le joueur 5.""")
                        elif tuer == "Joueur 6" :
                            Village.liste_j[J6].vivant = False
                            self.potion_mort -= 1
                            print("""   Tu as choisis de tuer le joueur 6.""")
                        elif tuer == "Joueur 7" :
                            Village.liste_j[J7].vivant = False
                            self.potion_mort -= 1
                            print("""   Tu as choisis de tuer le joueur 7.""")
                        elif tuer == "Joueur 8" :
                            Village.liste_j[J8].vivant = False
                            self.potion_mort -= 1
                            print("""   Tu as choisis de tuer le joueur 8.""")
                
                #################################################            
                ### Potion de vie mais plus de potion de mort ###
                elif self.potion_mort == 0 :
                    print("   Le " + Village.i + " est mort. Souhaites-tu le faire revivre (V) ou ne rien faire (R) ?")
                    reponse = input()
                    while reponse != 'V' and reponse != 'R' :
                        print("   Souhaites-tu le faire revivre (V) ou ne rien faire (R) ?")
                        reponse = input()
                    # Réssuciter
                    if reponse == "V" :
                        i == True
                        print("   Le joueur renaît de ses cendres.")
                        self.potion_vie -= 1
                     
                    # Ne rien faire 
                    elif reponse == "R" :
                        print("   Tu as choisis de ne rien faire.")
                
                ########################################    
                ### Aucune des deux potions en stock ###
                elif self.potion_mort == 0 and self.potion_vie == 0 :
                    print(i.pseudo + " est mort, il était " + i.role.type + ". Tu n'as plus de potions, tu ne peux rien faire.")
                
                ######################################
                ### La sorcière a ses deux potions ###  
                elif self.potion_mort == 1 and self.potion_vie == 1 :
                    print(i.pseudo + " est mort, il était " + i.role.type + ". Souhaites-tu le faire revivre (V), ne rien faire (R), ou tuer quelqu'un d'autre (T) ?")
                    reponse = input()
                    while reponse != 'V' and reponse != 'T' and reponse != 'R' :
                        print("   Souhaites-tu le faire revivre (V), ne rien faire (R), ou tuer quelqu'un d'autre (T) ?")
                        reponse = input()
                        
                    # Réssuciter
                    if reponse == "V" :
                        i == True
                        print("   Le joueur renaît de ses cendres.")
                        self.potion_vie -= 1
                     
                    # Ne rien faire 
                    elif reponse == "R" :
                        print("   Tu as choisis de ne rien faire.")
                    
                    # Tuer une autre personne
                    elif reponse == "T" :
                        print("""   Qui souhaites-tu tuer ? (Joueur X)""")
                        tuer = input()
                        while tuer !=  "Joueur 1" and tuer != "Joueur 2" and tuer != "Joueur 3" and tuer != "Joueur 4" and tuer != "Joueur 5" and tuer != "Joueur 6" and tuer != "Joueur 7" and tuer != "Joueur 8" :
                            print("   Inscris le joueur que tu souhaites empoisonner. (Joueur X)")
                            tuer = input()
                        if tuer == "Joueur 1" :
                            Village.liste_j[J1].vivant = False
                            self.potion_mort -= 1
                            print("""   Tu as choisis de tuer le joueur 1.""")
                        elif tuer == "Joueur 2" :
                            Village.liste_j[J2].vivant = False
                            self.potion_mort -= 1
                            print("""   Tu as choisis de tuer le joueur 2.""")
                        elif tuer == "Joueur 3" :
                            Village.liste_j[J3].vivant = False
                            self.potion_mort -= 1
                            print("""   Tu as choisis de tuer le joueur 3.""")
                        elif tuer == "Joueur 4" :
                            Village.liste_j[J4].vivant = False
                            self.potion_mort -= 1
                            print("""   Tu as choisis de tuer le joueur 4.""")
                        elif tuer == "Joueur 5" :
                            Village.liste_j[J5].vivant = False
                            self.potion_mort -= 1
                            print("""   Tu as choisis de tuer le joueur 5.""")
                        elif tuer == "Joueur 6" :
                            Village.liste_j[J6].vivant = False
                            self.potion_mort -= 1
                            print("""   Tu as choisis de tuer le joueur 6.""")
                        elif tuer == "Joueur 7" :
                            Village.liste_j[J7].vivant = False
                            self.potion_mort -= 1
                            print("""   Tu as choisis de tuer le joueur 7.""")
                        elif tuer == "Joueur 8" :
                            Village.liste_j[J8].vivant = False
                            self.potion_mort -= 1
                            print("""   Tu as choisis de tuer le joueur 8.""")
            else :
                print("   Il n'y a pas eu de mort.")
                                    
    #############################
                            