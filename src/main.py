# Command line python script to do the whole input -> output thing
# Will be called as follow:
# python main.py <name-of-file-containing-boggle-board>

import sys
import os
import copy

class Grid:
    letters = []
    adj_matrix = []
    dimension = 0

    dict_words = []
    output_words = []

    def __init__(self, filepath, dictpath):

        # Load the file data
        with open(filepath) as file:
            file_data = file.read().splitlines()
    
        # iterate on each row and store the letters + set the connections
        for row in file_data:
            columns = row.split(',')
            self.letters.append(columns)
            self.adj_matrix.append([True for _ in columns])

        self.dimension = len(self.letters)

        # Load the dictionary
        with open(dictpath) as file:
            self.dict_words = file.read().splitlines()

    def create_all_permutations(self):

        # Seed of the permutations
        for row_i in range(self.dimension):
            for col_i in range(self.dimension):
                print(f"Starting DFS at seed r:{row_i}, c:{col_i}")
                print(self.adj_matrix)
                seed_letter = self.letters[row_i][col_i]
                seed_adj_matrix = copy.deepcopy(self.adj_matrix)

                self.dfs(seed_letter, row_i, col_i, seed_adj_matrix)



    def dfs(self, current_word, row_i, col_i, adj_matrix):

        # Check if the new word created is a valid new one
        if current_word in self.dict_words and current_word not in self.output_words and len(current_word) >= 3:
            print(current_word)
            self.output_words.append(current_word)

        adj_matrix[row_i][col_i] = False 

        # can technically go into 8 directions including diagonals
        for step_row_i in range(-1,2):
            next_row_i = row_i + step_row_i

            if next_row_i < 0 or next_row_i >= self.dimension:
                continue

            for step_col_i in range(-1, 2):
                next_col_i = col_i + step_col_i

                if next_col_i < 0 or next_col_i >= self.dimension:
                    continue

                # Check for connection, if there is none we skip it
                if adj_matrix[next_row_i][next_col_i] is False:
                    continue
        
                # Create a new word and 
                next_word = current_word + self.letters[next_row_i][next_col_i]

                # Recurse in the search
                next_adj_matrix = copy.deepcopy(adj_matrix)
                self.dfs(next_word, next_row_i, next_col_i, next_adj_matrix)

    def print_grid(self):
        for row in self.letters:
            for letter in row:
                print(f"[{letter}] ", end="")
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
    grid = Grid(filepath, 'src/en_dict.txt')
    grid.print_grid()
    
    # find all the words in the grid
    
    
    grid.create_all_permutations()
    # Print and return all words
    for word in grid.output_words:
        print(word)
        
    return grid.output_words


if __name__ == '__main__':
    boggle_solver(sys.argv)
