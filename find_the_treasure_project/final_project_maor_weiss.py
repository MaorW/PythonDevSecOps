from random import randint
from pathlib import Path

"""
### The "find the treasure" game ###

Instructions for the codder:
Step1:
1. Create new file or overwrite an existing file
2. The program will create a sequence of [1-20] random numbers between 0 to 9 by an ascending order
3. After the last digit (The digit 9), Print the word 'TREASURE'
4. Then, The program will create sequence of [1-20] random numbers between 0 to 9 by an descending order

Step2:
1. Open that file with ReadOnly permissions and take the cursor to the first character of the file
2. Let the user decide what direction to go  [1- forward 2-backward]
3. Then, the user must decide how many steps to move.
4. If the user hits one of the characters 'TREASURE',  print to the user how many times it took to get there
    If not, send a msg to the user that the game continues until the cursor hits one of the 'TREASURE' characters.

"""

# Global env
steps_to_win = 0


def create_new_game_file():
    game_file = open("find_the_treasure_file.txt", 'w')
    for chr in range(10):
        for i in range(randint(1, 20)):
            game_file.write(str(chr))

    game_file.write('TREASURE')

    for chr in range(9, 0, -1):
        for i in range(randint(1, 20)):
            game_file.write(str(chr))
    game_file.close()



# The challenge
# If the player guessed under ten guesses, record the name and the score to a CSV file table
def etgar(steps_to_win):
    pass


print('Welcome to the "find the treasure" game ')
# Step1
create_new_game_file()

# Step2
with open("find_the_treasure_file.txt", 'r') as game_file:
    current_chr = (0, 0)
    chr = ''

    while True:
        direction = input("Where do you want to move? [1- forward 2-backwards] ")
        num_of_steps = int(input("How many characters? "))

        if direction == '1':
            # TODO - Forward steps
            chr = get_forward_chr(current_chr, num_of_steps)
            steps_to_win += 1
        elif direction == '2':
            # TODO - Backwards steps
            chr = get_backward_chr(current_chr, num_of_steps)
            steps_to_win += 1
        else:
            continue  # If the user didn't use '1' or '2', ask an input again...

        print(f'You hit the character “{chr}” ')
        if chr in 'TREASURE':
            break
        else:
            print('… again … until hit one of the “TREASURE” letters…')

print(f'It took you {steps_to_win} steps to get there')
if steps_to_win <= 10:
    etgar(steps_to_win)
