
# Go over every element in input -> check each position of element based on element length
# Increase counter for that position
def most_common_bits(binary_input):
    # Get the length of the binary value to determine further calculations
    len_of_element = len(binary_input[0])
    gamma_counter = 0
    gamma_rate = []
    for i in range(len_of_element):
        gamma_rate.append([0, 0])
    for full_bit in binary_input:
        if gamma_counter == len(full_bit):
            gamma_counter = 0
        for bit in full_bit:
            if bit == '0' and gamma_counter < len_of_element:
                gamma_rate[gamma_counter][0] += 1
            elif bit == '1' and gamma_counter < len_of_element:
                gamma_rate[gamma_counter][1] += 1
            gamma_counter += 1
    return gamma_rate

# Form binary value out of most common bits for easier comparison
def reform_to_binary(given_input):
    binary_value = []
    for value in given_input:
        if value[0] > value[1]:
            binary_value.append(0)
        else:
            binary_value.append(1)
    return binary_value


def inverse_values(given_input):
    inverse_list = []
    for item in given_input:
        if item == 0:
            inverse_list.append(1)
        else:
            inverse_list.append(0)
    return inverse_list


# Remove item and return new list based on gamma binary for given
# position in binary value
# ( Original gamma_binary value is used for Oxygen rating )
# ( Inverse of gamma_binary value is used for CO2 rating )
def get_rating(binary_input, gamma_binary, position_checked):
    gamma_counter = 0
    for full_bit in binary_input[:]:
        if gamma_counter == len(full_bit):
            gamma_counter = 0
        #print(f'position to check : {position_checked}')
        print()
        print(f'current item : {full_bit}')
        if int(full_bit[position_checked]) != gamma_binary[position_checked]:
            print(f'item removed : {full_bit}')
            binary_input.remove(full_bit)
        print()

    return binary_input


binary_input = []
with open('input.txt') as file_in:
    for row in file_in.read().split('\n'):
        binary_input.append(list(row))

# These variables hold information about the number of times that a "0" or a "1" appear in each value
gamma_rate = []
gamma_binary = []
gamma_counter = 0


oxygen_value_found = False
co2_value_found = False


position_checked = 0

# Create copies of the original list to get values for CO2 and Oxygen
binary_input_oxygen = binary_input[:]
binary_input_co2 = binary_input[:]

### Get Oxygen rating
while not oxygen_value_found:
    # Get the most common values for each position
    gamma_rate = most_common_bits(binary_input_oxygen)
    # Create the binary value by looking up what was the most common number
    gamma_binary = reform_to_binary(gamma_rate)

    binary_input_oxygen = get_rating(binary_input_oxygen, gamma_binary, position_checked)
    print()
    print(f'Status after position : {position_checked+1}')
    for full_bit in binary_input_oxygen:
        print(full_bit)

    # Reset values after each deletion
    position_checked += 1
    gamma_rate.clear()
    gamma_binary.clear()

    # Create new empty list to determine most common values
    for i in range(len(binary_input_oxygen[0])):
        gamma_rate.append([0, 0])

    # If we have only one item left , finish the loop

    if len(binary_input_oxygen) == 1:
        oxygen_value_found = True


position_checked = 0

### Get CO2 rating
while not co2_value_found:
    # Get the most common values for each position
    gamma_rate = most_common_bits(binary_input_co2)
    # Create the binary value by looking up what was the most common number
    gamma_binary = inverse_values(reform_to_binary(gamma_rate))

    binary_input_co2 = get_rating(binary_input_co2, gamma_binary, position_checked)

    # Reset values after each deletion
    position_checked += 1
    gamma_rate.clear()
    gamma_binary.clear()

    # Create new empty list to determine most common values
    for i in range(len(binary_input_co2[0])):
        gamma_rate.append([0, 0])


    # If we have only one item left , finish the loop
    if len(binary_input_co2) == 1:
        co2_value_found = True
# print(binary_input_co2)
# print(binary_input_oxygen)

print()

print("Oxygen   :")
for item in binary_input_oxygen:
    print(item)

print("CO2   :")
for item in binary_input_co2:
    print(item)

print()

co2_rating = int("".join(str(x) for x in binary_input_co2[0]), 2)
oxygen_rating = int("".join(str(x) for x in binary_input_oxygen[0]), 2)

print(f'Oxygen rating : {oxygen_rating}')
print(f'Co2 rating : {co2_rating}')
print(f'Life support rating : {oxygen_rating*co2_rating}')