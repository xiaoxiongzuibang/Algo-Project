from Game import Game
from GUI import GUI
from CreatSet import *

if __name__ == '__main__':
    game = Game(french_words)
    gui = GUI(game)
    gui.run()