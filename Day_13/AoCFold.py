with open('input.txt') as file:
    coords = set()
    while True:
        line = file.readline().strip().split(',')
        if len(line) < 2:
            break
        coords.add((int(line[0]),int(line[1])))
    line = file.readline().strip().split()
    fold = line[2].split('=')
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
        for coord in coords:
            if coord[1] > max_y:
                y = 2 * max_y - coord[1]
                new_coords.add((coord[0],y))
            else:
                new_coords.add(coord)
    coords.clear()
    coords.update(new_coords)
    print(len(coords))