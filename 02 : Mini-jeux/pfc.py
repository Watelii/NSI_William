import random 
import doctest
from time import sleep

def pfc() :
    victoires = 0
    egalites = 0
    défaites = 0
    nb_manches = 0
    print("En combien de manches gagnantes veux-tu jouer ?")
    reponse = int(input())
    while victoires < reponse and défaites < reponse :
        print('Pierre, Feuille ou Ciseaux ? (P/F/C)')
        choix = input()
        #if choix != 'P' or 'F' or 'C' :
         #   print("Inscris P, F ou C.")
        options = ['P', 'F', 'C']
        choix_pc = random.choice(options)
        if choix == choix_pc :
            egalites += 1
            sleep(0.5)
            print("Egalité.")
            nb_manches += 1
            sleep(0.5)
        elif choix == 'P' and choix_pc == 'F' :
            défaites += 1
            sleep(0.5)
            print("Tu as perdu.")
            nb_manches += 1
            sleep(0.5)
        elif choix == 'P' and choix_pc == 'C' :
            victoires += 1
            sleep(0.5)
            print("Tu as gagné !")
            nb_manches += 1
            sleep(0.5)
        elif choix == 'C' and choix_pc == 'F' :
            victoires += 1
            sleep(0.5)
            print("Tu as gagné !")
            nb_manches += 1
            sleep(0.5)
        elif choix == 'C' and choix_pc == 'P' :
            défaites += 1
            sleep(0.5)
            print("Tu as perdu.")
            nb_manches += 1
            sleep(0.5)
        elif choix == 'F' and choix_pc == 'C' :
            défaites += 1
            sleep(0.5)
            print("Tu as perdu.")
            nb_manches += 1
            sleep(0.5)
        elif choix == 'F' and choix_pc == 'P' :
            victoires += 1
            sleep(0.5)
            print("Tu as gagné !")
            nb_manches += 1
            sleep(0.5)
                
        if victoires == reponse :
            print("Tu as gagné contre l'ordinateur", victoires, "à", défaites, "donc en", nb_manches, "manches.")
        elif défaites == reponse :
            print("Tu as perdu contre l'ordinateur" , victoires, "à", défaites, "donc en", nb_manches,"manches.")
    
  
pfc()
