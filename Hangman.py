import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    word=''
    for letter in secret_word:
        if letter in letters_guessed:
            word=word + letter
        else:
            word=word+"_"
    print(f'the secret word guessed so far is:')
    return word

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    word=''
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if letter not in letters_guessed:
            word=word + letter
    return (f"avaialabe letters are: {word} \n")

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    if len(my_word)==len(other_word):
        for number,item in enumerate(my_word):
            if item==other_word[number] or item=="_":
                pass
            else:
                return False
    else:
        return False
    return True

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_) cannot be one of the letters in the word
             that has already been revealed.

    '''
    newlist=[]
    for words in wordlist:
        if match_with_gaps(my_word,words):
            newlist.append(words)
    print(newlist)

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    '''

    letter=''
    count=0
    guesses=6
    letters_guessed=[]
    long=0
    warnings=3
    long=len(secret_word)
    print(f"\n I am thinking of a word that is {long} letters long. \n")
    while(count==0 and warnings>-1 and guesses>0):
        if guesses<6:
                    print(get_available_letters(letters_guessed))
                    print(f"you have {guesses} guesses left")
        if guesses==6:
            print(f"you have {guesses} guesses")
        print("please input a letter in lowercase or * for a hint: ")
        letter=input(letter)
        if letter not in "qwertyuiopasdfghjklzxcvbnm*":
            warnings-=1
            print('wrong input')
            if warnings>0:
                print(f"you have {warnings} warnings left \n")
            continue
        elif letter in letters_guessed:
            warnings=warnings-1
            print('wrong input')
            print(f"you have {warnings} warnings left")
            continue
        if letter=="*":
            result=get_guessed_word(secret_word,letters_guessed)
            print("possible combinations are:")
            show_possible_matches(result)
            continue
        letters_guessed.append(letter)
        print(get_guessed_word(secret_word,letters_guessed))
        if letter not in secret_word:
                    guesses=guesses-1
                    print("WRONG! the letter is not in word \n")
        else:
            print("RIGHT!! the letter was in the word \n")
        if is_word_guessed(secret_word,letters_guessed):
            count=1
            print('YOU WON!!! ')
    if guesses==0:
        print('you failed')
        print(f"the word was {secret_word}")
    if warnings==-1:
        print('bad boy')



secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)
