with open('input.txt') as file:
    line = file.readline().strip().split()
    y_vals = line[-1].split('..')
    y_vals[0] = y_vals[0].split('=')[1]
    y_vals = [int(y_vals[0]), int(y_vals[1])]
    y_init = -1 * min(y_vals) - 1
    # find the max height of that velocity
    prev = 0
    here = y_init
    print(y_init)
    y_velocity = y_init-1
    while prev < here:
        prev = here
        here = here + y_velocity
        y_velocity -= 1
    print(prev)