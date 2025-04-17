import random
import os
import re

def check_play_status():
    valid_res = ['yes', 'no', 'y', 'n']
    while True:
        try:
            res = input('Do you wish to play again (Yes or No?):')
            if res.lower() not in valid_res:
                raise ValueError("Yes/No or Y/N only pls")
            if res.lower() in ['yes','y']:
                return True
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print ('Thanks for playing!')
                exit()

        except ValueError as err:
            print(err)

def play_bbp():
    user_score = 0
    computer_score = 0
    play = True

    while play:
        os.system('cls' if os.name == 'nt' else clear)
        print('')
        print('Bato, Bato, Pick!')

        user_choice = input('Please choose your weapon : [B]ato, [P]apel, or [G]unting:')

        if not re.match("^[GgBbPp]$", user_choice):
            print("Invalid choice! Please choose: [B]ato, [P]apel, or [G]unting:")
            continue

        print(f'You chose: {user_choice.upper()}')

        choices = ['G', 'B', 'P']
        opp_choice = random.choice(choices)
        print(f'Computer chose: {opp_choice}')

        # determine the winner

        if opp_choice == user_choice.upper():
            print("It\'s a tie!")
        elif (opp_choice == 'B' and user_choice.upper() == 'G') or \
            (opp_choice == 'G' and user_choice.upper() == 'P') or \
            (opp_choice == 'B' and user_choice.upper() == 'P'):
                print(f'{opp_choice} beats {user_choice.upper()},  Computer wins!')
                computer_score += 1
        else:
                print(f'{user_choice.upper()} beats {opp_choice},  You win!')
                user_score += 1
        print(f'Score - You {user_score}, Computer: {computer_score}')
        play = check_play_status()


if __name__ == '__main__':
    play_bbp()
        


        