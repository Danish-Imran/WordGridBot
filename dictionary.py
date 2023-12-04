from nltk.corpus import words

def initialize_dictionary():
    global word_list
    english_words = words.words()
    english_words.extend(("pazazz", "razzamatazz", "coocoo", "booboo", "zyzzyva", "muumuu", "deeded")) # add beneficial words that aren't included in dictionary

    word_list = [word.upper() for word in english_words if len(word) > 3]
    return word_list
