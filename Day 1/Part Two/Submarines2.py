import csv
import numpy as np

larger_measurements = 0
last_measure = 0
measurements_list = []
sum_list = []
file_in = open('input.txt', 'r')


# Load values into a List
for row in file_in.read().split('\n'):
    if row.isdigit():
        measurements_list.append(float(row))

print(len(measurements_list))


prev_sum = 0
current_sum = 0
current_position = 0

# Go over the imported list and create a new one with values that are equal to the sum of the current element and the next two that follow
for item in measurements_list:

    # If we can't form the requested sum ( we do not have 3 numbers ) we exit the loop
    if current_position+3 > len(measurements_list):
        break
    current_sum = item + measurements_list[current_position+1] + measurements_list[current_position+2]
    sum_list.append(current_sum)
    current_position += 1

print(sum_list)


# Same as part one , we just compare the values of sums
for row in sum_list:
    if last_measure == 0:
        last_measure = float(row)
    if float(row) > last_measure:
        larger_measurements += 1
        print(float(row))
    last_measure = float(row)

print(larger_measurements)



