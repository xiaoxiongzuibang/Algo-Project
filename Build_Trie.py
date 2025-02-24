
from CreatSet import *
from Game import board
class Trie:
    def __init__(self):
        # 1. built a basic root 2. insert words form french_words 3. creat a test search approach
        self.root = {}
        # self.root represent the basic root of our trie


    def insert_word(self, word):
        # insert each letter of a word to a dictionary
        # if it is already there , pass , if not creat a new node
        node = self.root
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node["#"] = True

    def search(self, word):
        node = self.root
        for letter in word:
            if letter not in node:
                return False
            node = node[letter]
        return "#" in node




trie = Trie()
for word in french_words:
    trie.insert_word(word)

test_words = ["bon",'c']
for word in test_words:
    print(f"'{word}' 在Trie中: {trie.search(word)}")
print(board)


