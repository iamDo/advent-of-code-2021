course = []

with open('./input', 'r') as input_file:
    course = [[line.split(' ')[0], int(line.split(' ')[1])] for line in input_file.readlines()]

aim = 0
horizontal_position = 0
vertical_position = 0

for move in course:
    if move[0] == 'down':
        aim += move[1]
    elif move[0] == 'up':
        aim -= move[1]
    elif move[0] == 'forward':
        horizontal_position += move[1]
        vertical_position += aim*move[1]

print(vertical_position*horizontal_position)
