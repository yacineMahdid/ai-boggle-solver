class Node:
    letter = ''
    edges = {} #node can have up to 26 edges with current english alphabet
    is_word = False
    sequence = ""

    def __init__(self, letter, sequence, is_word):
        self.letter = letter
        self.edges = {}
        self.sequence = sequence
        self.is_word = is_word