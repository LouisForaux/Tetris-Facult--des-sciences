from tkinter import *
import modele
DIM = 30
COULEURS = ["red","blue","green","yellow","orange","purple","pink",
            "dark grey","black"]
x1= modele.ModeleTetris()
class VueTetris:

    def __init__(self, ModeleTetris):
        self.__modele = ModeleTetris
        self.__fenetre= Tk()
        self.__fenetre.title("Tetris")
        self.__can_terrain = Canvas(self.__fenetre, width =self.__modele.get_largeur()*DIM, height =self.__modele.get_hauteur()*DIM)
        self.__can_terrain.pack(side ='left')
        frame = Frame(self.__fenetre)
        btn_quitter = Button(frame, text="quitter" , command = self.__fenetre.destroy)
        btn_quitter.pack()
        frame.pack(side ='right')
        self.__les_cases = []
        
        for i in range(self.__modele.get_hauteur()):
            liste =[]
            for j in range( self.__modele.get_largeur()):
                liste.append(self.__can_terrain.create_rectangle(j*DIM,i*DIM,DIM*self.__modele.get_largeur(),DIM*self.__modele.get_hauteur(),outline ="grey", fill= COULEURS[self.__modele.get_valeur(i,j)]))
            self.__les_cases.append(liste)
        
        
    def fenetre(self):
        return self.__fenetre

    def dessine_case(self,i,j,coul):
        self.__can_terrain.itemconfigure(self.__les_cases[i][j],fill = COULEURS[coul])

    def dessine_terrain(self):
        for i in range(0,self.__modele.get_hauteur()):
            ligne =[]
            for j in range(0,self.__modele.get_largeur()):
                self.dessine_case(i,j,self.__modele.get_valeur(i,j))

    def dessine_forme(self, coords, couleur):
        for i in coords :
            self.dessine_case(i[1],i[0], couleur)


    
