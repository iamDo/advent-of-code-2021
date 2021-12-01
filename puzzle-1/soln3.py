# NXF's solution but fixed
with open('input', 'r') as f:
    data = [int(line.strip()) for line in f.readlines()]

amt = 0
for i in range (0, len(data) - 1):
    if data[i] < data[i + 1]: amt += 1

print(amt)
