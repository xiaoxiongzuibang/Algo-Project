from Game import Game
from GUI import GUI

if __name__ == '__main__':
    game = Game()
    gui = GUI(game)
    gui.run()