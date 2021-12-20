def iter(start, insertion_table):
    prev = ''
    output = []
    for char in start:
        pair = prev + char
        if prev != '' and pair in insertion_table.keys():
            output.append(insertion_table[pair])
        output.append(char)
        prev = char
    return output

with open('input.txt') as file:
    start = file.readline().strip()
    file.readline()
    insertion_table = dict()
    for line in file:
        line.strip()
        pattern = line.split()
        insertion_table[pattern[0]] = pattern[2]
    for i in range(40):
        start = iter(start, insertion_table)
    chars = set()
    chars.update(start)
    min_count = None
    max_count = None
    for char in chars:
        num = start.count(char)
        if min_count == None or num < min_count:
            min_count = num
        if max_count == None or num > max_count:
            max_count = num
    print(max_count - min_count)