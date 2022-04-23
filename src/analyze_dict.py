# script to analyze the dictionary and generate a bi letter sequence

import json

# Filepath
DICTIONARY_NAME = 'src/en_dict.txt'
SEQUENCE_NAME = "src/en_seq_freq.json"

if __name__ == '__main__':
    # Load the dictionary so that we can manipulate it

    # Load the boggle file data
    with open(DICTIONARY_NAME) as file:
        file_data = file.read().splitlines()
    
    # Need to run a windows on each sequence of two letters
    sequence_frequency = {}
    for word in file_data:
        # get two letters
        for i in range(len(word) - 1 ):
            bi_sequence = word[i] + word[i+1]
            if bi_sequence not in sequence_frequency:
                sequence_frequency[bi_sequence] = 1
            else:
                sequence_frequency[bi_sequence] = sequence_frequency[bi_sequence] + 1

    print(sequence_frequency)
    
    # Save this frequency list as a json file
    with open(SEQUENCE_NAME, 'w') as fp:
        json.dump(sequence_frequency, fp)