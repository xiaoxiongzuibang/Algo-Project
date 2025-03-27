from tkiteasy import *
import tkinter as tk
from tkinter import messagebox
import pandas as pd
from MonteCarloSimulation import *
import time

df = pd.read_csv('./dictionnaire_fr.csv')
french_words = set(df.iloc[:, 0])

class GUI:
    def __init__(self, game):
        self.game = game
        self.state = True
        self.root = ouvrirFenetre(1000, 600)
        self.matrix = game.generate_board()
        self.letter_list = []
        self.word_list = []
        self.result = []
        self.button_list = []  
        self.button_matrix = [] 
        self.last_coord = None

    def initialization(self):
        self.root.dessinerRectangle(0, 0, 1000, 600, "orange")
        self.root.afficherTexte("Entrez un mot et cliquez sur 'Confirmer'",
                                 800, 50, "black", 20)
        self.root.afficherTexte("'Soumettre': valider votre réponse.",
                                 800, 75, "black", 20)
        self.root.afficherTexte("ANSWER", 700, 275, "black", 20)
        self.root.afficherTexte("RESULT", 900, 275, "black", 20)
        self.root.dessinerLigne(600, 0, 600, 600, "black", 5)
        self.root.dessinerLigne(600, 100, 1000, 100, "black", 5)
        self.root.dessinerLigne(600, 250, 1000, 250, "black", 5)
        self.root.dessinerLigne(600, 550, 1000, 550, "black", 5)
        self.root.dessinerLigne(800, 250, 800, 550, "black", 5)

        from Game import Game
        game = Game(french_words)
        found_words = game.generate_all_valid_words(self.matrix)
        self.result = found_words

    def letter_command(self, letter, button, row, col):
        # 如果已经选择过按钮，则检查当前按钮是否和上一次相邻（包括对角线）
        if self.last_coord is not None:
            last_row, last_col = self.last_coord
            if abs(row - last_row) > 1 or abs(col - last_col) > 1:
                messagebox.showwarning("Attention", "请选择与上一个按钮相邻或对角的按钮！")
                return 

        self.last_coord = (row, col)
        if button['state'] != tk.DISABLED:
            button.config(bg="gray", state=tk.DISABLED)
            self.letter_list.append(letter)
            letter_id = self.root.afficherTexte(letter, 800, 150, "black", 50)
            self.root.after(250, lambda: self.root.supprimer(letter_id))
        else:
            messagebox.showwarning("Attention", "You can not choose the same letter twice")

    def confirmer_command(self):
        word = "".join(self.letter_list)
        self.letter_list = []
        self.word_list.append(word)
        for button in self.button_list:
            button.config(state=tk.NORMAL, bg="SystemButtonFace")
        self.last_coord = None

    def soumettre_command(self):
        for i in range(len(self.word_list)):
            self.root.afficherTexte(f"{i+1}: {self.word_list[i]}", 670, 310+20*i, "black", 22)

    def result_command(self):
        from Game import Game
        game = Game(french_words)
        result_list, score = game.calculate_result_score(self.word_list)
        result_list = ["TRUE" if i == 1 else "FALSE" for i in result_list]
        for i in range(len(result_list)):
            self.root.afficherTexte(f"{i + 1}: {result_list[i]}", 875, 310 + 20 * i, "black", 22)
        self.root.afficherTexte(f"Accuracy/Précision：{format(score,'.2f')}%", 900, 525, "black", 15)
        self.end_time = time.time()
        total_time = self.end_time - self.start_time
        messagebox.showinfo('Resultat', f"Total Time: {round(total_time, 2)} seconds\nThese words are correct: {self.result}")

    def restart_command(self):
        self.state = False
        self.root.quit()

    def letter_factory(self):
        for i in range(4):
            row_buttons = []
            for j in range(4):
                letter = self.matrix[i][j]
                letter_button = tk.Button(self.root, text=letter, font=("Arial", 25, "bold"))
                letter_button.config(command=lambda l=letter, b=letter_button, r=i, c=j: self.letter_command(l, b, r, c))
                letter_button.place(x=i*150+50, y=j*150+50, width=70, height=70)
                self.button_list.append(letter_button)
                row_buttons.append(letter_button)
            self.button_matrix.append(row_buttons)

        """CONFIRMER"""
        confirmer_button = tk.Button(self.root, text='CONFIRMER', font=("Arial", 10, "bold"),
                                     command=self.confirmer_command)
        confirmer_button.place(x=675, y=200, width=80, height=30)

        """SOUMETTRE"""
        soumettre_button = tk.Button(self.root, text="SOUMETTRE", font=("Arial", 10, "bold"),
                                     command=self.soumettre_command)
        soumettre_button.place(x=825, y=200, width=80, height=30)

        """RESULTAT"""
        result_button = tk.Button(self.root, text='Resultat', font=("Arial", 10, "bold"),
                                  command=self.result_command)
        result_button.place(x=675, y=565, width=80, height=30)

        """RESTART"""
        restart_button = tk.Button(self.root, text='Restart', font=("Arial", 10, "bold"),
                                   command=self.restart_command)
        restart_button.place(x=825, y=565, width=80, height=30)

    def run(self):
        self.start_time = time.time()
        self.initialization()
        self.letter_factory()
        self.root.mainloop()

