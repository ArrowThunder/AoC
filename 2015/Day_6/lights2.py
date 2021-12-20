def change_field(field, a, b, func):
    min_x = min(a[0],b[0])
    max_x = max(a[0],b[0])
    min_y = min(a[1],b[1])
    max_y = max(a[1],b[1])
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            func(field, (x,y))

def turn_on(field, pos):
    field[pos] += 1

def turn_off(field, pos):
    if field[pos] > 0:
        field[pos] -= 1

def toggle(field, pos):
    field[pos] += 2

field = dict()
for x in range(1000):
    for y in range(1000):
        field[(x,y)] = 0

with open('input.txt') as file:
    for line in file:
        tokens = line.split()
        if tokens[0] == 'turn':
            tokens.pop(0)
        a = tokens[1].split(',')
        a = (int(a[0]), int(a[1]))
        b = tokens[3].split(',')
        b = (int(b[0]), int(b[1]))
        if tokens[0] == 'on':
            change_field(field, a, b, turn_on)
        elif tokens[0] == 'off':
            change_field(field, a, b, turn_off)
        elif tokens[0] == 'toggle':
            change_field(field, a, b, toggle)

print(sum(field.values()))