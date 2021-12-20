def move(pos, char):
    if char == '^': # north
        return (pos[0], pos[1]+1)
    elif char == 'v': # south
        return (pos[0], pos[1]-1)
    elif char == '>': # east
        return (pos[0]+1, pos[1])
    elif char == '<': # west
        return (pos[0]-1, pos[1])
    
with open('input.txt') as file:
    houses = {(0,0)}
    line = file.readline()
    # x is west/east (east positive)
    # y is north/south (north positive)
    santa_pos = (0,0)
    robo_pos = (0,0)
    santa_turn = True
    for char in line:
        if santa_turn:
            santa_pos = move(santa_pos, char)
            houses.add(santa_pos)
        else:
            robo_pos = move(robo_pos, char)
            houses.add(robo_pos)
        santa_turn = not santa_turn
    print(len(houses))