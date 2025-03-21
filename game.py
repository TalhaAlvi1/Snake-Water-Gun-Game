import random

def get_computer_choice():
    return random.choice(['snake', 'water', 'gun'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'snake' and computer == 'water') or \
         (user == 'water' and computer == 'gun') or \
         (user == 'gun' and computer == 'snake'):
        return "You win!"
    else:
        return "Computer wins!"
