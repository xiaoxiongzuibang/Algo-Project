from Game import Game
from GUI import GUI
from CreatSet import *
df = pd.read_csv('dictionnaire_fr.csv')
french_words = df.iloc[:, 0]

if __name__ == '__main__':
    game = Game(french_words)
    gui = GUI(game)
    gui.run()