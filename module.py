import formes
class ModuleTetris:
    def __init__(self, lignes, colonnes):
        self.__haut=lignes+4
        self.__larg=colonnes
        self.__base=4
        self.__terrain=[]
        for i in range(self.__haut):
            ligne=[]
            if i<4:
                for j in range(self.__larg):
                    ligne.append("-2")
                self.__terrain.append(ligne)
                ligne=[]
            else:
                for j in range(self.__larg):
                    ligne.append("-1")
                self.__terrain.append(ligne)
                ligne=[]
        print(self.__terrain)
    def get_largeur(self):
        return self.__larg
    def get_hauteur(self):
        return self.__haut

    def get_valeur(self, lig,col):
        return self.__terrain[lig][col]

    def est_occupe(self, lig,col):
        if self.get_valeur(lig,col)==0:
            return True
        else:
            return self.get_valeur(lig,col)

    def fini(self):
        for i in range(self.__larg):
            if self.est_occupe(4,i)==True:
                return True
        return False

#Zone de test du module

tet=ModuleTetris(1,4)
print(tet.est_occupe(4,2))
print(tet.fini())