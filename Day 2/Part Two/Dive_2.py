## input to solve
file_in = open('input.txt', 'r')
## input given for testing
# file_in = open('example.txt', 'r')
file_input = []
instructions = []
# Get the values from the input and add them to a list
for row in file_in.read().split('\n'):
    file_input.append(row)

# print(file_input)

# Split the values for the instruction and the amount of movement ( 'forward 5' becomes ['forward','5']
for item in file_input:
    instructions.extend(item.split())

#print(instructions)

depth = 0
horizontal_position = 0
aim = 0
current_position = 1


for value in instructions:
    # Only look at the values that have a direction instruction and based on that move the submarine 'up' , 'down' , 'forward'
    if (current_position % 2 == 1):

        # print(f'Aim : {aim} , Depth : {depth} , Position : {horizontal_position}')
        match value:
            case 'forward':
                horizontal_position += float(instructions[current_position])
                if aim == 0:
                    print(f'Current aim is {aim} , depth does not change ( {depth} )')
                # Depth calculation was moved here because of the new rules.
                # Check for 'aim' direction and if it is not equal to 0,  change the depth
                else:
                    depth = depth + (float(instructions[current_position]) * aim)
            # For part two the cases where changed to increase/decrease the 'aim' value
            case 'up':
                aim = aim - float(instructions[current_position])
            case 'down':
                aim = aim + float(instructions[current_position])
            case _:
                print("Invalid input")
    current_position += 1

print(f'Horizontal position : {horizontal_position}')
print(f'Depth : {depth}')
print(f'Aim : {aim}')
print(f'Final position : {horizontal_position*depth}')

