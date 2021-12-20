def parse(string):
    index = 1 # start after first quotation mark
    mem = 0
    while True:
        if string[index] == '\\':
            index += 1
            if string[index] == 'x':
                index += 2
        elif string[index] == '"':
            if index < len(string) - 1:
                raise Exception('string ended too early')
            else:
                break
        mem += 1
        index += 1
    return mem

def encode(string):
    enc = 2 # enclosing quotes
    for char in string:
        if char == '\\' or char == '"':
            enc += 2
        else:
            enc += 1
    return enc

with open('input.txt') as file:
    string_lit = 0
    string_mem = 0
    string_enc = 0
    for line in file:
        line = line.strip()
        string_lit += len(line)
        string_mem += parse(line)
        string_enc += encode(line)
    print(string_lit - string_mem)
    print(string_enc - string_lit)