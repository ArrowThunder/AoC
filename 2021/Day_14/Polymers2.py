def iter(pairs, letters, insertion_table):
    output = dict()
    for pair in pairs:
        count = pairs[pair]
        if pair in insertion_table:
            new = insertion_table[pair]
            if new[0] in letters:
                letters[new[0]] += count
            else:
                letters[new[0]] = count
            for i in range(1,3):
                if new[i] in output:
                    output[new[i]] += count
                else:
                    output[new[i]] = count
        else:
            if pair in output:
                output[pair] += count
            else:
                output[pair] = count
    return output
    
with open('input.txt') as file:
    start = file.readline().strip()
    file.readline()
    insertion_table = dict()
    pairs = dict()
    letters = dict()
    prev = ''
    for char in start:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
        if prev != '':
            pair = prev + char
            if pair in pairs:
                pairs[pair] += 1
            else:
                pairs[pair] = 1
        prev = char
    for line in file:
        line.strip()
        pattern = line.split()
        insertion_table[pattern[0]] = [pattern[2], pattern[0][0]+pattern[2], pattern[2]+pattern[0][1]]
    for i in range(40):
        pairs = iter(pairs, letters, insertion_table)
    print(max(letters.values()) - min(letters.values()))