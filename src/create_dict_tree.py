# script to create a tree structure of the dictionary

# TODO: Add is_word to Node class
# TODO: Add sequence to Node class to store words (might not be 100% required but useful for debugging)
# TODO: Absorb the first layer of iteration into the recursive function, doesn't make sense to have duplicated code in the main
# TODO: [Optional] Fix up maybe how we represent letters, it's a bit all over the place currently and hard-coded for English

import json

# Filepath
DICTIONARY_NAME = 'src/en_dict.txt'
# Letters that are supported 
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Node that composed the tree structure that will be traverse
class Node:
    letter = ''
    edges = [] #node can have up to 26 edges with current english alphabet
    depth = 0

    def __init__(self, letter, depth):
        self.letter = letter
        self.edges = []
        self.depth = depth

    # Print fucntion that traverse the whole tree
    def traverse_tree(self):
        spaces = ' '*self.depth
        print(spaces + self.letter)

        for node in self.edges:
            node.traverse_tree()


def get_sub_dict(dict, sequence):
    """ 
        Return a filtered version of the dictionary matching the sequence of interest O(n)
        dict: list representing the current word in the dictionary
        sequence: the current sequence of words to filter the dict with

        return the filtered sub dictionary
    """
    
    sub_dict = []
    for word in dict:
        if word.startswith(sequence):
            sub_dict.append(word)

    return sub_dict    

def get_longest_word(dict):
    """ return the longest word out of the dictionary list O(n)"""

    longest_word_len = 0

    for word in dict:
        if len(word) > longest_word_len:
            longest_word_len = len(word)
    
    return longest_word_len


def recurse_letters_all(letter_i, sequence, dict, sub_tree, cur_depth, max_depth):
    """
        Recursively create and add nodes in the alphabetical decision tree.
        
        letter_i: index of the letter currently being used
        sequence: the sequence of characters that make up a potential word
        dict: the current sub dictionary that could match the sequence
        sub_tree: the tree onto which this letter originated and upon which nodes will be appended
        cur_depth: the current depth of the letter in the full tree.
        max_depth: the max depth allowed in the full tree (used to stop and equal to longest word in dictionary)

        return nothing as it only populate the nodes in the tree
    """

    # recursion stop when we hit the max depth allowed
    if cur_depth == max_depth:
        return

    # creation of the new sequence of letters and filtering of the dictionary to match
    new_sequence = sequence + LETTERS[letter_i]
    new_depth = cur_depth + 1
    new_sub_dict = get_sub_dict(dict, new_sequence)

    # if there is something matching this sequence we continue recursing
    # otherwise we stop as this sequence is depleted from available characters
    if new_sub_dict:
                
        # Iterate on each letters of the alphabet
        for letter_i in range(26):
            
            # Create the node and append it to the tree
            node = Node(LETTERS[letter_i], new_depth)
            sub_tree.edges.append(node)
            
            # Recurse with the new parameters
            recurse_letters_all(letter_i, new_sequence, new_sub_dict, node, new_depth, max_depth)

if __name__ == '__main__':
    # Load the dictionary so that we can manipulate it

    # Load the boggle file data
    with open(DICTIONARY_NAME) as file:
        file_data = file.read().splitlines()
    
    # Establish how much depth in the tree we want to allow 
    max_depth = get_longest_word(file_data)

    # The tree that will contains all
    tree = Node('', 0)

    # Iterate on the first layer of the tree
    for letter_i in range(26):
        
        print(f"{letter_i}")

        node = Node(LETTERS[letter_i], 1)
        tree.edges.append(node)

        recurse_letters_all(letter_i, '', file_data, node, 0, max_depth)

    tree.traverse_tree()
