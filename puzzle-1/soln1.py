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
