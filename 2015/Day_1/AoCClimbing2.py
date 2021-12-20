with open('input.txt') as file:
    line = file.readline()
    floor = 0
    turn = 0
    for char in line:
        turn += 1
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        if floor == -1:
            break
    print(turn)