course = []

with open('./input', 'r') as input_file:
    course = [[line.split(' ')[0], int(line.split(' ')[1])] for line in input_file.readlines()]

aim = horizontal_position = vertical_position = 0

for move in course:
    if move[0] == 'forward':
        horizontal_position += move[1]
        vertical_position += aim*move[1]
    else:
        aim += (move[1],-move[1])[move[0]=='up']

print(vertical_position*horizontal_position)
