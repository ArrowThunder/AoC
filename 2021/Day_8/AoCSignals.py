def parse_line(line):
    line = line.split('|')
    inputs = line[0].split()
    outputs = line[1].split()
    return inputs, outputs

with open('input.txt') as file:
    total = 0
    for line in file:
        inputs, outputs = parse_line(line)
        for code in outputs:
            if len(code) == 2 or len(code) == 3 or len(code) == 4 or len(code) == 7:
                total += 1
    print(total)