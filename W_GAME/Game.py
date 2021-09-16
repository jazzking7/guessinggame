import math
from random import *
from PA import *
from PB import *
from PC import *
from PD import *
from PE import *

def get_random_puzzle(puzzles):

    x = randint(0, len(puzzles)-1)
    return puzzles[x]

def count_occurrences_of_letter(puzzle, letter):


    count = 0
    for i in range(len(puzzle)):
        if puzzle[i] == letter:
            count += 1
    return count

def check_puzzle_compatibility(puzzle, blanks, puzzle2):

    if (len(puzzle) != len(puzzle2)):
        return False
    for index, element in enumerate(blanks):
        if element:
            if (puzzle[index] != puzzle2[index]):
                return False 
    return True

def get_best_compatible_puzzle(puzzle, blanks, letter, puzzles):

    compatibles = []
    occurrences = []

    for puz in puzzles:
        if check_puzzle_compatibility(puzzle, blanks, puz):
            compatibles.append(puz)
            occurrences.append(count_occurrences_of_letter(puz, letter))
    if len(compatibles) == 0:
        return None
    
    minimum = min(occurrences)

    for element in compatibles:
        if (count_occurrences_of_letter(element, letter) == minimum):
            return element
    return None

def get_starting_blanks(puzzle):

    blanks = []
    for i in range(len(puzzle)):
        if puzzle[i] == " ":
            blanks.append(True)
        else:
            blanks.append(False)
            
    return blanks

def blanks_to_string(blanks, puzzle):

    string = ""
    for index, boolean in enumerate(blanks):
        if boolean:
            string += puzzle[index]
        else:
            string += "_"
            
    return string
    
def update_blanks(blanks, puzzle, letter):

    for i in range(len(puzzle)):
        if puzzle[i] == letter:
            blanks[i] = True

def check_if_game_won(blanks):

    for i in blanks:
        if (i == False):
            return False
        
    return True

def guessed_full_phrase(puzzle, phrase, blanks):

    if len(phrase) != len(puzzle):
        return False
    
    for index, letter in enumerate(puzzle):
        if puzzle[index] != phrase[index]:
            return False
        
    for i in range(len(blanks)):
        blanks[i] = True
        
    return True

def ending_countdown():
    x = 20
    while (x > 0):
        time.sleep(1)
        if x == 3:
            print(99599584995)
            x -= 1
            continue
        if x == 13:
            print(x)
            print("#$@!&^%*&^$^^%&^$@&!&\\^%*&^$^^#$")
            x -= 1
            continue
        if x == 11:
            print(x)
            print("#$!&...pl..e.a..s.e....h.l.p..m.e...")
            x -= 1
            continue
        if x == 8:
            print(x)
            print("#...c.a...l...t.h..s...n..mb...r....")
            x -= 1
            continue
        if x == 6:
            print(x)
            print("9$@9!5&9\\58%4#9&5$")
            x -= 1
            continue
        if x == 5:
            print(x)
            print("9$9!5&9958%4#9&5$")
            x -= 1
            continue
        print(x)
        x -= 1
    time.sleep(3)

def spin(wheel):

    x = randint(0, len(wheel)-1)
    return wheel[x]

def update_score(misfortune, puzzle, wheel, miswheel):
    score = 0
    if misfortune:
        score = len(puzzle)*spin(miswheel)
    else:
        score = len(puzzle)*spin(wheel)
    return score

def face(misfortune):
    faces = ["(^o^): ", "(^_^): ", "(^0^): ", "\\(^0^)/: "]
    badfaces = ["(=_=): ", "(=_o): ", "(o_o): ", "(X_O): ", "(*_*): ", "(#_X): ", "(#_@): "]
    if misfortune:
        x = randint(0, len(badfaces)-1)
        return badfaces[x]
    y = randint(0, len(faces)-1)
    return faces[y]
        
