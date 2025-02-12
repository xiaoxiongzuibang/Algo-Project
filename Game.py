import random as rnd

from CreatSet import *
class Game:
    def __init__(self,french_words):
        self.words = french_words
        self.alphabet =['a','b','c','d','e','f','g','h','i','j','k','l',
                    'm','n','o','p','q','r','s',
                    't','u','v','w','x','y','z']
        self.probability = [8.45, 1.06, 3.03, 3.55, 17.26, 1.11, 1.23, 1.11, 7.34, 0.34,
                            0.05, 5.46, 2.97, 7.13, 5.26, 2.79, 1.36, 6.55, 7.91, 7.11,
                            6.05, 1.83, 0.04, 0.42, 0.30, 0.15]

    def generate_board(self):
        board = [[rnd.choices(self.alphabet,self.probability) [0]
                  for _ in range(4)] for _ in range(4)]
        return board



game = Game(french_words)
board = game.generate_board()
print(board)
