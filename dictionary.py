from nltk.corpus import words

def initialize_dictionary():
    global word_list
    english_words = words.words()
    english_words.extend(("pazazz", "razzamatazz", "coocoo", "booboo", "zyzzyva", "muumuu", "deeded")) # add beneficial words that aren't included in dictionary

    # I do not have the dictionary that the game uses, and getting a word list before runtime is difficult for me to implement
    words_to_remove = ["KAKKAK", "HAIATHALAH", "MURUMURU", "CONSENTANEOUSNESS", "DIPLOCOCCIC", "WALLAWALLA", "PUPPIFY", "KUKURUKU", "CURUCUCU", "PREAPPEARANCE", 
    "MUDDYHEADED", "TANGANTANGAN", "UNSHAVENNESS", "GANGGANG", "HIPPOPHAGI", "UNSENSUOUSNESS", "GYPSYFY", "QUINQUENNIAD", "SMACKSMAN", "WINDOWWARDS", "PURUPURU",
    "GIFFGAFF"] # remove words that are often chosen by the bot 

    word_list = [word.upper() for word in english_words if len(word) > 3 and word.upper() not in words_to_remove]

    return word_list
