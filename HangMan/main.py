import random
import os
from english import words
import subprocess

os.system('cls')
hangman_word = words()

hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" o ",
        "   ",
        "   "),
    2: (" o ",
        " | ",
        "   "),
    3: (" o ",
        "/| ",
        "   "),
    4: (" o ",
        "/|\\",
        "   "),
    5: (" o ",
        "/|\\",
        "/  "),
    6: (" o ",
        "/|\\",
        "/ \\")
}

def main():
    ran_word = random.choice(hangman_word)
    tries = 0
    guessed = []
    progress = '_'*len(ran_word)

    while True:
        print('******* HangMan Game *******')
        print(f"The letter have {len(ran_word)} letters!!")
        print(f"Your progression: {progress}")
        print('****************************')

        user_input = input('Enter your letter: ')

        os.system('cls')
        subprocess.call("cls", shell=True)

        while len(user_input)!=1 or not user_input.isalpha():
            print('******* HangMan Game *******')
            user_input = input('Enter valid letter: ')
            os.system('cls')
        print('****************************')
        subprocess.call("cls", shell=True)

        if user_input in guessed:
            print('You have already entered this letter!\n\n')
            continue

        guessed.append(user_input)


        if user_input in ran_word:
            progress = ''.join([user_input if ran_word[i] == user_input else progress[i] for i in range(len(ran_word))])
            print('Correct guess...')
            print('Your progress: ', progress)

        else:
            tries+=1
        
        for art in hangman_art[tries]:
            print(art)
        print()

        if tries == 6:
            print('******* HangMan Game *******')
            print('GameOver! You Lost...')
            print('----------------------------')
            print(f"The word was: {ran_word}")
            print('****************************')
            break

        if '_' not in progress:
            print('******* HangMan Game *******')
            print('You won!')
            print('----------------------------')
            print(f"You guessed word: {ran_word} \nMistakes: {tries}")
            print('****************************')
            break

    play_again = input('Do you want to play again? (y/n): ').lower()
        
    while play_again not in ['y', 'n'] or not play_again.isalpha():
        play_again = input('Enter valid choice! (y/n): ').lower()
        
    if play_again == 'y':
        subprocess.call("cls", shell=True)
        main()

    else:
        os.system('cls')
        subprocess.call("cls", shell=True)
        print('ThankYou for playing!')
        

if __name__ == '__main__':
    main()
