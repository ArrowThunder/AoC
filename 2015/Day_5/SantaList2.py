with open('input.txt') as file:
    num_nice = 0
    for line in file:
        line = line.strip()
        prev = ['','','']
        pairs = set()
        repeat = False
        mirror = False
        for char in line:
            if prev[-1] != '':
                pair = prev[-1] + char
                if pair in pairs:
                    if prev[-1] == char and prev[-2] == char and prev[-3] != char:
                        mirror = True
                    else:
                        repeat = True
                else:
                    pairs.add(pair)
            if char == prev[-2]:
                mirror = True
            prev.append(char)
            prev.pop(0)
        if repeat and mirror:
            num_nice += 1
    print(num_nice)