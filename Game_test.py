import random as rnd
import numpy as np
from CreatSet import *
from Build_Trie import *

class Game:
    def __init__(self, french_words):
        self.words = set(french_words)
        self.alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l',
                         'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.probability_2 = [0.0851, 0.0426, 0.0638, 0.0638, 0.1277,
                              0.0213, 0.0106, 0.0213, 0.0319, 0.0106,
                              0.0000, 0.0426, 0.0426, 0.0319, 0.0213,
                              0.0213, 0.0106, 0.0638, 0.0638, 0.0638,
                              0.0213, 0.0213, 0.0106, 0.0106, 0.0000,
                              0.0106]
        self.trie = Trie()
        self.trie.insert_dic(french_words)

    def generate_board(self):
        return [[rnd.choices(self.alphabet, self.probability_2)[0] for k in range(4)] for k in range(4)]


##API
    def calculate_result_score(self, input_list):
        valid_words = [word for word in input_list if word in self.words]
        score = (len(valid_words) / len(input_list)) * 100 if input_list else 0
        return valid_words, score


##find all valid words on board

    def find_words(self, board, i, j, visited, current_word, found_words):
        if not self.trie.starts_with(current_word):
            return

        if current_word in self.words:
            found_words.add(current_word)

        directions = [(-1,-1), (-1,0), (-1,1),
                      (0,-1), (0,1),
                      (1,-1),  (1,0), (1,1)]

        for dx, dy in directions:
            ni, nj = i+ dx, j + dy
            if 0 <= ni < 4 and 0 <= nj < 4 and not visited[ni][nj]:
                visited[ni][nj] = True
                self.find_words(board, ni, nj, visited, current_word + board[ni][nj], found_words)
                visited[ni][nj] = False

    def generate_all_valid_words(self, board):
        found_words = set()
        for i in range(4):
            for j in range(4):
                visited = [[False]*4 for k in range(4)]
                visited[i][j] = True
                self.find_words(board, i, j, visited, board[i][j], found_words)
        return list(found_words)

# example
game = Game(french_words)
board = game.generate_board()
found_words = game.generate_all_valid_words(board)
valid_words, score = game.calculate_result_score(found_words)

print(f"nombre des mots valide = : {len(valid_words)}")
print(f"score: {score:.2f}%")
print("les mots sont:", valid_words)