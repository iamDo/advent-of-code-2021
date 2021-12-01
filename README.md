# Advent of code 2021
My solutions for 2021's advent of code. Probably going to be written almost entirely in Python.
# puzzle-1
## soln1.py
```py
read_lines = []
with open('./input', 'r') as input_file:
    read_lines = input_file.readlines()

increments = 0
decrements = 0
no_change = 0
prev_line = int(read_lines[0].strip())
cur_line = int(read_lines[0].strip())
for line in read_lines:
    prev_line = cur_line
    cur_line = int(line.strip())
    if cur_line > prev_line:
        increments = increments + 1
    elif prev_line > cur_line:
        decrements = decrements + 1
    else:
        no_change = no_change + 1

print(increments)
print(decrements)
print(no_change)
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
