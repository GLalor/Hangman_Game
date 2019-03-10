import random
import os
if os.name == 'nt':
    clear = lambda: os.system('cls')
else: 
    clear = lambda: os.system('clear')
clear()

words = ["case","list","wage","deer","sour"]
global lettersGuessed
lettersGuessed = ['']
global correctGues
correctGues = []


def main():
    gameLogic()

def gameLogic():
    guesedWrong = 0
    correctGuesses = 0
    word = workPicker()
    printHangman(guesedWrong, correctGues, word)
    while guesedWrong <= 6:
        letter = userInput(guesedWrong, word)
        if letter in word and letter != '':
            if word.count(letter) == 1:
                correctGues[word.index(letter)] = letter
                correctGuesses = correctGuesses + 1
            else:
                for i in range(0, len(word)):
                    if word[i] == letter:
                        correctGues[i] = letter
                        correctGuesses = correctGuesses + 1
            printHangman(guesedWrong, correctGues, word)
            if correctGuesses == len(word):
                printWinner(guesedWrong, correctGues, word)
                break
        else: 
            guesedWrong = guesedWrong + 1
            printHangman(guesedWrong, correctGues, word)
    printFinalWord(word)

def workPicker():
    word = words[random.randint(0,4)]
    for i in range(0,len(word)):
        correctGues.append("")
    return word


def userInput(guesedWrong, word):
    letter = ''
    print()
    while letter in lettersGuessed:
        print ("\033[A                             \033[A")
        letter = input("Guess a letter:")
        if letter in lettersGuessed:
            print("Letter already guessed!")
            letter = input("Guess a letter:")
        else:
            lettersGuessed.append(letter)
            return letter
    return ''


def printHangman(guesedWrong, correct, word):
    clear()
    print("Lets play hangman!!!")
    print("---------------------")
    printRules()
    for i in range(0,6):
        if i == 0:
            print("")
        elif i == 1:
            print("#######")
        else:
            if guesedWrong > 0:
                printWrongAnswers(guesedWrong)
                break
            else:
                print("#")
    if len(correct) > 0:
        printCorrectLetters(correctGues,word)
    else:
     printSpaces(word)
  
def printWinner(guesedWrong, correct, word):
    printHangman(guesedWrong, correct, word)
    print("Winner Winner")

def printSpaces(wordPicked):
    print()
    for i in range(0, len(wordPicked)):
        print("-", end="")
    print("\n")

def printCorrectLetters(correct,wordPicked):
    print()
    for i in range(0,len(correct)):
        if correct[i] == "":
            print(" ",end="")
        else:
            print(correct[i], end="")
    printSpaces(wordPicked)

def printFinalWord(wordPicked):
    print("The word was: ",wordPicked)



def printWrongAnswers(numGuesses):
    if numGuesses == 1:
        print("#   |")
        printTags(3)
    elif numGuesses == 2:
        print("#   |")
        print("#   0")
        printTags(2)
    elif numGuesses == 3:
        print("#   |")
        print("#   0")
        print("#   |")
        printTags(1)
    elif numGuesses == 4:
        print("#   |")
        print("#   0")
        print("#  /|")
        printTags(1)
    elif numGuesses == 5:
        print("#   |")
        print("#   0")
        print("#  /|\\")
        printTags(1)
    elif numGuesses == 6:
        print("#   |")
        print("#   0")
        print("#  /|\\")
        print("#  /")
    elif numGuesses == 7:
        printFullBody()


def printTags(numTags):
    if numTags > 0:
        for i in range(0, numTags):
            print("#")

def printFullBody():
    print("#   |")
    print("#   0")
    print("#  /|\\")
    print("#  /\\")
    print("\n  R.I.P")

def printRules():
    print("Rules:")
    print("----  7 Guesses  ----")

if __name__ == '__main__':
   main()