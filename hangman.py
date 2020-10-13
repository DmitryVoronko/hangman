# Write your code here
import random


def run_game():
    words = ['python', 'java', 'kotlin', 'javascript']
    computer_word = random.choice(words)
    computer_letters = set(computer_word)
    user_letters = set()
    correct_user_letters = set()
    lives = 8
    while True:
        hint = ""

        for letter in computer_word:
            if letter in correct_user_letters:
                hint += letter
            else:
                hint += '-'
        print("")
        print(hint)
        user_letter = input("Input a letter: ")

        if len(user_letter) != 1:
            print("You should input a single letter")
            continue

        if user_letter in user_letters:
            print("You've already guessed this letter")
            continue

        user_letters.add(user_letter)

        if not user_letter.isascii() or not user_letter.islower():
            print("Please enter a lowercase English letter")
            continue

        if user_letter in computer_word:
            correct_user_letters.add(user_letter)
            if len(correct_user_letters) is len(computer_letters):
                print(f"You guessed the word ${computer_word}!")
                print("You survived!")
                break
        else:
            print("That letter doesn't appear in the word")
            lives -= 1

        if lives == 0:
            print("You lost!")
            break


print("H A N G M A N")


def show_menu():
    while True:
        user_input = input('Type "play" to play the game, "exit" to quit: ')
        if user_input == "play":
            run_game()
            show_menu()
        elif user_input == "exit":
            break
        else:
            continue


show_menu()