def play(misfortune, multiplayer):
    '''
    Parameter: a boolean indicating whether or not the special variant should be played.
    This function will let the player play the game.
    '''
    puzzles = [
        
        "TO BE OR NOT TO BE",
        "DEATH IS NOT THE END",
        "NO GAME NO LIFE",
        "YOU FORGOT GOODBYE",
        "WHY SO SERIOUS",
    ]
    
    mispuzzles = [
        "SIO ULY HINBCHA VON GS CGUACHUNCIHM",
        "TO XE OR NOT TO XE",
        "XO BE OR NOX XO BE",
        "TX BE XR NXT TX BE",
        "XEATH IS NOT THE ENX",
        "DEAXH IS NOX XHE END",
        "DEATX IS NOT TXE END",
        "XO GAME XO LIFE",
        "NX GAME NX LIFE",
        "NO XAME NO LXFE",
        "YOU XORGOT GOODBYE",
        "YOU FORXOT XOODBYE",
        "YOU FORGOT GOODXYE",
        "WXY SO SERIOUS",
        "WHY XO XERIOUX",
        "WHY SO SEXIOUS"
    ]
    # wheels of score
    wheel = [1,2,3,4,5,6,7,8,9,10,15,20,25,30,35,40,45,50,55,60,65,70,100]
    miswheel = [1,2,3,4,5,6,7,-8,-9,-10,-15,-20,-25,-30,-35,-40,-45,-50,-55,-60,-65,-70,-100]
    score1 = 0
    score2 = 0
    # records guesses
    num_correct_guesses, num_incorrect_guesses = 0, 0
    # starting quiz
    puzzle = get_random_puzzle(puzzles)
    puzzles.remove(puzzle)
    # starting blanks
    blanks = get_starting_blanks(puzzle)
    # guessing letters
    guessed_letters = []
    # starting display
    print("\nHere is your phrase:")
    print(blanks_to_string(blanks, puzzle))
    # multiplayer mode display
    if multiplayer:
        print("\nYour turn!")
        you = False
        player2 = True
    # game status
    winner = False
    
    # start to guess
    while not winner:
        letter = ''
        # keep asking for input
        while not letter.isalpha():
            letter = input("Guess a letter (a - z or A - Z) "+ face(misfortune))
            letter = letter.upper()
            if len(letter) > 1:
                break
        # special answers
        if len(letter) > 1:
            if letter == "911":
                badcall()
                winner = check_if_game_won(blanks)
            elif letter == "99599584995":
                first_phone_call()
                winner = check_if_game_won(blanks)
            else:
                if guessed_full_phrase(puzzle, letter, blanks):
                    num_correct_guesses += 1
                    if multiplayer and not player2:
                        score2 = 1000000
                    else:
                        score1 = 1000000
                else:
                    num_incorrect_guesses += 1
            print("\n"+blanks_to_string(blanks, puzzle))
            winner = check_if_game_won(blanks)
            continue
        # record guessed letters
        if letter not in guessed_letters:
            guessed_letters.append(letter)
        guessed_letters = sorted(guessed_letters)
        # using occurrences to determine if a letter is correct
        letter_present = count_occurrences_of_letter(puzzle, letter) > 0
        # verify if misfortune is on
        if letter_present and misfortune:
            update_blanks(blanks, puzzle, letter)
            new_puzzle = get_best_compatible_puzzle(puzzle, blanks, letter, mispuzzles)
            # change puzzle
            if new_puzzle not in [None, puzzle]:
                mispuzzles.remove(new_puzzle)
                puzzle = new_puzzle
                letter_present = count_occurrences_of_letter(puzzle, letter) > 0
                print("\nMUAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA")
        
        if letter_present:
            update_blanks(blanks, puzzle, letter)
            num_correct_guesses += 1
        else:
            num_incorrect_guesses += 1
        # update score:
        if multiplayer:
            if not you:
                if letter_present:
                    score1 += update_score(misfortune, puzzle, wheel, miswheel)
                else:
                    score1 -= update_score(misfortune, puzzle, wheel, miswheel)
            elif not player2:
                if letter_present:
                    score2 += update_score(misfortune, puzzle, wheel, miswheel)
                else:
                    score2 -= update_score(misfortune, puzzle, wheel, miswheel)
        else:
            
            if letter_present:
                score1 += update_score(misfortune, puzzle, wheel, miswheel)
            else:
                score1 -= update_score(misfortune, puzzle, wheel, miswheel)
        # print the current phrase        
        print("\n"+blanks_to_string(blanks, puzzle))
        # check if the game won (break loop)
        winner = check_if_game_won(blanks)
        if not winner:
            # display scores
            if multiplayer:
                print("Your balance: {}$   Player2's balance: {}$".format(score1, score2))
            else:
                print("Your balance: {}$".format(score1))
            # display guessed letters
            print("Guessed letters: " + ','.join(guessed_letters))
            # multiplayer display turn
            if multiplayer:
                if you:
                    print("Your turn!")
                    you = False
                    player2 = True
                elif player2:
                    print("Player2's turn!")
                    player2 = False
                    you = True
                    
    # game is finished
    print("\nYOU FOUND THE SENTENCE! CONGRATS! \\(^o^)/")
    print("\nIn total there are {} correct and {} incorrect guesses! (o_0)".format(num_correct_guesses, num_incorrect_guesses))
    if multiplayer:
        print("\nYour total balance: {}$   Player2's total balance: {}$\n".format(score1, score2))
    else:
        print("\nYour total balance: {}$\n".format(score1))
    win = (score1 > score2)
    passed = ((score1 > 0) and (score2 > 0))
    million = ((score1 == 1000000) or (score2 == 1000000))
    escape = end_sequence(multiplayer, million, win, misfortune, passed)
    if (escape == 100):
        return escape
        
