from tkiteasy import *
import tkinter as tk
import pandas as pd

df = pd.read_csv('./dictionnaire_fr.csv')
french_words = set(df.iloc[:, 0])

# data = {"word": ["nul", "non"]}
# french_words = set(pd.DataFrame(data).iloc[:, 0])

class GUI:
    def __init__(self, game):
        self.game = game
        self.root = ouvrirFenetre(1000,600)
        self.matrix = game.generate_board()
        self.letter_list = []
        self.word_list = []

    def initialization(self):
        self.root.dessinerRectangle(0, 0, 1000, 600, "orange")
        self.root.afficherTexte("Entrez un mot et cliquez sur 'Confirmer'",
                                800, 50, "black", 20)
        self.root.afficherTexte("'Soumettre': valider votre réponse.",
                                800, 75, "black", 20)
        self.root.afficherTexte("ANSWER",700, 275, "black", 20)
        self.root.afficherTexte("RESULT", 900, 275, "black", 20)
        self.root.dessinerLigne(600, 0, 600, 600, "black", 5)
        self.root.dessinerLigne(600, 100, 1000, 100, "black", 5)
        self.root.dessinerLigne(600, 250, 1000, 250, "black", 5)
        self.root.dessinerLigne(600, 550, 1000, 550, "black", 5)
        self.root.dessinerLigne(800, 250, 800, 550, "black", 5)

    def letter_command(self, letter):
        self.letter_list.append(letter)
        letter_id = self.root.afficherTexte(letter, 800, 150, "black", 50)
        self.root.after(250, lambda: self.root.supprimer(letter_id))
    def confirmer_command(self):
        word = "".join(self.letter_list)
        self.letter_list = []
        self.word_list.append(word)

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
        print(self.word_list)
        print(self.word_list[0] in french_words)

    def restart_command(self):
        self.word_list = []  # 清空已输入的单词
        self.letter_list = []  # 清空当前输入
        self.matrix = self.game.generate_board()  # 重新生成游戏棋盘
        self.root.supprimer()  # 清空所有绘制的内容
        self.initialization()  # 重新绘制界面
        self.letter_factory()  # 重新生成字母按钮


    def letter_factory(self):
        """Letter Button: let player to chose their letters"""
        for i in range(4):
            for j in range(4):
                letter = self.matrix[i][j]
                letter_button = tk.Button(self.root, text=letter,font=("Arial", 25, "bold"),
                                          command=lambda l=letter: self.letter_command(l))
                letter_button.place(x=i*150+50, y=j*150+50, width=70, height=70)

        """ Confirmer Button: let player to finish one particular word"""
        confirmer_button = tk.Button(self.root, text='CONFIRMER', font=("Arial", 10, "bold"),
                                  command=self.confirmer_command)
        confirmer_button.place(x=675, y=200, width=80, height=30)

        """Soumettre Button: let player to finish the game and get the result"""
        soumettre_button = tk.Button(self.root, text="SOUMETTRE", font=("Arial", 10, "bold"),
                                  command=self.soumettre_command)
        soumettre_button.place(x=825, y=200, width=80, height=30)

        """ Rsult Button: generate the result"""
        result_button = tk.Button(self.root, text='Resultat', font=("Arial", 10, "bold"),
                                     command=self.result_command)
        result_button.place(x=675, y=565, width=80, height=30)

        """ Rdstart Button: Restart the game"""
        restart_button = tk.Button(self.root, text='Restart', font=("Arial", 10, "bold"),
                                  command=self.restart_command)
        restart_button.place(x=825, y=565, width=80, height=30)

    def run(self):
        self.initialization()
        self.letter_factory()
        self.root.mainloop()
