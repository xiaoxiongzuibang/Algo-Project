from tkiteasy import *
import tkinter as tk
#from Game import Game

class GUI:
    def __init__(self, game):
        self.game = game
        self.root = ouvrirFenetre(1000,600)
        self.matrix = game.generate_board()
        self.letter_list = []

    def initialization(self):
        self.root.dessinerRectangle(0, 0, 1000, 600, "orange")
        self.root.afficherTexte("Entrez un mot et cliquez sur 'Confirmer'",
                                800, 50, "black", 20)
        self.root.afficherTexte("'Soumettre': valider votre réponse.",
                                800, 75, "black", 20)
        self.root.dessinerLigne(600, 0, 600, 600, "black", 5)
        self.root.dessinerLigne(600, 100, 1000, 100, "black", 5)

    def command(self, letter):
        self.letter_list.append(letter)
        for i in range(len(self.letter_list)):
            self.root.afficherTexte(self.letter_list[i], 700+12*i, 120, "black", 20)

    def letter_factory(self):
        """Letter Button: let player to chose their letters"""
        for i in range(4):
            for j in range(4):
                letter = self.matrix[i][j]
                letter_button = tk.Button(self.root, text=letter,font=("Arial", 25, "bold"), command=lambda l=letter: self.command(l))
                letter_button.place(x=i*150+50, y=j*150+50, width=70, height=70)

        """Confirmer Button: let player to finish one particular word"""
        confirmer_button = tk.Button(self.root, text=letter, font=("Arial", 25, "bold"),
                                  command=lambda l=letter: self.command(l))
        confirmer_button.place(x=i * 150 + 50, y=j * 150 + 50, width=70, height=70)

        """Soumettre Button: let player to finish the game and get the result"""
        soumettre_button = tk.Button(self.root, text=letter, font=("Arial", 25, "bold"),
                                  command=lambda l=letter: self.command(l))
        soumettre_button.place(x=i * 150 + 50, y=j * 150 + 50, width=70, height=70)
    def run(self):
        self.initialization()
        self.letter_factory()
        self.root.mainloop()
