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
