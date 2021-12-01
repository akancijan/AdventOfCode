import csv
import numpy as np

larger_measurements = 0
last_measure = 0

file_in = open('input.txt', 'r')


for row in file_in.read().split('\n'):
    if row.isdigit():
        if last_measure == 0 :
            last_measure = float(row)
        if float(row) > last_measure:
            larger_measurements += 1
            print(float(row))
        last_measure = float(row)

print(larger_measurements)



