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
        # 将一个单词查人到树上去
        node = self.root
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node["#"] = True


    def starts_with(self, prefix):
    # check if the prefix of current word exisit
        node = self.root
        prefix = prefix.lower() #将字符串转换为小写
        for char in prefix:
            if char not in node: #如果字符不在字符上，则返回错误
                return False
            node = node[char] #检查每一个字符串上的元素是否在node上
        return True

    def insert_dic(self, dictionary):
        for word in dictionary:
            self.insert_word(word)
    # insert the dictionary to the form "trie"

    def search(self, word): # test
        node = self.root
        for letter in word:
            if letter not in node:
                return False
            node = node[letter]
        return "#" in node







# build up the trie
















