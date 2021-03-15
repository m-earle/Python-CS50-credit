from cs50 import get_string
#import math

def main():
    text = get_string("Text:") #ask user for string
    letters = count_letters(text) ##call function to count letters
    words = count_words(text) ##call function to count words
    sentences = count_sent(text) ##call function to count sentences
    L = (letters / words) * 100
    S = (sentences / words) * 100
    index = 0.0588 * L - 0.296 * S - 15.8 ##reading level formula
    rindex = round(index)
    #print(f" L = {L}")
    #print(f"S = {S}")
    #print(f"index = {index}")
    #print(f"rindex = {rindex}")
    if (rindex < 1):
        print("Before Grade 1")
    elif (rindex > 16):
        print("Grade 16+");
    else:
        print(f"Grade {rindex}") ##prints reading level

def count_letters(s):
    letters = 0
    for c in s:
        if c.isalpha() == True:
            letters = letters + 1
    #print(f" Letters = {letters}")
    return letters

def count_words(s):
    words = 1
    for c in s:
        if c.isspace() == True:
            words = words + 1
    #print(f" Words = {words}")
    return words

## assume . ! or ? indicates end of sentence
def count_sent(s):
    sentences = 0
    for c in s:
        if c == "." or c == "!" or c == "?":
            sentences = sentences + 1
    #print(f"Sentences = {sentences}")
    return sentences

main()