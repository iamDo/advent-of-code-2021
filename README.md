# Advent of code 2021
My solutions for 2021's advent of code. Probably going to be written almost entirely in Python.
# puzzle-1
## soln1.py
```py
read_lines = []
with open('./input', 'r') as input_file:
    read_lines = input_file.readlines()

increments = 0
prev_line = int(read_lines[0].strip())
cur_line = int(read_lines[0].strip())
for line in read_lines:
    prev_line = cur_line
    cur_line = int(line.strip())
    if cur_line > prev_line:
        increments = increments + 1

print(increments)
```
## soln2.py
```py
measurements = []
with open('./input', 'r') as input_file:
    measurements = [int(line.strip()) for line in input_file.readlines()]

increments = sum([1 if measurements[index + 1] > measurements[index] else 0
    for index in range(0, len(measurements) - 1)])

print(increments)
```
## soln3.py
```py
# NXF's solution but fixed
with open('input', 'r') as f:
    data = [int(line.strip()) for line in f.readlines()]

amt = 0
for i in range (0, len(data) - 1):
    if data[i] < data[i + 1]: amt += 1

print(amt)
```
# puzzle-2
## soln1.py
```py
read_lines = []
with open('./input', 'r') as input_file:
    read_lines = [int(line.strip()) for line in input_file.readlines()]

orig_length = len(read_lines)
lines = read_lines + [0, 0, 0]

prev_depth = None
cur_depth = sum([lines[0], lines[1], lines[2]])
increments = 0
for i in range(1, orig_length - 1):
    prev_depth = cur_depth
    measurements = [lines[i], lines[i + 1], lines[i + 2]]
    cur_depth = sum(measurements)
    if cur_depth > prev_depth:
        increments = increments + 1

print(increments)
```
## soln2.py
```py
measurements = []
window_width = 3

with open('./input', 'r') as input_file:
    measurements = [int(line.strip()) for line in input_file.readlines()]

def get_sum_from_index(index):
    return sum([measurements[i] for i in range(index, index + window_width)])

increments = sum([1 if get_sum_from_index(index + 1) > get_sum_from_index(index) else 0
    for index in range(0, (len(measurements) - window_width))])

print(increments)
```
# puzzle-3
## soln1.py
```py
course = []

with open('./input', 'r') as input_file:
    course = [[line.split(' ')[0], int(line.split(' ')[1])] for line in input_file.readlines()]

horizontal_position = sum([move[1] if move[0] == 'down' else -move[1]
    for move in
        [_move for _move in course
        if _move[0] in ['up', 'down']]])

vertical_position = sum([_move[1] for _move in course if _move[0] == 'forward'])

print(vertical_position * horizontal_position)
```
# puzzle-4
## soln1.py
```py
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
```
