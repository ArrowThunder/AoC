def parse_line(line):
    line = line.split('|')
    inputs = line[0].split()
    outputs = line[1].split()
    return inputs, outputs

def decode_line(inputs, outputs):
    one = ''
    c, e, f = '', '', ''
    five_seg = [] # 2,3,5
    six_seg = [] # 0,6,9
    
    # get critical data from the inputs
    for code in inputs:
        if len(code) == 2:
            one = code
        elif len(code) == 5:
            five_seg.append(code)
        elif len(code) == 6:
            six_seg.append(code)
    # begin deciphering the inputs
    # find 6 to determine c and f
    for code in six_seg:
        if not (one[0] in code):
            c = one[0]
            f = one[1]
            break
        elif not (one[1] in code):
            c = one[1]
            f = one[0]
            break
    # knowing c and f, determine 5, and therefore e
    for code in five_seg:
        if not (c in code):
            for letter in ['a','b','c','d','e','f','g']:
                if letter != c and not (letter in code):
                    e = letter
                    break
            break
    
    output = ''
    for code in outputs:
        output += seg_decode(code, c, e, f)
    print(output)
    return int(output)

# decipher a code based on its length and the c, e, and f segments
def seg_decode(code, c, e, f):
    if len(code) == 2:
        return '1'
    elif len(code) == 3:
        return '7'
    elif len(code) == 4:
        return '4'
    elif len(code) == 5:
        if e in code:
            return '2'
        elif not (c in code):
            return '5'
        else:
            return '3'
    elif len(code) == 6:
        if not (c in code):
            return '6'
        elif not (e in code):
            return '9'
        else:
            return '0'
    else:
        return '8'

with open('input.txt') as file:
    total = 0
    for line in file:
        inputs, outputs = parse_line(line)
        total += decode_line(inputs, outputs)
    print(total)