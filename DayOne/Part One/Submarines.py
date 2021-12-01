import csv
import numpy as np


# Counter for the number of measurement that were higher than the one before
larger_measurements = 0

last_measure = 0

file_in = open('input.txt', 'r')

#We open the file and read each line as a number
for row in file_in.read().split('\n'):
    if row.isdigit():
        # Check for first measurement
        if last_measure == 0 :
            last_measure = float(row)

        # Compare the current row in file with the previous measurement and increase counter if True
        if float(row) > last_measure:
            larger_measurements += 1
            print(float(row))
        last_measure = float(row)

print(larger_measurements)



