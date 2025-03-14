import random
from Game import Game
import pandas as pd
from itertools import chain

df = pd.read_csv('dictionnaire_fr.csv')
french_words = list(df.iloc[:, 0].str.strip())

def available(position: list) -> bool:
    '''Judge position'''
    return 0 <= position[0] <= 3 and 0 <= position[1] <= 3

def monte_carlo_simulation(epoches: int, steps: int) -> list:
    '''
    The probability that more than 5 characters construct a word is small which we can ignore.
    Using Monte Carlo simulation for each character in the board.
    Only need to simulate for 2/3/4/5 steps and verify if they are in the dicitonary.
    '''
    direction = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
    simulation_path = []
    '''For each element in matrix'''
    for i in range(4):
        for j in range(4):
            '''epoches times simulation'''
            simulation_list = []
            for epoch in range(epoches):
                a = 0
                position_list = [[i,j]]
                current_i, current_j = i, j
                while a < steps-1:
                    dir = random.choice(direction)
                    if available([current_i+dir[0], current_j+dir[1]]):
                        new_position = [current_i+dir[0], current_j+dir[1]]
                        position_list.append(new_position)
                        current_i, current_j = new_position[0], new_position[1]
                        a += 1
                    else:
                        pass
                simulation_list.append(position_list)
            simulation_path.append(simulation_list)
    return simulation_path


def transformer(matrix: list, simulation_path: list) -> list:
    '''Transform the simulation path list to a word list'''
    steps = len(simulation_path[0][0])
    transform_result = []
    for element in range(16):
        word_list = []
        for epoch in range(len(simulation_path[1])):
            word = ''
            for step in range(steps):
                character = matrix[simulation_path[element][epoch][step][0]][simulation_path[element][epoch][step][1]]
                word = word + character
            word_list.append(word)
        transform_result.append(word_list)
    return list(chain.from_iterable(transform_result))

def next(dictionary: list, transform_result: list) -> list:
    unique_list = list(set(transform_result))
    result = [word for word in unique_list if word in dictionary]
    return result


# game = Game(french_words)
# board = game.generate_board()
# simulation_path = monte_carlo_simulation(10000, 5)
# transform_result = transformer(board, simulation_path)
# print(next(french_words, transform_result))
# print('list' in ['ilist'])


