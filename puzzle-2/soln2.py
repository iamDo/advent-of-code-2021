measurements = []
window_width = 3

with open('./input', 'r') as input_file:
    measurements = [int(line.strip()) for line in input_file.readlines()]

def get_sum_from_index(index, window_width, measurements):
    return sum([measurements[i] for i in range(index, index + window_width)])

increments = sum([1 if get_sum_from_index(index + 1, window_width, measurements) > get_sum_from_index(index, window_width, measurements) else 0 for index in range(0, (len(measurements) - window_width))])

print(increments)
