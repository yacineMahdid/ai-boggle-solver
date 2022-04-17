# Command line python script to do the whole input -> output thing
# Will be called as follow:
# python main.py <name-of-file-containing-boggle-board>

import sys
import os


def find_all_words(grid):
    words = [] # OUTPUT: list of valid words

    return words

def boggle_solver(argv):

    # Boggle Variable
    grid = [] # INPUT: 2d array where grid[row][col]

    # Input Checking
    if len(argv) != 2:
        raise AttributeError("Only one argument must be given to the boggle solver")

    # Check if file exist
    filepath = argv[1]

    if not os.path.isfile(filepath):
        raise FileNotFoundError("The file doesn't exist")
    
    # Load the file data
    with open(filepath) as file:
        file_data = file.read().splitlines()
    
    # Populate the Grid
    for row in file_data:
        columns = row.split(',')
        grid.append(columns)

    # find all the words in the grid
    words = find_all_words(grid)

    # Print and return all words
    for word in words:
        print(word)
    return words


if __name__ == '__main__':
    boggle_solver(sys.argv)
