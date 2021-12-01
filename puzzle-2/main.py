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
