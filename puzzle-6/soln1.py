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
