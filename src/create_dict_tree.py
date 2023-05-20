# script to create a tree structure of the dictionary

# TODO: Save the tree in the repository so that I can load it in the main function
# TODO: [Optional] Fix up maybe how we represent letters, it's a bit all over the place currently and hard-coded for English

# BUG: Depth variable seems to be absolutely useless

import json

# Filepath
DICTIONARY_NAME = 'src/en_dict.txt'
# Letters that are supported 
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

global WORD_COUNT
WORD_COUNT = 0

# Node that composed the tree structure that will be traverse
class Node:
    letter = ''
    edges = [] #node can have up to 26 edges with current english alphabet
    depth = 0
    is_word = False
    sequence = ""

    def __init__(self, letter, depth, sequence, is_word):
        self.letter = letter
        self.edges = []
        self.depth = depth
        self.sequence = sequence
        self.is_word = is_word


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

def is_sequence_a_word(dict, sequence):

    for word in dict:
        if word == sequence:
            return True
    return False

def get_longest_word(dict):
    """ return the longest word out of the dictionary list O(n)"""

    longest_word_len = 0

    for word in dict:
        if len(word) > longest_word_len:
            longest_word_len = len(word)
    
    return longest_word_len


def recurse_letters_all(sequence, dict, sub_tree, cur_depth, max_depth):
    """
        Recursively create and add nodes in the alphabetical decision tree.
        
        sequence: current sequence of character up to this point
        dict: the current sub dictionary that could match the sequence
        sub_tree: the tree onto which this letter originated and upon which nodes will be appended
        cur_depth: the current depth of the letter in the full tree.
        max_depth: the max depth allowed in the full tree (used to stop and equal to longest word in dictionary)

        return nothing as it only populate the nodes in the tree
    """

    #print(f"{cur_depth}")

    # recursion stop when we hit the max depth allowed
    if cur_depth == max_depth:
        return

    new_depth = cur_depth + 1

    # Iterate on each letters of the alphabet
    for letter_i in range(26):

        # creation of the new sequence of letters and filtering of the dictionary to match
        new_sequence = sequence + LETTERS[letter_i]
        new_sub_dict = get_sub_dict(dict, new_sequence)

        # if there is something matching this sequence we continue recursing
        # otherwise we stop as this sequence is depleted from available characters
        if new_sub_dict:
            
            # check if this sequence is a word
            is_word = is_sequence_a_word(new_sub_dict, new_sequence)

            if is_word:
                global WORD_COUNT
                WORD_COUNT = WORD_COUNT + 1
                print(f"Total number of word = {WORD_COUNT} and word is {new_sequence}")

            # Create the node and append it to the tree
            node = Node(LETTERS[letter_i], new_depth, new_sequence, is_word)
            sub_tree.edges.append(node)
            
            # Recurse with the new parameters
            recurse_letters_all(new_sequence, new_sub_dict, node, new_depth, max_depth)

if __name__ == '__main__':
    # Load the dictionary so that we can manipulate it

    # Load the boggle file data
    with open(DICTIONARY_NAME) as file:
        file_data = file.read().splitlines()
    
    # Establish how much depth in the tree we want to allow 
    max_depth = get_longest_word(file_data)

    # The tree that will contains all
    tree = Node('', 0, '', False)

    # Populate the tree
    recurse_letters_all('', file_data, tree, 0, max_depth)
