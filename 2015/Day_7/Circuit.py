def helper(circuit, command):
    a, b = None, None
    if command[0].isdigit():
        a = int(command[0])
    else:
        a = emulate(circuit, command[0])
    if command[2].isdigit():
        b = int(command[2])
    else:
        b = emulate(circuit, command[2])
    return a, b

def emulate(circuit, target):
    command = circuit[target]
    if type(command) == int:
        # base case
        return command
    elif len(command) == 1:
        # should be either a wire substitution or a value insertion
        if command[0].isdigit():
            # hidden base case
            circuit[target] = int(command[0])
        elif command[0].isalpha():
            circuit[target] = emulate(circuit, command[0])
        else:
            raise Exception('outside params')
    elif len(command) == 2:
        # should always be a not
        circuit[target] = ~emulate(circuit, command[1])
    else:
        # should be wire action wire
        if command[1] == 'AND':
            a, b = helper(circuit, command)
            circuit[target] = a & b
        elif command[1] == 'OR':
            a, b = helper(circuit, command)
            circuit[target] = a | b
        elif command[1] == 'LSHIFT':
            a, b = helper(circuit, command)
            circuit[target] = a << b
        elif command[1] == 'RSHIFT':
            a, b = helper(circuit, command)
            circuit[target] = a >> b
        else:
            raise Exception('unexpected command')
    return circuit[target]

with open('input.txt') as file:
    circuit = {
        'd': 72,
        'e': 507,
        'f': 492,
        'g': 114,
        'h': 65412,
        'i': 65079,
        'x': 123,
        'y': 456
    }
    for line in file:
        line = line.strip().split()
        if len(line) > 1:
            circuit[line[-1]] = line[:-2]
    print(emulate(circuit, 'a'))