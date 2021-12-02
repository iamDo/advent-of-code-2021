course = []

with open('./input', 'r') as input_file:
    course = [[line.split(' ')[0], int(line.split(' ')[1])] for line in input_file.readlines()]

horizontal_position = sum([move[1] if move[0] == 'down' else -move[1]
    for move in
        [_move for _move in course
        if _move[0] in ['up', 'down']]])

vertical_position = sum([_move[1] for _move in course if _move[0] == 'forward'])

print(vertical_position * horizontal_position)
