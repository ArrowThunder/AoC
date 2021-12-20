with open('input.txt') as file:
    houses = {(0,0)}
    line = file.readline()
    # x is west/east (east positive)
    # y is north/south (north positive)
    pos = (0,0) 
    for char in line:
        if char == '^': # north
            pos = (pos[0], pos[1]+1)
        elif char == 'v': # south
            pos = (pos[0], pos[1]-1)
        elif char == '>': # east
            pos = (pos[0]+1, pos[1])
        elif char == '<': # west
            pos = (pos[0]-1, pos[1])
        houses.add(pos)
    print(len(houses))