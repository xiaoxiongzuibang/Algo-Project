from Game import Game
from GUI import GUI
from CreatSet import *
import os
import sys

df = pd.read_csv('dictionnaire_fr.csv')
french_words = df.iloc[:, 0]

if __name__ == '__main__':
    while True:
        game = Game(french_words)
        gui = GUI(game)
        gui.run()
        if not gui.state:
            os.execv(sys.executable, ['python'] + sys.argv)
        else:
            break
