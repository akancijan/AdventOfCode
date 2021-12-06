import numpy as np
from calculations_module import  check_vertical_horizontal_lines, check_diagonal_lines


# Change between example.txt for testing
# and input.txt for submission input
with open('input.txt', 'r') as f:
    file_input = [[str(num) for num in line.split('\n')] for line in f if line.strip() != ""]
# NOTE! I edited the input and example files using regex in notepad++ to format the numbers
# for easier import

# Added a grid of the example solution to test out
# how the diagonals are formed
'''                              grid for [6,4][2,0]
  0 1 2 3 4 5 6 7 8 9            0 1 2 3 4 5 6 7 8 9    

0 1 . 1 . . . . 1 1 .          0 . . 1 . . . . . . .           
1 . 1 1 1 . . . 2 . .          1 . . . 1 . . . . . .
2 . . 2 . 1 . 1 1 1 .          2 . . . . 1 . . . . .
3 . . . 1 . 2 . 2 . .          3 . . . . . 1 . . . .
4 . 1 1 2 3 1 3 2 1 1          4 . . . . . . 1 . . .
5 . . . 1 . 2 . . . .          5 . . . . . . . . . .
6 . . 1 . . . 1 . . .          6 . . . . . . . . . .
7 . 1 . . . . . 1 . .          7 . . . . . . . . . .
8 1 . . . . . . . 1 .          8 . . . . . . . . . .
9 2 2 2 1 1 1 . . . .          9 . . . . . . . . . .
'''

'''
0,9,5,9
8,0,0,8
9,4,3,4
2,2,2,1
7,0,7,4
6,4,2,0
0,9,2,9
3,4,1,4
0,0,8,8
5,5,8,2
'''

# Edit read array to remove unwanted symbols
for row in file_input:
    for number in row:
        if number == '':
            row.remove(number)

temp_row = []
line_coordinates_matrix = []

# Generate matrix that contains coordinates
for item in file_input:
    temp_row = [int(i) for i in item[0].split(',')]
    line_coordinates_matrix.append(temp_row)

# Generate field to determine line drawings
highest_x = 0
highest_y = 0
# Go over the coordinates matrix to find the maximum 'x' and 'y' values
# to form the movement field matrix
for row in line_coordinates_matrix:
    if row[0] > highest_x:
        highest_x = row[0]
    if row[1] > highest_y:
        highest_y = row[1]
    if row[2] > highest_x:
        highest_x = row[2]
    if row[3] > highest_y:
        highest_y = row[3]

print(f'highest_x : {highest_x} highest_y : {highest_y}')
movement_field = np.zeros((highest_x + 1, highest_y + 1))

# Find horizontal and vertical lines and return positions of lines found
movement_field = check_vertical_horizontal_lines(line_coordinates_matrix, movement_field)
# Find diagonal lines and return positions of lines found
movement_field = check_diagonal_lines(line_coordinates_matrix, movement_field)

# Get number of the highest overlap number of lines
maxElement = np.amax(movement_field)
print(maxElement)

count = 0
# Sum up all points where at least 2 points overlap
for i in range(int(maxElement + 1)):

    if i >= 2:
        count += np.count_nonzero(movement_field == i)
        print(f'Sum for {i} = {count}')

# Final solution
print(f'Final solution : {count}')



