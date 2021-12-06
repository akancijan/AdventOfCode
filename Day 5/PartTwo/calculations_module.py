import numpy as np


def check_vertical_horizontal_lines(line_coordinates_matrix, movement_field):
    max_coord = 0
    min_coord = 0
    for item in line_coordinates_matrix:
        x1, x2, y1, y2 = item[0], item[2], item[1], item[3]
        if x1 == x2:
            print(f'Vertical Line check successful {item}')
            if y1 > y2:
                max_coord = y1
                min_coord = y2
            else:
                max_coord = y2
                min_coord = y1
            # Add values to movement field moving vertically
            for i in range(min_coord, max_coord + 1):
                movement_field[x1][i] += 1

        if y1 == y2:
            print(f'Horizontal Line check successful {item}')
            if x1 > x2:
                max_coord = x1
                min_coord = x2
            else:
                max_coord = x2
                min_coord = x1
            # Add values to movement field moving horizontally
            for i in range(min_coord, max_coord + 1):
                movement_field[i][y1] += 1
    return movement_field


def check_diagonal_lines(line_coordinates_matrix, movement_field):
    for item in line_coordinates_matrix:
        x1, x2, y1, y2 = item[0], item[2], item[1], item[3]

        dy = y2 - y1
        dx = x2 - x1

        # If dx = dy a diagonal line can be drawn
        # after this check , we check for the direction of the diagonal

        # if dx is a negative number and dy is positive
        if abs(dx) == abs(dy) and (dx < 0 and dy > 0):
            print(f'Diagonal check successful dx < 0 dy > 0, point : {item}')

            # Set starting coordinate
            diagonal_cord_x = x2
            diagonal_cord_y = y2
            # print(f'Diagonal point Start Added: {diagonal_cord_x} , {diagonal_cord_y}')

            # Add starting coordinate to movement field
            movement_field[diagonal_cord_x][diagonal_cord_y] += 1
            for i in range(abs(dy)):
                # Update value of current point while moving diagonally
                diagonal_cord_x = diagonal_cord_x + 1
                diagonal_cord_y = diagonal_cord_y - 1

                # Mark coordinate in field as passed
                movement_field[diagonal_cord_x][diagonal_cord_y] += 1

        # if both dx and dy are positive
        if abs(dx) == abs(dy) and (dx > 0 and dy > 0):

            # Set starting coordinate
            diagonal_cord_x = x1
            diagonal_cord_y = y1

            # Add starting coordinate to movement field
            movement_field[diagonal_cord_x][diagonal_cord_y] += 1
            for i in range(abs(dy)):
                # Update value of current point while moving diagonally
                diagonal_cord_x = diagonal_cord_x + 1
                diagonal_cord_y = diagonal_cord_y + 1

                # Mark coordinate in field as passed
                movement_field[diagonal_cord_x][diagonal_cord_y] += 1

        # if both dx and dy are negative
        if abs(dx) == abs(dy) and (dx < 0 and dy < 0):

            # Set starting coordinate
            diagonal_cord_x = x2
            diagonal_cord_y = y2

            movement_field[diagonal_cord_x][diagonal_cord_y] += 1
            for i in range(abs(dy)):
                # Update value of current point while moving diagonally
                diagonal_cord_x = diagonal_cord_x + 1
                diagonal_cord_y = diagonal_cord_y + 1

                # Mark coordinate in field as passed
                movement_field[diagonal_cord_x][diagonal_cord_y] += 1

        # if dx positive and dy negative
        if abs(dx) == abs(dy) and (dx > 0 and dy < 0):

            # Set starting coordinate
            diagonal_cord_x = x1
            diagonal_cord_y = y1

            # Add starting coordinate to movement field
            movement_field[diagonal_cord_x][diagonal_cord_y] += 1
            for i in range(abs(dy)):
                # Update value of current point while moving diagonally
                diagonal_cord_x = diagonal_cord_x + 1
                diagonal_cord_y = diagonal_cord_y - 1

                # Mark coordinate in field as passed
                movement_field[diagonal_cord_x][diagonal_cord_y] += 1

    return movement_field
