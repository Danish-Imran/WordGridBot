import math
from dictionary import word_list

point_values = {
    "A": 1,
    "B": 3,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 4,
    "G": 3,
    "H": 3,
    "I": 1,
    "J": 8,
    "K": 5,
    "L": 2,
    "M": 3,
    "N": 2,
    "O": 1,
    "P": 4,
    "Q": 10,
    "R": 1,
    "S": 1,
    "T": 1,
    "U": 2,
    "V": 5,
    "W": 4,
    "X": 8,
    "Y": 4,
    "Z": 10,
}

def calculate_point_value(input_word):
    scoring_word = input_word
    word_point_total = 0

    for letter in scoring_word:
        for i in range(1, scoring_word.count(letter) + 1):
            word_point_total += point_values[letter] * i
            scoring_word = scoring_word.replace(letter, "")
            
    return input_word

    
calculate_point_value("COOCOO")
