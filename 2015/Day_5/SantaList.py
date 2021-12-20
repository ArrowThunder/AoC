with open('input.txt') as file:
    nice = 0
    for line in file:
        line = line.strip()
        prev = ''
        vowels = 0
        double = False
        naughty = False
        for char in line:
            # check for vowels
            if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
                vowels += 1
            # check for double letters
            if char == prev:
                double = True
            # check for bad pairs
            if (prev == 'a' and char == 'b') or (prev == 'c' and char == 'd') or (prev == 'p' and char == 'q') or (prev == 'x' and char == 'y'):
                naughty = True
                break
            prev = char
        if vowels >= 3 and double and not naughty:
            nice += 1
    print(nice)