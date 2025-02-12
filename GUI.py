from tkiteasy import *
#from Game import Game

class GUI:
    def __init__(self, game):
        self.game = game
        self.root = ouvrirFenetre(2000,2000)
        self.matrix = game.generate_board()

    def initialization(self):
        for i in range(6):
            for j in range(6):
                self.root.dessinerRectangle(i*200, j*200, 500, 500, "orange")
                self.root.afficherTexte(self.matrix[i][j], i*200+100, j*200+100, col="black", sizefont=70)

    def run(self):
        self.initialization()
        self.root.mainloop()
