import colorama, random
from colorama import Fore

colorama.init()

TOTAL_TURNS = 6

def get_word(num):
    fname = f"{num}_letters.txt"
    lines = open(fname).read().splitlines()
    return random.choice(lines)

def intro():
    rules = input("Welcome to Wordle! Would you like an explainer of the rules? Type Y or N.\n")
    while rules not in ["Y", "N"]:
        rules = input("I'm not sure what you mean. Would you like an explainer of the rules? Type Y or N.\n")
    if rules == "Y":
        print("\nWordle is a word-based guessing game where you have six tries to guess a randomly generated word. Each letter in your guess provides information about this target word.")
        print("Letters in " + Fore.GREEN + "green " + Fore.RESET + "can be in that exact spot within the target word.")
        print("Letters in " + Fore.YELLOW + "yellow " + Fore.RESET + "can be found somewhere within the target word, but not at the spot where it's located in your guess.\n")
    word_len = input("How long would you like your word to be?\nType 4 or 5.\n")
    while int(word_len) not in [4, 5]:
        word_len = input("Please choose a valid option. How long would you like your word to be?\nType 4 or 5.\n")    
    return get_word(word_len)
    
def set_guess(entry, length):
    while not(type(entry) == str and len(entry) == length):
        entry = input(f"Your guess must be a {length}-letter word.\n")
    if entry not in open(f"{len(entry)}_letters.txt").read():
        override = input("Your guess wasn't found in our list of valid words. Override? Y/N\n")
        if override != "Y":
            entry = set_guess(input("Please guess again.\n"), length)            
    return entry.lower()

def check_guess(guess, word): 
    accuracy = ""
    if guess == word:
        print(Fore.GREEN + f"{word}" + "\nYou won!\n")
        exit()    
    for x in range(len(word)):
        if guess[x] != word[x]:
            if guess[x] in word: 
                accuracy += (Fore.YELLOW + f"{guess[x]}" + Fore.RESET + " ")
            else: 
                accuracy += (f"{guess[x]} ")
        else:
            accuracy += (Fore.GREEN + f"{guess[x]}" + Fore.RESET + " ")
    print(accuracy + "\n")

def turn(turns, word): 
    guess = set_guess(input(f"Turns remaining: {turns}\n"), len(word)) #sets 
    check_guess(guess, word)  

def play(turns): 
    word = intro()
    while turns != 0:
        turn(turns, word)
        turns -= 1
    print(f"You lost. The word was {word}.") 
    
play(TOTAL_TURNS)