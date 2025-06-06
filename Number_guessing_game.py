import random

from art import logo

def num_selection():
    numbers = list(range(1, 100)) #creates a list of numbers from 1 to 100
    num = random.choice(numbers)
    return num

def easy_guessing(target_num):
    easy_attempts = 10

    while easy_attempts > 0 :
        guess = int(input( "Make a guess: "))

        if guess == target_num :
            print("You win")
            return True

        elif guess < target_num:
            print("wrong guess, number too low")
            easy_attempts -= 1
            print(f"You have {easy_attempts} attempts left")

        elif guess > target_num:
            print("wrong guess, number too high")
            easy_attempts -= 1
            print (f"You have {easy_attempts} attempts left")

        if easy_attempts == 0:
            print("you have no attempts left")
            return False


def hard_guessing(target_num):
    hard_attempts = 5

    while hard_attempts > 0:
        guess = int(input("Make a guess: "))

        if guess == target_num:
            print("You win")
            return True

        elif guess < target_num:
            print("wrong guess, number too low")
            hard_attempts -= 1
            print(f"You have {hard_attempts} attempts left")

        elif guess > target_num:
            print("wrong guess, number too high")
            hard_attempts -= 1
            print(f"You have {hard_attempts} attempts left")

        if hard_attempts == 0:
            print("you have no attempts left")
            return False

       # hard_guessing()


def play_game():
    print (logo)
    print("Welcome to the Number Guessing Game!\n"
          "Im thinking of a number between 1 and 100.\n")
    selection = input("Please choose the difficulty level. Type: 'easy' or 'hard': ")
    target_num = num_selection()  # makes sure the number is selected only once

    if selection == 'easy':
        #for easy_attempts in range (10):
        easy_guessing(target_num)

    elif selection == 'hard':
        #for attempts in range (5):
            #target_num = num_selection()
        hard_guessing(target_num)

play_game()
