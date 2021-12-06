file_in = open('input.txt', 'r')
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
current_position = 1


for value in instructions:
    # Only look at the values that have a direction instruction and based on that move the submarine 'up' , 'down' , 'forward'
    if (current_position % 2 == 1):
        match value:
            case 'forward':
                horizontal_position += float(instructions[current_position])
            case 'up':
                depth = depth - float(instructions[current_position])
            case 'down':
                depth = depth + float(instructions[current_position])
            case _:
                print("Invalid input")
    current_position += 1

print(f'Horizontal position : {horizontal_position}')
print(f'Depth : {depth}')
print(f'Final position : {horizontal_position*depth}')

