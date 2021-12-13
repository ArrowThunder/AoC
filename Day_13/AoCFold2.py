with open('input.txt') as file:
    coords = set()
    max_x = None
    max_y = None
    while True:
        line = file.readline().strip().split(',')
        if len(line) < 2:
            break
        coords.add((int(line[0]),int(line[1])))
    for line in file:
        temp = line.strip().split()
        fold = temp[2].split('=')
        new_coords = set()
        if fold[0] == 'x':
            max_x = int(fold[1])
            for coord in coords:
                if coord[0] > max_x:
                    x = 2 * max_x - coord[0]
                    new_coords.add((x, coord[1]))
                else:
                    new_coords.add(coord)
        else:
            max_y = int(fold[1])
            new_coords = set()
            for coord in coords:
                if coord[1] > max_y:
                    y = 2 * max_y - coord[1]
                    new_coords.add((coord[0],y))
                else:
                    new_coords.add(coord)
        coords.clear()
        coords.update(new_coords)
    # now print it
    for row in range(max_y + 1):
        to_print = ''
        for col in range(max_x + 1):
            if (col,row) in coords:
                to_print += '█'
            else:
                to_print += ' '
        print(to_print)