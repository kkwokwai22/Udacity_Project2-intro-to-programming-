import pdb

# A list of replacement words to be passed in to the play game function.
pass_in_words = ["good", "python", "programming", "java", "Python", "script", "bytecode", "virtual", "programs",
                 "interpreter", "library","faster"]

parts_of_speech = ["___1___","___2___","___3___","___4___"]

level_easy_answer = {'___1___': 'good','___2___':'python', '___3___':'programming', '___4___':'java'}
level_medium_answer = {'___1___': 'Python','___2___':'script', '___3___':'bytecode', '___4___':'virtual'}
level_hard_answer = {'___1___': 'programs','___2___':'interpreter', '___3___':'library', '___4___':'faster'}


# The following are easy level test strings to pass in to the play_game function.
easy = "There are many ___1___ reasons to choose Python as your primary programming language." \
       "First of all ___2___ is an easy to learn, powerful programming language. " \
        "Object-oriented ___3___ is a lot easier than something. In languages like ___4___."

# The answers for easy level question
# 1 = good
# 2 = python
# 3 = programming
# 4 = java

# The following are medium level test strings to pass in to the play_game function.
medium ="___1___ is very fast. The source code is compiled into bytecode, so that executing the same file will be faster," \
        "if the ___2___ will be executed again. " \
        "The ___3___ is an '''intermediate language'''" \
        "which is said to run on a ___4___ machine that executes the machine code corresponding to each bytecode."

# The answer for medium level question
# 1 = Python
# 2 = script
# 3 = bytecode
# 4 = virtual

# The following are hard level test question strings to pass in to the play_game function.
hard = "It's surprisingly easy to embed Python, or better the Python interpreter into C ___1___. " \
       "By doing this you can add features from Python that could take months to code in C. Vice versa, " \
        "it's possible to extend the Python ___2___ by adding a module written in C. " \
        "One reason to do this is if a C ___3___ exists that does something which Python doesn't." \
       "Another good reason is if you need something to run ___4___ than you can manage in Python."

# The answer for hard level question
# 1 = programs
# 2 = interpreter
# 3 = library
# 4 = faster

greeting = raw_input("Welcome to Kevin's mab libs!! what is your name")
user_level_input = raw_input("Hi " + greeting + " please select the difficulty of the game! easy? medium? or hard?")


def set_game_level(user_level_input):
    """
    set_game_level(user_level_input) returns medium strings & dictionary of game level
    input: easy, medium or hard.
    output: user_level_inputs strings.
    """
    if user_level_input == "easy":
        print easy
        return easy, level_easy_answer
    elif user_level_input == "medium":
        print medium
        return medium, level_medium_answer
    elif user_level_input == "hard":
        print hard
        return hard, level_hard_answer
    else:
        return "none"

# Checks if a word in parts_of_speech is a substring of the word passed in.
def word_in_pos(word, parts_of_speech):
    for i in parts_of_speech:
        if i in word:
            return i
    return None

def word_replace(word, replacement, user_input):
    """
    :param word: sentence being operated/modified
    :param replacement: string with correct answer
    :param user_input: the pass in words
    :return: whole new string with correct answer and no commas and period.
    """
    word = word.replace(',', '')
    word = word.replace('.', '')
    word = word.replace(';', '')
    word = word.replace('\'', '')
    word = word.replace('\"', '')
    word = word.replace('\'\'\'', '')
    word = word.replace(replacement, user_input)
    return word

# this is the main function for the game.
def play_game(ml_string, parts_of_speech, proper_answer):
    """
    :param ml_string: easy/medium/hard level strings
    :param parts_of_speech: ___number___
    :param proper_answer: the correct answer in string (pass in word)
    :return: end of the game (if every word is correct) or you will be loop in the try again.
    """
    replaced = []
    new_ml_string = ml_string.split()
    index = 1
    for word in new_ml_string:
        replacement = word_in_pos(word, parts_of_speech)
        if replacement != None:
            user_input = raw_input("what should go into blank number " + str(index) + " :")
            while user_input != proper_answer['___'+str(index)+'___']:
                print "try again!"
                user_input = raw_input("what should go into blank number " + str(index) + " :")
            word = word_replace(word, replacement, user_input)
            print " ".join(replaced) + ' ' + word + ml_string.split('___'+str(index)+'___')[1]
            index += 1
        replaced.append(word)
    replaced = " ".join(replaced)
    return "Thank you for playing " + greeting + " !"

game_sentence , proper_answer = set_game_level(user_level_input)

print play_game(game_sentence , parts_of_speech, proper_answer)




