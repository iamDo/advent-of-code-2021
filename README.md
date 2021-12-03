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
## soln2.py
```py
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
```
## soln3.py
```py
c=[]
p=' '
with open('./input','r')as f:
    c=[[l.split(p)[0],int(l.split(p)[1])]for l in f.readlines()]
a=h=v=0
for m in c:
    l,d=m[1],m[0]
    if d=='forward':
        h+=l
        v+=a*l
    else:
        a+=(l,-l)[d=='up']
print(v*h)
```
# puzzle-5
## soln1.py
```py
report = []

with open('./input', 'r') as input_file:
    report = [[int(char) for char in line.strip()] for line in input_file.readlines()]

gamma_rate = [0] * len(report[0])

for line in report:
    for i in range(0, len(line)):
        gamma_rate[i] += line[i]

gamma_rate = ''.join(['1' if v > 500 else '0' for v in gamma_rate])
epsilon_rate = ''.join([ '0' if v == '1' else '1' for v in gamma_rate])

print(int(gamma_rate, 2) * int(epsilon_rate ,2))
```
# puzzle-6
## input_simple
```py
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
```
## soln1.py
```py
report = []

with open('./input', 'r') as input_file:
    report = [[int(char) for char in line.strip()] for line in input_file.readlines()]

oxygen_report = report
scrubber_report = report

for i in range(0, len(report[0])):
    transposed_oxygen_report = [[row[j] for row in oxygen_report] for j in range(len(oxygen_report[0]))]
    zero_count = sum([1 if v == 0 else 0 for v in transposed_oxygen_report[i]])
    one_count = sum([1 if v == 1 else 0 for v in transposed_oxygen_report[i]])
    most_common = 0
    if one_count >= zero_count:
        most_common = 1

    oxygen_report = [v for v in oxygen_report if v[i] == most_common]
    if len(oxygen_report) == 1:
        break


for i in range(0, len(report[0])):
    transposed_scrubber_report = [[row[j] for row in scrubber_report] for j in range(len(scrubber_report[0]))]
    zero_count = sum([1 if v == 0 else 0 for v in transposed_scrubber_report[i]])
    one_count = sum([1 if v == 1 else 0 for v in transposed_scrubber_report[i]])
    for l in scrubber_report:
        print(l)
    least_common = 1
    if zero_count <= one_count:
        least_common = 0

    scrubber_report = [v for v in scrubber_report if v[i] == least_common]
    print()
    if len(scrubber_report) == 1:
        break

oxygen_value = int(''.join([str(v) for v in oxygen_report[0]]), 2)
scrubber_value = int(''.join([str(v) for v in scrubber_report[0]]), 2)

print(oxygen_value*scrubber_value)
```
