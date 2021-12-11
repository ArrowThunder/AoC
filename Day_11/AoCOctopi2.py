NUM_ROWS = 10
NUM_COLS = 10

with open('input.txt') as file:
    octopi = []
    for row in range(NUM_ROWS):
        line = file.readline()
        octopi.append([])
        for col in range(NUM_COLS):
            octopi[row].append(int(line[col]))
    step = 0
    while True:
        step += 1
        flashes = []
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                octopi[row][col] += 1
                check = [(row, col)]
                while (len(check) > 0):
                    this = check.pop()
                    r, c = this[0], this[1]
                    if this in flashes:
                        continue
                    if octopi[r][c] > 9:
                        # flashes
                        flashes.append(this)
                        # check clearances
                        north = r > 0
                        west = c > 0
                        south = r < (NUM_ROWS - 1)
                        east = c < (NUM_COLS - 1)
                        # add 1 to all nearby and check them too
                        if north:
                            check.append((r-1,c))
                            octopi[r-1][c] += 1
                            if west:
                                check.append((r-1,c-1))
                                octopi[r-1][c-1] += 1
                            if east:
                                check.append((r-1,c+1))
                                octopi[r-1][c+1] += 1
                        if south:
                            check.append((r+1,c))
                            octopi[r+1][c] += 1
                            if west:
                                check.append((r+1,c-1))
                                octopi[r+1][c-1] += 1
                            if east:
                                check.append((r+1,c+1))
                                octopi[r+1][c+1] += 1
                        if west:
                            check.append((r,c-1))
                            octopi[r][c-1] += 1
                        if east:
                            check.append((r,c+1))
                            octopi[r][c+1] += 1
        for point in flashes:
            row, col = point[0], point[1]
            octopi[row][col] = 0
        if len(flashes) == NUM_COLS * NUM_ROWS:
            print(step)
            break