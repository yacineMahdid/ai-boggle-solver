# script to create a tree structure of the dictionary

import json

# Filepath
DICTIONARY_NAME = 'src/en_dict.txt'
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

class Node:
    letter = ''
    edges = []
    depth = 0

    def __init__(self, letter, depth):
        self.letter = letter
        self.edges = []
        self.depth = depth

    def traverse_tree(self):
        spaces = ' '*self.depth
        print(spaces + self.letter)

        for node in self.edges:
            node.traverse_tree()


def get_sub_dict(dict, sequence):
    
    sub_dict = []
    for word in dict:
        if word.startswith(sequence):
            sub_dict.append(word)

    return sub_dict    

def get_longest_word(dict):

    longest_word_len = 0

    for word in dict:
        if len(word) > longest_word_len:
            longest_word_len = len(word)
    
    return longest_word_len

def recurse_letters_all(letter_i, sequence, dict, sub_tree, cur_depth, max_depth):

    if cur_depth == max_depth:
        return

    new_sequence = sequence + LETTERS[letter_i]
    new_depth = cur_depth + 1

    new_sub_dict = get_sub_dict(dict, new_sequence)

    if new_sub_dict:
                
        # Iterate on each letters
        for letter_i in range(26):
            
            node = Node(LETTERS[letter_i], new_depth)
            sub_tree.edges.append(node)
            
            recurse_letters_all(letter_i, new_sequence, new_sub_dict, node, new_depth, max_depth)

if __name__ == '__main__':
    # Load the dictionary so that we can manipulate it

    # Load the boggle file data
    with open(DICTIONARY_NAME) as file:
        file_data = file.read().splitlines()
    
    max_depth = get_longest_word(file_data)

    tree = Node('', 0)
    for letter_i in range(26):
        
        print(f"{letter_i}")

        node = Node(LETTERS[letter_i], 1)
        tree.edges.append(node)

        recurse_letters_all(letter_i, '', file_data, node, 0, max_depth)

    tree.traverse_tree()
