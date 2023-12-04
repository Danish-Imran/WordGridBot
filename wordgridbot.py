from dictionary import initialize_dictionary

point_values = { # original values for each letter
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
    # calculates the points gained from entering a word
    scoring_word = input_word # creates duplicate
    word_point_total = 0 # initializes score tracker and resets it

    for letter in scoring_word: 
        for i in range(1, scoring_word.count(letter) + 1): # iterates through amount of repeated letters
            word_point_total += point_values[letter] * i # adds the score for that letter
            scoring_word = scoring_word.replace(letter, "") # removes letter from string so it is not counted twice


    return word_point_total

def is_word_formable(word, letters):
    # sees if a word is formable with the given letters
    word_set = set(word)
    letters_set = set(letters)

    return word_set.issubset(letters_set) # returns boolean


word_list = initialize_dictionary() # creates dictionary


# begin game loop

nine_letters = "PAZRMTEUK"
possible_words = []

for word in word_list:
    if is_word_formable(word, nine_letters):
        possible_words.append(word)

possible_words = sorted(possible_words, key=calculate_point_value) # sorts lowest to highest point value
