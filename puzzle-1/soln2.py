measurements = []
with open('./input', 'r') as input_file:
    measurements = [int(line.strip()) for line in input_file.readlines()]

increments = sum([1 if measurements[index + 1] > measurements[index] else 0
    for index in range(0, len(measurements) - 1)])

print(increments)
