import numpy as np

# Change between example.txt for testing
# and input.txt for submission input

# NOTE! I edited the input and example files using regex in notepad++ to format the numbers
# for easier import
with open('input.txt', 'r') as f:
    file_input = [[str(num) for num in line.split('\n')] for line in f if line.strip() != ""]

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

max_coord = 0
min_coord = 0
for item in line_coordinates_matrix:
    # check if x1 = x2
    if item[0] == item[2]:
        if item[1] > item[3]:
            max_coord = item[1]
            min_coord = item[3]
        else:
            max_coord = item[3]
            min_coord = item[1]
        # Move line from min to max
        for i in range(min_coord, max_coord + 1):
            movement_field[i][item[0]] += 1
    # check if y1 = y2
    if item[1] == item[3]:
        if item[0] > item[2]:
            max_coord = item[0]
            min_coord = item[2]
        else:
            max_coord = item[2]
            min_coord = item[0]
        for i in range(min_coord, max_coord + 1):
            movement_field[item[1]][i] += 1

print(movement_field)
# Get maximum number of overlapping lines
maxElement = np.amax(movement_field)
print(maxElement)

count = 0
# Sum up all points where at least 2 points overlap
for i in range(int(maxElement+1)):
    if i >= 2:
        count += np.count_nonzero(movement_field == i)

print(count)



