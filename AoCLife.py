digits = 0

def getTarget(counts, oxy):
    if oxy:
        if counts[0] > counts[1]:
            return 0
        else:
            return 1
    else:
        if counts[1] < counts[0]:
            return 1
        else:
            return 0

def parser(data, index, oxy=True):
    counts = [0,0]
    for line in data:
        counts[int(line[index])] += 1
    target = getTarget(counts, oxy)
    output = []
    for line in data:
        if int(line[index]) == target:
            output.append(line)
    if len(output) == 1:
        return output[0]
    else:
        return parser(output, index + 1, oxy)

oxygen = ''
CO2 = ''

with open('input.txt') as file:
    lines = file.readlines()
    for char in lines[0]:
        if char == '0' or char == '1':
            digits += 1
    oxygen = parser(lines, 0)
    CO2 = parser(lines, 0, False)

oxyRating = 0
scrubRating = 0

for i in range(digits):
    oxyRating += int(oxygen[i]) * 2**(digits-i-1)
    scrubRating += int(CO2[i]) * 2**(digits-i-1)
print(oxyRating)
print(scrubRating)
print(oxyRating * scrubRating)