#coding: utf-8
import tkinter as tk
import tkinter.font as tkFont
from time import sleep
from PIL import ImageTk, Image


################################################################################
# classe ObjetGraphique
################################################################################
class ObjetGraphique():
    annuaire = {}
    def __init__(self, num, x, y, col):
        self.num = num
        self.x = x
        self.y = y
        self.col = col
        ObjetGraphique.annuaire[num] = self


################################################################################
# classe Canevas
################################################################################
class Canevas(tk.Canvas):
    def __init__(self, master, largeur,hauteur):
        tk.Canvas.__init__(self, master, width=largeur, height=hauteur, bg="black", confine=True)
# attributs
        self.master = master #la fenêtre hébergeant le canvas
        self.img = {} #pour stocker les images sinon elles sont garbagecollectées dès leur création lol
#         self.obj = {}
        self.lastkey = None #dernière touche tapée
        self.lastclic = None #dernier clic cliqué
        self.lastpos = 0,0 #dernière pos souris

# bindings
        self.bind_all("<Key>", self.evenementClavier)
        self.bind("<Button-1>", self.evenementClicG)
        self.bind("<Button-3>", self.evenementClicD)
        self.bind("<Motion>", self.evenementDeplaceSouris)
        self.pack()

################################################################################
# CREATION D'OBJETS
################################################################################

    def afficherTexte(self, txt, x, y, col="white", sizefont=18):
        font = tkFont.Font(family='Helvetica', size=sizefont, weight='normal')
        return ObjetGraphique(self.create_text(x,y,fill=col, text=txt, font=font), x, y, col)

    def dessinerRectangle(self, x, y, l, h, col):
        return ObjetGraphique(self.create_rectangle(x, y, x+l, y+h, fill=col, width=0), x, y, col)

    def dessinerLigne(self, x, y, x2, y2, col, ep=1):
        return ObjetGraphique(self.create_line(x, y, x2, y2, fill=col, cap='round', width=ep), x, y, col)

    def dessinerCercle(self, x, y, r, col):
        return ObjetGraphique(self.create_oval(x-r, y-r, x+r, y+r, width=1, outline=col), x, y, col)

    def dessinerDisque(self, x, y, r, col):
        return ObjetGraphique(self.create_oval(x-r, y-r, x+r, y+r, width=0, fill=col), x, y, col)

    def changerPixel(self, x, y, col):
        return ObjetGraphique(self.dessinerRectangle(x,y,1,1,col), x, y, col)

    def afficherImage(self, x, y, filename, sx=None, sy=None):
        image = Image.open(filename)
        if not image:
            print("Erreur: afficherImage",filename,": fichier incorrect")
            return
        if sx!=None and sy!=None:
            image = image.resize((sx,sy), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)
        self.img[img] = True
        self.create_rectangle(x, y, x+img.width()-1, y+img.height()-1, outline='')
        return ObjetGraphique(self.create_image(x, y, image=img, anchor="nw"), x, y, None)

# dessinerFleche: ne renvoit pas d'objet graphique
# N = longueur des branches de la flèche
    def dessinerFleche(self,x,y,x2,y2,N,col,ep=1):
        self.dessinerLigne(x,y,x2,y2,col,ep)
        vx,vy = x2-x,y2-y                   # vecteur initial
        m = max(abs(vx),abs(vy))
        vx /= m
        vy /= m                             # normalisation
        px,py = x2-vx*N,y2-vy*N             # point intermédiaire
        pvx,pvy = vy,-vx                    # 90°
        fx1,fy1 = px+pvx*N,py+pvy*N         # 1ère extrémité 
        fx2,fy2 = px-pvx*N,py-pvy*N         # 2nde extrémité
        self.dessinerLigne(x2,y2,fx1,fy1,col,ep)
        self.dessinerLigne(x2,y2,fx2,fy2,col,ep)

################################################################################
# MODIFICATEURS
################################################################################
    def deplacer(self, obj, x, y):
        obj.x += x
        obj.y += y
        self.move(obj.num,x,y)

    def supprimer(self, obj):
        self.delete(obj.num)
        del ObjetGraphique.annuaire[obj.num]
        obj = None

    def changerCouleur(self, obj, col):
        obj.col = col
        self.itemconfigure(obj.num, fill=col)

    def changerTexte(self, obj, txt):
        self.itemconfigure(obj.num, text=txt)
        
    def placerAuDessus(self,obj):
        if type(obj)==ObjetGraphique:
            self.tag_raise(obj.num)
        
    def placerAuDessous(self,obj):
        if type(obj)==ObjetGraphique:
            self.tag_lower(obj.num)

################################################################################
# EVENEMENTS
################################################################################
    def evenementClicG(self, event):
#         if event!=self.lastclic:
#             print("Mouse", event)
            self.lastclic = event

    def evenementClicD(self, event):
#         if event!=self.lastclic:
#             print("Mouse", event)
            self.lastclic = event

    def evenementClavier(self, event):
#         if event.keysym != self.lastkey:
#             print("Keyboard",event.keysym)#event, event.char)
            self.lastkey=event.keysym

    def evenementDeplaceSouris(self, event):
#         print("Move",event)#event, event.char)
        self.lastpos=(event.x, event.y)

    def recupererTouche(self):
#         print(self.lastkey)
        self.master.focus_force()
        self.update()
        touche = self.lastkey
        self.lastkey = None
        return touche

    def attendreTouche(self):
        touche = None
        while touche == None:
            self.pause(0.1)
            touche = self.recupererTouche()
        return touche

    def recupererClic(self):
        self.master.focus_force()
        self.update()
        clic = self.lastclic
        self.lastclic = None
        return clic

    def attendreClic(self):
        clic = None
        while clic==None:
            self.pause(0.1)
            clic = self.recupererClic()
        return clic

    def recupererPosition(self):
        self.master.focus_force()
        self.update()
        posx,posy = self.lastpos[0],self.lastpos[1]
        return ObjetGraphique(None,posx,posy,None)
    
    def recupererObjet(self, x, y):
        ido = self.find_overlapping(x, y, x, y)
        if not ido:
            return None
        return ObjetGraphique.annuaire[ido[-1]]

################################################################################
# AUTRES FONCTIONS
################################################################################
    def actualiser(self):
        self.update()

    def fermerFenetre(self):
        self.master.destroy()
            
    def pause(self, sleeptime=0.0005):
        sleep(sleeptime)



def ouvrirFenetre(x=400, y=200):
    racine = tk.Tk()
    #racine.protocol("WM_DELETE_WINDOW", qtk.quad.master.destroy)
    g = Canevas(racine, x, y)
#     tk.mainloop()
    return g




if __name__ == '__main__':
    ouvrirFenetre()
    tk.mainloop()
