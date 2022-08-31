from random import randint
from os.path import exists
import csv

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
position = 0
length_of_characters = 0


def create_new_game_files():
    # Game file
    game_file = open("find_the_treasure_file.txt", 'w')
    for chr in range(10):
        for i in range(randint(1, 20)):
            game_file.write(str(chr))

    game_file.write('TREASURE')

    for chr in range(9, 0, -1):
        for i in range(randint(1, 20)):
            game_file.write(str(chr))
    game_file.close()

    # Score csv file - If the file does not exist
    if not exists('score_file.csv'):
        score_file = open('score_file.csv', 'w', newline='')
        writer = csv.writer(score_file)
        writer.writerow(['Player_name', ' Score'])
        score_file.close()


def get_position(num_of_steps, length_of_characters):
    if 0 < num_of_steps < length_of_characters:
        return num_of_steps

    if num_of_steps > length_of_characters:
        return num_of_steps - length_of_characters

    if num_of_steps < 0:
        return num_of_steps + length_of_characters

    if num_of_steps == 0:
        return 1  # The first position


# The challenge
# If the player guessed under ten guesses, record the name and the score to a CSV file table
def challenge(steps_to_win, num_of_scores):
    print()  # For space
    player_name = input('Congrads! You\'ve guessed won the game! What is your name?  ')
    with open('score_file.csv', 'a', newline='') as players_file:
        write_payer = csv.writer(players_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        write_payer.writerow([player_name, steps_to_win])

    # Creating new_scores_table by list
    score_file = open('score_file.csv', 'r+')
    score_list = list(csv.reader(score_file))

    # Sorting the rows by the 'steps_to_win score'
    score_list.sort(key=lambda x: x[1])

    # If there are more than 10 scores - Delete the last row, which is the lower score
    if num_of_scores > 10:
        score_list.pop()
    score_file.close()

    new_scores_table = open('score_file.csv', 'w+', newline='')

    # writing the new_scores_table into the score file
    with new_scores_table:
        score = csv.writer(new_scores_table)
        score.writerows(score_list)
    new_scores_table.close()


def get_score_file_parameters():
    score_file = open('score_file.csv')
    score_list = list(csv.reader(score_file))
    num_of_scores = len(score_list) - 1  # First row doesn't count as a score
    if num_of_scores > 0:
        lower_score = int(score_list[-1][1])
    else:
        lower_score = 0  # If the CSV is empty
    score_file.close()

    return num_of_scores, lower_score


print('Welcome to the "find the treasure" game ')
# Step1
create_new_game_files()
num_of_scores, lower_score = get_score_file_parameters()

# Step2
with open("find_the_treasure_file.txt", 'r') as game_file:
    while True:
        direction = input("Where do you want to move? [1- forward 2-backwards] ")

        if not direction in '12':
            print("again...")
            continue  # If the user didn't use '1' or '2', ask an input again...

        try:  # For characters which are not numbers
            num_of_steps = int(input("How many characters? "))
        except ValueError:
            print("again...")
            continue

        # For efficiency, if the length is not equal to zero, the variable has been calculated
        if length_of_characters == 0:
            data = game_file.read()
            length_of_characters = len(data)

        if not num_of_steps >= 0:
            print("Pls Write a positive number for the characters' steps")
            continue

        if direction == '1':
            position = get_position(num_of_steps + position, length_of_characters)

        else:  # direction == '2'
            position = get_position((num_of_steps * -1) + position, length_of_characters)

        steps_to_win += 1
        game_file.seek(position)
        chr = game_file.readline(1)

        print(f'You hit the character “{chr}”. ')
        if chr in 'TREASURE':
            break
        else:
            print('… again … until hit one of the “TREASURE” letters…')

print(f'It took you {steps_to_win} steps to get there')

if steps_to_win <= lower_score or num_of_scores <= 10:
    num_of_scores += 1
    challenge(steps_to_win, num_of_scores)

print('Thank you for playing!')
