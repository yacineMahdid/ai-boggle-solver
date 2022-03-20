# Command line python script to do the whole input -> output thing
# Will be called as follow:
# python main.py <name-of-file-containing-boggle-board>


import sys

def boggle_solver(argv):

    # Input Checking
    if len(argv) != 2:
        raise Exception("Only one argument must be given to the boggle solver")

    print(str(argv))
    print(len(argv))

if __name__ == '__main__':
    boggle_solver(sys.argv)
