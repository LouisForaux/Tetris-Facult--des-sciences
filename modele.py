from random import randint
LES_FORMES = [[(0,3),(0,0),(0,1),(0,2)],[(0,0),(1,0),(0,1),(1,1)],[(0,0),(1,0),(0,1),(-1,1)],[(0,0),(-1,0),(0,1),(1,1)],[(-1,1),(-1,0),(0,0),(1,0)],[(0,0),(-1,0),(1,0),(1,1)],[(0,0),(-1,0),(1,0),(0,-1)]]
class ModeleTetris :
    '''c'est le terrain du modèle du jeu tetris'''
    
    def __init__(self, lig= 14, col= 24):
        '''ModeleTetris,int,int-->ModeleTetris'''
        self.__haut = lig + 4
        self.__larg = col
        self.__base = 4
        self.__terrain = []
        for i in range(self.__haut):
            liste =[]
            for j in range( self.__larg):
                if i < self.__base:
                    liste.append(-2)
                else:
                    liste.append(-1)
            self.__terrain.append(liste)
        self.__forme = Forme(self)

        self.__score=0

    def get_largeur(self):
        '''ModeleTetris->int'''
        return self.__larg

    def get_hauteur(self):
        '''ModeleTetris->int'''
        return self.__haut

    def get_valeur(self, lig,col):
        '''ModeleTetris,int,int->(int,int)'''
        return self.__terrain[lig][col]

    def est_occupe(self,lig,col):
        '''ModeleTetris,int,int-> booleen'''
        if self.get_valeur(lig,col) == -1 or self.get_valeur(lig,col) == -2:
            return False
        else:
            return True

    def fini(self):
        '''ModeleTetris->booeleen'''
        for i in self.__terrain[self.__base]:
            if i >= 0:
                return True
        return False

    def ajoute_forme(self):
        '''ModeleTetris->None'''
        li = self.__forme.get_coords()
        for i in li:
            self.__terrain[i[1]][i[0]] = self.__forme.get_couleur()

    def forme_tombe(self):
        '''ModeleTetris->booleen'''
        if not self.__forme.tombe():
            return False
        else:
            self.ajoute_forme()
            self.__forme = Forme(self)
            return True

    def get_couleur_forme(self):
        '''ModeleTetris->'''
        return self.__forme.get_couleur()

    def get_coords_forme(self):
        return self.__forme.get_coords()

    def forme_a_gauche(self):
        self.__forme.a_gauche()

    def forme_a_droite(self):
        self.__forme.a_droite()

    def forme_tourne(self):
        self.__forme.tourne()

    def est_ligne_complete(self, lig):
        occ=0
        tot=0
        for i in range(len(self.__terrain[self.__larg])):
            if self.est_occupe(lig, i):
                occ+=1
            tot+=1
        if tot==occ:
            return True
        return False
    
        

class Forme:

    def __init__(self,ModeleTetris):
        self.__modele= ModeleTetris
        ket = randint(0,6)
        self.__couleur = ket
        self.__forme = LES_FORMES[ket]
        self.__x0= randint(2,self.__modele.get_largeur()-2)
        self.__y0= 1

    def get_couleur(self):
        return self.__couleur


    def get_coords(self):
        res= []
        for i in self.__forme:
            res.append((self.__x0+i[0], self.__y0+i[1]))
        return res

    def collision(self):
        li = self.get_coords()
        for i in li:
            if i[1]+1 == self.__modele.get_hauteur():
                return True
            if (self.__modele.est_occupe(i[1]+1, i[0])):
                
                return True
        return False

    def tombe(self):
        if self.collision() == True:
            return True
        else:
            self.__y0+=1
            return False
    def position_valide(self):
        for couple_coords in self.get_coords():
            if couple_coords[0] < 0 or couple_coords[0] >= self.__modele.get_largeur():
                return False
            if couple_coords[1] > self.__modele.get_hauteur():
                return False
            if self.__modele.est_occupe(couple_coords[1],couple_coords[0]):
                return False
        return True

    def a_gauche(self):
        self.__x0 -=1
        if not self.position_valide():
            self.__x0 += 1

    def a_droite(self):
        self.__x0 += 1
        if not self.position_valide():
            self.__x0 -= 1

    def tourne(self):
        forme_prec = self.__forme
        
        self.__forme =[]
        for couple_coords in forme_prec:
            self.__forme.append((couple_coords[1]*-1,couple_coords[0]))
        if not self.position_valide():
            self.__forme = forme_prec
    
        
                                        
                                        

    
                
