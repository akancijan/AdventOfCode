
binary_input = []
with open('input.txt') as file_in:
    for row in file_in.read().split('\n'):
        binary_input.append(list(row))

# Get the length of the binary value to determine further calculations
len_of_element = len(binary_input[0])
# print(binary_input)
# print(len_of_element)

gamma_rate = []
gamma_counter = 0
# Create a counter for the most common number in each position for the binary number
for i in range(len_of_element):
    gamma_rate.append([0, 0])

# For each full bit  value go over individual number and increase the counter
# depending if it's a 0 or 1
for full_bit in binary_input:
    if gamma_counter == len_of_element:
        gamma_counter = 0
    for bit in full_bit:
        if bit == '0' and gamma_counter < len_of_element:
            gamma_rate[gamma_counter][0] += 1
        elif bit == '1' and gamma_counter < len_of_element:
            gamma_rate[gamma_counter][1] += 1
        gamma_counter += 1

# print(gamma_rate)

gamma_binary = []
# Create the binary value by looking up what was the most common number
for gamma_value in gamma_rate:
    if gamma_value[0] > gamma_value[1]:
        gamma_binary.append(0)
    else:
        gamma_binary.append(1)

# print(gamma_binary)

# Convert the binary value into decimal
gamma_result = int("".join(str(x) for x in gamma_binary), 2)
# print(gamma_result)

epsilon_binary = []

# Inverse the gamma result to get epsilon binary value to convert into decimal
for item in gamma_binary:
    if item == 0:
        epsilon_binary.append(1)
    else:
        epsilon_binary.append(0)

epsilon_result = int("".join(str(x) for x in epsilon_binary), 2)

print(f'Epsilon Binary : {epsilon_binary} Epsilon result :  {epsilon_result}')
print(f'Gamma Binary : {gamma_binary} Gamma result : {gamma_result}')
print(f'Power consumption of the submarine is : {epsilon_result*gamma_result}')
