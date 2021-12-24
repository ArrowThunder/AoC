def change_reactor(reactor, a, b, func):
    for x in range(a[0], b[0] + 1):
        for y in range(a[1], b[1] + 1):
            for z in range(a[2], b[2] + 1):
                func(reactor, (x,y,z))

def turn_on(reactor, pos):
    reactor.add(pos)

def turn_off(reactor, pos):
    reactor.discard(pos)

def parse_token(string):
    string = string.split('=')
    output = string[1].split('..')
    return [int(output[0]), int(output[1])]

reactor = set()
with open('input.txt') as file:
    for line in file:
        line = line.strip().split()
        if len(line) < 2:
            continue
        command = line[0]
        tokens = line[1].split(',')
        x = parse_token(tokens[0])
        y = parse_token(tokens[1])
        z = parse_token(tokens[2])
        a, b = (x[0],y[0],z[0]), (x[1],y[1],z[1])
        if abs(a[0]) > 50:
            break
        if command == 'on':
            change_reactor(reactor, a, b, turn_on)
        elif command == 'off':
            change_reactor(reactor, a, b, turn_off)
print(len(reactor))