def menu():
    stop = False
    while not stop:
        p("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        p("Welcome to Wheel of (Mis)Fortune! Dear visitor! \\(^o^)/ \\(x_x)/ \\(^_+)/\n\
Guess the phrase, one letter at a time...QUITE SIMPLE RIGHT??\\(>o<)/\n\
This is a game where YOUR LIFE is at STAKE!(YAY! SO FUN!! SO EXCITING!!)")
        p("\\(^o^)/\\(+_=)/\\(0_o)/\\(^_+)/\\(=_=)/\\(+_o)/\\(^o^)/\\(+_=)/\\(0_o)/\\(O_O)/")
        p("HUH? You have a cellphone? Well...call 911 during game for hints!\\(^0^)")
        p("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
        p("...Now, DEAR visitor, what would YOU like to DO? \\(^0^)/?")
        p("1 --> Play a game of Wheel of Fortune ($_$)\n\
2 --> Play a game of Wheel of MISFORTUNE \\(^0^)/ \\(X_X)\n\
3 --> Exit......(=_=)")
        proper_answer = False
        while not proper_answer:
            answer = input(">>> ")
            if answer == "1":
                valid1 = False
                while not valid1:
                    x = input("Multiplayer mode? (+_O)\n1 --> play alone\n2 --> add Player2\n>>> ")
                    x = x.upper()
                    if x == "2":
                        valid1 = True
                        proper_answer = True
                        play(False, True)
                    elif x == "1":
                        valid1 = True
                        proper_answer = True
                        play(False, False)
                    else:
                        print("Invalid input! (+_x)")
            
            elif answer == "2":
                valid2 = False
                while not valid2:
                    y = input("Multiplayer mode? (+_O)\n1 --> play alone\n2 --> add Player2\n>>> ")
                    y = y.upper()
                    if y == "2":
                        valid2 = True
                        proper_answer = True
                        escaped = play(True, True)
                        if (escaped == 100):
                            return 100
                        
                    elif y == "1":
                        valid2 = True
                        proper_answer = True
                        play(True, False)
                    else:
                        print("Invalid input!(+_x)")

            elif answer == "3":
                valid3 = False
                while not valid3:
                    ans = input("Are you sure you want to quit? (o_o) yes/no: ")
                    ans = ans.upper()
                    if ans == "YES":
                        bye = False
                        valid3 = True
                        proper_answer = True
                        while not bye:
                            c1 = input("do you REALLY want to quit???(x_O) yes/no: ")
                            c1 = c1.upper()
                            if c1 == "YES":
                                lag(1)
                                p("\nDIE!(X_O)")
                                lag(1)
                                execution(1)
                                bye = True
                            elif c1 == "NO":
                                lag(1)
                                p("\nTOO LATE! DIE!(X_O)")
                                lag(1)
                                execution(1)
                                bye = True
                            elif c1 == "GOODBYE":
                                ending_countdown()
                                lag(1)
                                bye = True
                                stop = True
                                return 50
                            else:
                                print("AnSwEr PrOpErLy!!(x_O)")
                        
                    elif ans == "NO":
                        valid3 = True
                        p("GOOD! Now choose your game! (^o^)")
                    else:
                        print("AnSwEr PrOpErLy! (+_x)")
            else:
                print("Invalid input! (+_x)")
                proper_answer = False
    
if __name__ == '__main__':
    try:
        x = open("New Message.txt", 'r')
        x.close()
        Grand_final()
        
    except:
        intro()
        safe = (menu() == 100)
        if safe:
            safezone()
