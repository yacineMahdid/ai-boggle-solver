# script to create a tree structure of the dictionary

import pickle 
from helper import Node

# Filepath
DICTIONARY_NAME = 'src/en_dict.txt'
# Letters that are supported 
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

global WORD_COUNT
WORD_COUNT = 0


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

def recurse_letters_all(sequence, dict, sub_tree):
    """
        Recursively create and add nodes in the alphabetical decision tree.
        
        sequence: current sequence of character up to this point
        dict: the current sub dictionary that could match the sequence
        sub_tree: the tree onto which this letter originated and upon which nodes will be appended
        
        return nothing as it only populate the nodes in the tree
    """

    # Iterate on each letters of the alphabet
    for letter_i in range(len(LETTERS)):

        # creation of the new sequence of letters and filtering of the dictionary to match
        new_sequence = sequence + LETTERS[letter_i]
        new_sub_dict = get_sub_dict(dict, new_sequence)

        # if there is something matching this sequence we continue recursing
        # otherwise we stop as this sequence is depleted from available characters
        if new_sub_dict:
            
            # check if this sequence is a word
            is_word = is_sequence_a_word(new_sub_dict, new_sequence)

            # Printing the words with a hacky global variable
            if is_word:
                global WORD_COUNT
                WORD_COUNT = WORD_COUNT + 1
                print(f"Total number of word = {WORD_COUNT} and word is {new_sequence}")

            # Create the node and append it to the tree
            node = Node(LETTERS[letter_i], new_sequence, is_word)
            sub_tree.edges[LETTERS[letter_i]] = node
            
            # Recurse with the new parameters
            recurse_letters_all(new_sequence, new_sub_dict, node)

if __name__ == '__main__':
    # Load the dictionary so that we can manipulate it

    # Load the boggle file data
    with open(DICTIONARY_NAME) as file:
        file_data = file.read().splitlines()

    # The tree that will contains all
    tree = Node('', '', False)

    # Populate the tree
    recurse_letters_all('', file_data, tree)

    file_pi = open('eng_tree.obj', 'wb') 
    pickle.dump(tree, file_pi)