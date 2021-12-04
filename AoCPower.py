ones = []
zeroes = []
with open('input.txt') as file:
    lines = file.readlines()
    for char in lines[0]:
        if char == '0' or char == '1':
            ones.append(0)
            zeroes.append(0)
    for line in lines:
        i = 0
        for char in line:
            if char == '0':
                zeroes[i] += 1
            elif char == '1':
                ones[i] += 1
            i += 1
gammarate = 0
epsilonrate = 0
for i in range(len(ones)):
    if ones[i] > zeroes[i]:
        gammarate += 2**(len(ones)-i-1)
    else:
        epsilonrate += 2**(len(ones)-i-1)
print(gammarate)
print(epsilonrate)
print(gammarate * epsilonrate)