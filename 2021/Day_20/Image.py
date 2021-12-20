def bin_n(string):
    num = 0
    for i in range(len(string)):
        index = (i + 1) * -1
        if string[index] == '1':
            num += 2 ** i
    return num

def check_point(image, bounds, point):
    if point[0] <= bounds[0] or point[1] <= bounds[1] or point[0] >= bounds[2] or point[1] >= bounds[3]:
        return bounds[4]
    else:
        return point in image

def enhance(image, bounds, enhancement):
    # expand operating boundaries
    bounds[0] -= 1
    bounds[1] -= 1
    bounds[2] += 1
    bounds[3] += 1
    # perform enhancement
    new = set()
    for row in range(bounds[0], bounds[2] + 1):
        for col in range(bounds[1], bounds[3] + 1):
            string = ''
            for sub_row in (row - 1, row, row + 1):
                for sub_col in (col - 1, col, col + 1):
                    string += '1' if check_point(image, bounds, (sub_row, sub_col)) else '0'
            if enhancement[bin_n(string)] == '#':
                new.add((row, col))
    # check the infinite field
    if bounds[4]:
        bounds[4] = True if enhancement[511] == '#' else False
    else:
        bounds[4] = True if enhancement[0] == '#' else False
    # update the world
    return new, bounds

def print_image(image, bounds):
    for row in range(bounds[0], bounds[2] + 1):
        to_print = ''
        for col in range(bounds[1], bounds[3] + 1):
            if (row,col) in image:
                to_print += '#'
            else:
                to_print += '.'
        print(to_print)
    print()

with open('input.txt') as file:
    enhancement = file.readline().strip()
    file.readline()
    lines = file.readlines()
    bounds = [0, 0, len(lines), None, False]
    image = set()
    for row in range(len(lines)):
        line = lines[row].strip()
        if len(line) == 0:
            continue
        bounds[3] = len(line)
        for col in range(len(line)):
            if line[col] == '#':
                image.add((row,col))
    for i in range(2):
        image, bounds = enhance(image, bounds, enhancement)
    print(len(image))
    for i in range(50-2):
        image, bounds = enhance(image, bounds, enhancement)
    print(len(image))