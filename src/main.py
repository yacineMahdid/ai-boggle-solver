# Command line python script to do the whole input -> output thing
# Will be called as follow:
# python main.py <name-of-file-containing-boggle-board>

import sys
import os
import copy
import json

from timeit import default_timer as timer
from datetime import timedelta

class Grid:
    """Object representation of a Boggle Grid capable of solving itself!"""
    letters = [] # letters in the grid
    dimension = 0 # the dimension of the board
    
    nodes = []
    adj_matrix = []

    dict_words = [] # words downloaded from the dictionary
    output_words = [] # the output words after the search

    def __init__(self, filepath, dictpath, seqpath):
        """Constructor who take a filepath for the grid and the location of a dictionary file"""

        # Load the boggle file data
        with open(filepath) as file:
            file_data = file.read().splitlines()
    
        # iterate on each row and store the letters + set the connections
        for row in file_data:
            columns = row.split(',')
            self.letters.append(columns)

            for letter in columns:
                self.nodes.append(letter)

        self.dimension = len(self.letters)

        # Load the dictionary
        with open(dictpath) as file:
            self.dict_words = file.read().splitlines()

        # load up the sequence frequency and use that to prune the adj matrix
        with open(seqpath, 'r') as fp:
            seq_frequency = json.load(fp)

        # Create the adjacency matrix which is N*N
        # index = row_i*dimension + col_i
        for row_i in range(self.dimension):
            for col_i in range(self.dimension):

                # Calculate the current node index
                node_index = row_i*self.dimension + col_i
                self.adj_matrix.append([False for _ in range(self.dimension**2)])

                # check all of the possible connection with the current node
                # by trying all possible 8 direction
                for step_row_i in range(-1,2):
                    next_row_i = row_i + step_row_i

                    if next_row_i < 0 or next_row_i >= self.dimension:
                        continue

                    for step_col_i in range(-1, 2):
                        next_col_i = col_i + step_col_i

                        if next_col_i < 0 or next_col_i >= self.dimension:
                            continue

                        # At this point the step is possible
                        step_index = next_row_i*self.dimension + next_col_i

                        # We don't allow same connection
                        if node_index == step_index:
                            continue

                        # Check if the duo of letter is possible and happen in the dictionary
                        letter_duo = self.nodes[node_index] + self.nodes[step_index]
                        if letter_duo not in seq_frequency:
                            print(f"{letter_duo} is not possible duo!")
                            continue
                        else:
                            print(letter_duo, seq_frequency[letter_duo])

                        self.adj_matrix[node_index][step_index] = True
        self.print_adj_matrix()
        
                        
    def find_all_words(self):
        """main function to find all the words in the grid that are in the dictionary"""
        # Seed of the permutations

        for node_index in range(len(self.nodes)):
            seed_letter = self.nodes[node_index]

            # copy the adj matrix and recurse
            seed_adj_matrix = copy.deepcopy(self.adj_matrix)
            self.dfs_graph(seed_letter, node_index, seed_adj_matrix)


    def dfs_graph(self, current_word, current_index, adj_matrix):
        """ standard depth first search algorithm that will add a word if valid
            self: the current Grid object
            current_word: the current_word formed to date in the traversal
            current_index: the index of the current nodeadj_matrix: adjacency matrix representing the connection in the graph

            return None
        """
        # Check if the new word created is a valid new one
        if current_word in self.dict_words and current_word not in self.output_words and len(current_word) >= 3:
            print(current_word)
            self.output_words.append(current_word)

        # Iterate on each of the connection for this position
        for next_index in range(0, len(self.nodes)):
            if adj_matrix[current_index][next_index] == True:

                # Create a new word  
                next_word = current_word + self.nodes[next_index]

                # Recurse in the search (make a copy and remove this node from the selectable ones)
                next_adj_matrix = copy.deepcopy(adj_matrix)
                for i in range(0, len(self.nodes)):
                    next_adj_matrix[current_index][i] = False
                    next_adj_matrix[i][current_index] = False
                self.dfs_graph(next_word, next_index, next_adj_matrix)


    def print_grid(self):
        """pretty print the boggle grid"""

        for row in self.letters:
            for letter in row:
                print(f"[{letter}] ", end="")
            print("")

    def print_adj_matrix(self):
        """pretty print the adjacency matrix"""
        for row in self.adj_matrix:
            for node in row:
                print(f"[{node}] ", end="")
            print("")


def boggle_solver(argv):

    # Input Checking
    if len(argv) != 2:
        raise AttributeError("Only one argument must be given to the boggle solver")

    # Check if file exist
    filepath = argv[1]

    if not os.path.isfile(filepath):
        raise FileNotFoundError("The file doesn't exist")
    
    # Populate the Grid
    # TODO REMOVE THIS HARD CODED DICTIONARY
    grid = Grid(filepath, 'src/en_dict.txt', 'src/en_seq_freq.json')
    grid.print_grid()
    
    # find all the words in the grid
    grid.find_all_words()

    # Print and return all words
    for word in grid.output_words:
        print(word)

    return grid.output_words


if __name__ == '__main__':

    # Timing of the boggle solver
    start = timer()
    boggle_solver(sys.argv)
    end = timer()

    print(f"Solving run time: {timedelta(seconds=end-start)}")
