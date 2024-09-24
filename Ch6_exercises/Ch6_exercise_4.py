# Exercise 4
print('\nExercise 4\n')

# Given a sequence as input find distances between the copies of
# the most frequent substring
"""
seq = input("Enter a dna string: ")
k = 3                                               # length of the substring, should also be possible be inputted by the user (default = 3)
substrings = {}
for i in range(len(seq) - k + 1):                   # create dict with all possible substrings. counts how many times they are seen in the original dna string
    substring = seq[i: i+k]
    if substring in substrings:
        substrings[substring] += 1
    else:
        substrings[substring] = 1

max_count = 0
most_freq_substring = ""
for substring, count in substrings.items():         # identify the string with more counts present in the dict obtained previously
    if count > max_count:                           # This function can be changed to >>> most_freq_substring = max(substrings, key=substrings.get) 
        most_freq_substring = substring
        max_count = count

positions = []
for i in range(len(seq) - k + 1):                   # 1. Go through the dna string, 2. identify the most common substring, 3. save their positions (first nucleotide only)
    substring = seq[i: i+k]
    if substring == most_freq_substring:
        positions.append(i)

distances = []
for p1,p2 in zip(positions[:-1], positions[1:]):    # Calculate the distance between the most common substrings
    distances.append(p2 - p1)

print(distances)
"""

# Rewrite the program to be more readable.

# Which parts can be made into sensible functions? 
    # 1. Function possible substrings
    # 2. Function to identify position of the most common substring (max function should be here)
    # 3. Function to calculate distances
    # 4. Interaction with user (input parameters: dna string and length of substring (default = 3))
# Make sure they both take appropriate parameters and return appropriate data structures. 
    # Use exception if the user puts anything that's not a sequence of ATGC. And substring length should always be a number
# It should be possible to call any of the functions individually from another module.

# Testing:
# seq = AGCTAGCGGTAGC, k = 3


def create_substring(seq: str, k: int) -> dict:
    """Create dict with all possible substrings. Then counts how many times they are seen in the original dna string"""
    substrings = {}
    for i in range(len(seq) - k + 1):
        kmer = seq[i: i+k]
        if kmer in substrings:
            substrings[kmer] += 1
        else:
            substrings[kmer] = 1
    return substrings

def kmer_position(substrings: dict, seq: str, k: int) -> tuple:
    """Go through the dna string; identify the most common substring; save their positions (first nucleotide only)"""
    positions = []
    most_freq_substring = max(substrings, key=substrings.get)
    for i in range(len(seq) - k + 1):
        substring = seq[i: i+k]
        if substring == most_freq_substring:
            positions.append(i)
    return tuple(positions)                             # passed to tuple because next function needs tuple as a parameter

def kmer_distance(positions: tuple) -> tuple:
    """Calculate the distance between the most common substrings"""
    distances = []
    for p1,p2 in zip(positions[:-1], positions[1:]):
        distances.append(p2 - p1)
    return tuple(distances)                             # make list immutable by transforming into tuple

#==================Functions that will not appear when defining main================================

def valid_dna_sequence(seq: str) -> bool:
    """Check if a string only has ATCG, meaning that it is a valid DNA string"""
    return set(seq.upper()).issubset({'A', 'T', 'C', 'G'})      # no need to put the small letters because with seq.upper they will alway be upper

def seq_input() -> str:
    """Check if input string is valid"""
    while True:
        seq = input("Enter a dna string:\n")
        if valid_dna_sequence(seq):
            return seq
        print("Error: Invalid DNA string. Please try another one.")

# check if k is a valid number (if can be transformed to int and is smaller than the length of string)

def k_input(seq: str) -> int:
    """Check if input k is valid"""
    while True:
        k = input("Enter a kmer length or press enter (k = 3):\n")
        if k == '':
            return 3
        try:
            k = int(k)
            if k > len(seq):
                print("Error: Invalid input. k is higher than length of the DNA string. Please enter a valid number.")
            else:
                return k
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")


#==================================================================================

def kmer_input() -> tuple:
    """input function that takes seq and k from the user and evaluates if they are valid"""
    seq = seq_input()
    k =  k_input(seq)
    return seq, k

def main():
    """main function for module"""
    seq, k = kmer_input()
    substrings = create_substring(seq, k)
    positions = kmer_position(substrings, seq, k)
    distances = kmer_distance(positions)
    print(distances)

if __name__ == "__main__":
    main()

