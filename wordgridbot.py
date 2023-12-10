from dictionary import initialize_dictionary
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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


# set up game

word_list = initialize_dictionary() # creates dictionary

driver = webdriver.Chrome()
driver.get('https://metzger.media/games/word-grid/')


try:
    word_count = 0
    play_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, 'play-button')))
    play_button.click()

    actions = ActionChains(driver)


    while word_count < 500: # enters 500 words before stopping, otherwise program goes forever
        word_count += 1
        valid_word = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="bg"]/div[4]/div/div/h2[3]'))) # checks if word can be submitted
        letter_board = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'letter'))) # finds elements with letters

        nine_letters = ""
        possible_words = []
        next_best_word_index = 0

        for i in letter_board[:9]: # collect the letters
            nine_letters += i.text
        
        for word in word_list: # determine possible words
            if is_word_formable(word, nine_letters):
                possible_words.append(word)

        possible_words = sorted(possible_words, key=calculate_point_value, reverse=True) # sorts highest to lowest point values

        actions.send_keys(possible_words[next_best_word_index])
        actions.perform() # type first word
        validity_of_word = valid_word.get_attribute("class") # check if guess is valid or not

        while validity_of_word == "score-text guess": # if word is not valid
            next_best_word_index += 1
            actions.reset_actions()
            
            for i in range(len(possible_words[next_best_word_index - 1])):
                actions.send_keys(Keys.BACK_SPACE)
            actions.perform() # clear what was inputted
            actions.reset_actions()

            actions.send_keys(possible_words[next_best_word_index]) # test the next best word
            actions.perform()
            validity_of_word = valid_word.get_attribute("class")


        actions.reset_actions() # enter word and reset actions
        actions.send_keys(Keys.RETURN)
        actions.perform()
        actions.reset_actions()
    
    time.sleep(5000) # after program ends, keeps tab open for 5000 seconds

except:
    driver.quit()
