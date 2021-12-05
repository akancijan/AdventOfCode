import numpy as np


def check_winner(current_score_matrix, current_winners):
    win = False
    current_matrix_id = 0
    for i in range(current_score_matrix.shape[0]):
        for j in range(current_score_matrix.shape[1]):
            if np.all(current_score_matrix[i][j] == 1) and (i not in current_winners):

                win = True
                current_matrix_id = i
            if win and (i not in current_winners):
                break
        if win and (i not in current_winners):
            break

    for i in range(current_score_matrix.shape[0]):
        for j in range(current_score_matrix.shape[1]):
            if np.all(current_score_matrix[i][:, j] == 1) and (i not in current_winners):

                win = True
                current_matrix_id = i
            if win and (i not in current_winners):
                break
        if win and (i not in current_winners):
            break

    return win, current_matrix_id

# Example bingo numbers
#bingo_number_draws = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]

# Column test numbers
#bingo_number_draws = [4, 19, 20, 5, 7, 14, 21, 17, 24]

# Final solution bingo numbers
# ( I manually added these to ease up the handling of file to focus only on the bingo cards )
bingo_number_draws = [46, 79, 77, 45, 57, 34, 44, 13, 32, 88, 86, 82, 91, 97, 89, 1, 48, 31, 18, 10, 55, 74, 24, 11, 80, 78, 28, 37, 47, 17, 21, 61, 26, 85, 99, 96, 23, 70, 3, 54, 5, 41, 50, 63, 14, 64, 42, 36, 95, 52, 76, 68, 29, 9, 98, 35, 84, 83, 71, 49, 73, 58, 56, 66, 92, 30, 51, 20, 81, 69, 65, 15, 6, 16, 39, 43, 67, 7, 59, 40, 60, 4, 90, 72, 22, 0, 93, 94, 38, 53, 87, 27, 12, 2, 25, 19, 8, 62, 33, 75]
bingo_matrix_str = []

# Read input file into an array
# Swap between 'example.txt' and 'input.txt'
with open('input.txt', 'r') as f:
    bingo_matrix_str = [[str(num) for num in line.split('\n')] for line in f if line.strip() != ""]

# Edit read array to remove unwanted symbols
for row in bingo_matrix_str:
    for number in row:
        if number == '':
            row.remove(number)


# Remove double spaces from each row for easier conversion to int()
for index, item in enumerate(bingo_matrix_str):
    for value in item:
        bingo_matrix_str[index] = value.strip().replace('  ', ' ')

bingo_matrix_int = []
temp_row = []
temp_matrix = []

# Get number of bingo cards
number_of_tables = int(len(bingo_matrix_str) / 5)
print(f'Number of tables : {number_of_tables}')

# Convert string values into int() arrays and group them by 5
# to form BINGO cards
counter = 1
for item in bingo_matrix_str:
    temp_row = [int(i) for i in item.split(' ')]
    temp_matrix.append(temp_row)
    if counter % 5 == 0:
        bingo_matrix_int.append(temp_matrix)
        temp_matrix = []
    counter += 1

bingo_card_matrix_values = np.array(bingo_matrix_int)

# Create a separate matrix to track if BINGO was achieved
matrix_shape = bingo_card_matrix_values.shape
bingo_card_matrix_guesses = np.zeros((matrix_shape[0], matrix_shape[1], matrix_shape[2]))

print(matrix_shape)

winner = False
winning_matrix_id = 0
winning_number = 0
winning_sum = 0

winning_boards_id = []

# Go over each bingo card after a number is drawn
for idx, guess in enumerate(bingo_number_draws):
    print(f'Current number to check : {guess}')
    for matrix_id, matrix in enumerate(bingo_card_matrix_values):

        for line_id, line in enumerate(matrix):
            for number_id, number in enumerate(line):
                # If a number was found on the bingo card check if the card is winning
                if guess == number:
                    bingo_card_matrix_guesses[matrix_id][line_id][number_id] = 1
                # Check only the Bingo cards that still have not achieved BINGO!
                if matrix_id not in winning_boards_id:
                    winner, winning_matrix_id = check_winner(bingo_card_matrix_guesses, winning_boards_id)
                    winning_number = guess
                # If the most recent board was a winner and is not in the Bingo winners list
                # Add that board to the list
                if winner and (winning_matrix_id not in winning_boards_id):
                    winning_boards_id.append(winning_matrix_id)
                    winner = False
                    print(f'Card number : {winning_matrix_id} BINGO!')
                    print(f'Added to winning pool')
                    winning_boards_id.sort()
                    print(f'Current winning pool : {winning_boards_id}')
                # Break out of loop only after all the bingo cards have achieved BINGO!
                if len(winning_boards_id) == number_of_tables:
                    print(f'All boards have achieved BINGO ! , last one was board : {winning_matrix_id} ')
                    break

            if len(winning_boards_id) == number_of_tables:
                break
        if len(winning_boards_id) == number_of_tables:
            break
    if len(winning_boards_id) == number_of_tables:
        break

print()

# Compare winning bingo card with the tracker matrix to rule out numbers that were guessed
# and only use the numbers that were not guessed to form the wanted SUM
print(winning_boards_id)
for i in range(bingo_card_matrix_values.shape[1]):
    for j in range(bingo_card_matrix_values.shape[2]):
        if bingo_card_matrix_guesses[winning_matrix_id][i][j] == 0:
            winning_sum += bingo_card_matrix_values[winning_matrix_id][i][j]


print()
print(winning_number)
print(winning_sum)
print(f'Final score : {winning_number*winning_sum}')


