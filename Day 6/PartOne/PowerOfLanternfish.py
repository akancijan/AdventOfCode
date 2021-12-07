# Swap between example.txt for testing the given example values
# and input.txt to get the final solution
filename = 'input.txt'

with open(filename) as f:
    for line in f.readlines():
        fields = line.split(',')


starting_number_of_fish = len(fields)
print(f'Starting number of fish : {starting_number_of_fish}')

# We will use a dictionary that keeps track of each fish.
# Each fish has a unique ID as a key and the value is the current day of it's cycle
fish_dict = {}

# Add each fish as new element into the dictionary
for idx, item in enumerate(fields):
    fish_dict[idx] = int(item)

day_timer = 80

new_fish_index = []
last_fish_index = list(fish_dict)[-1]
final_number_of_fish = 0

print(f' Initial state: {fields}')
for key in fish_dict:
    fish_dict[key] -= 1

for i in range(1,day_timer+1):
    # print(f'After {i} days : ', end=" ")
    # for key in fish_dict:
    #     print(fish_dict[key], end=",")
    print()
    print(f'Number of fish for day {i}: {len(fish_dict)}')
    final_number_of_fish = len(fish_dict)
    # Go over each fish in dictionary and check what their day cycle is
    for key in fish_dict:
        # If the value of the day cycle is 0 , reset it to 6 and create a new ID for the new fish
        # that was spawned
        if fish_dict[key] == 0:
            fish_dict[key] = 6
            if not new_fish_index:
                last_fish_index = list(fish_dict)[-1] + 1
                new_fish_index.append(last_fish_index)
            else:
                last_fish_index = new_fish_index[-1] + 1
                new_fish_index.append(last_fish_index)
        else:
            fish_dict[key] -= 1

    # Go over the list of ID-s of the new fish that were spawned , add them to the dictionary
    # and set their day cycle to 8
    for new_id in new_fish_index:
        fish_dict[new_id] = 8
    new_fish_index.clear()


