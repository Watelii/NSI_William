class Joueur : 
    def __init__(self,pseudo,role):
        self.vivant  = True
        self.pseudo = pseudo
        self.role = role
        
    def reveal(self):
        print("Tu as le rôle : " + self.role.type)
        print(self.role.reveal)
        
    def __repr__(self) :
        return self.pseudo
    
class Village :
    def __init__(self,J1,J2,J3,J4,J5,J6,J7,J8,p = True) :
        self.liste_j = [J1,J2,J3,J4,J5,J6,J7,J8]
        self.joueurs_amoureux = []
        self.cupidon = [i for i in self.liste_j if i.role.type == 'Cupidon']
        self.lg = [i for i in self.liste_j if i.role.type == 'Loup-garou']
        self.vol = [i for i in self.liste_j if i.role.type == 'Voleur']
        self.liste_joueur_lg = [i for i in self.liste_j if i.role.type == 'Cupidon' and 'Villageois' and 'Soricère' and 'Voyante' and 'Cupidon' and 'Voleur']