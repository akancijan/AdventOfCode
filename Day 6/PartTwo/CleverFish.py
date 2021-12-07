# Swap between example.txt for testing the given example values
# and input.txt to get the final solution
filename = 'example.txt'

with open(filename) as f:
    for line in f.readlines():
        fields = line.split(',')


# Get amount of fish that were present before the first day
starting_number_of_fish = len(fields)
print(f'Starting number of fish : {starting_number_of_fish}')


'''
########## Note ###########

Had to figure out a new way of counting the final number of fish.
Old solution created a new item for each fish spawned, after day 100~ the solution took to long to calculate.
Instead of spawning a new item each time it's easier to just keep track of counters for each day so that 
there are only 9 items at all time to update.

'''
# Creating a list of counters that track how many fish
# are on each day cycle ( between 0-8 )
fish_by_day_status = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# Go over the values from the input file and increase the counters
for item in fields:
    fish_by_day_status[int(item)] += 1


# Number of days given in the task ( 18 / 80 / 256 )
day_timer = 256
print(fish_by_day_status)

print(f'Inital state: {fish_by_day_status}')
sum_of_fish = 0
print()

# Used these to store the number of new fish spawned
# and number of fish that reset their cycle
new_cycle_fish = 0
old_fish_count = 0
for i in range(1, day_timer+1):
    print(f'------- DAWN OF THE NEW DAY ({i}) -------')
    sum_of_fish = 0
    for number in fish_by_day_status:
        sum_of_fish += number
    print(f'Number of fish at the start of the day : {sum_of_fish}')
    print()

    # For each day update counter values
    for idx, fish in enumerate(fish_by_day_status):
        print(f'idx {idx} fish count : {fish}')
        # First check how many new fish are spawned and increase counter for day 8
        if idx == 0:
            # Store the new day 8 counter in a separate variable
            # if not , it will update in this cycle instead of the next day
            old_fish_count = fish_by_day_status[8]
            fish_by_day_status[8] += fish

            # Same for the number of fish that reset their cycle
            new_cycle_fish = fish
            fish_by_day_status[0] -= fish
        # For day 1-7 just update counters
        if idx != 0 and idx != 8:
            fish_by_day_status[idx - 1] += fish
            fish_by_day_status[idx] -= fish
        # When we get to the final counter , update the number of new fish spawned
        # and fish that reset their cycle
        if idx == 8:
            fish_by_day_status[idx - 1] += old_fish_count
            fish_by_day_status[idx] -= old_fish_count
            fish_by_day_status[6] += new_cycle_fish


    sum_of_fish = 0
    print()
    print(f'After {i} days : ', end=" ")
    print(fish_by_day_status)

    # Sum all counters and return the final number of fish after each day
    # ( Last output is our solution )
    for number in fish_by_day_status:
        sum_of_fish += number
    print()
    print(f'Current number of fish after the day : {sum_of_fish}')
    print()
