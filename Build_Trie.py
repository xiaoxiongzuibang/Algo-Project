from aem.kae import pASSpace
from pyarrow import dictionary
import numpy as np

from CreatSet import *

class Trie:
    def __init__(self):
        # 1. built a basic root 2. insert words form french_words 3. creat a test search approach
        self.root= {}
        self.root_board={}


    def insert_word(self, word):
        # insert each letter of a word to a dictionary
        # if it is already there , pass , if not creat a new node
        node = self.root
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node["#"] = True


    def starts_with(self, prefix):
        """前缀是否存在"""
        node = self.root
        prefix = prefix.lower()
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True

    def insert_dic(self, dictionary):
        for word in dictionary:
            self.insert_word(word)


    def search(self, word): #
        node = self.root
        for letter in word:
            if letter not in node:
                return False
            node = node[letter]
        return "#" in node







# build up the trie
















