with open('input.txt') as file:
    line = file.readline()
    floor = 0
    for char in line:
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
    print(floor)