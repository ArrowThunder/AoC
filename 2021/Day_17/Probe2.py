with open('input.txt') as file:
    line = file.readline().strip().split()
    y_vals = line[-1].split('..')
    y_vals[0] = y_vals[0].split('=')[1]
    y_vals = [int(y_vals[0]), int(y_vals[1])]
    x_vals = line[-2].split(',')
    x_vals = x_vals[0].split('..')
    x_vals[0] = x_vals[0].split('=')[1]
    x_vals = [int(x_vals[0]), int(x_vals[1])]
    x_vals.sort()
    y_vals.sort()
    y_max = -1 * y_vals[0]
    y_min = y_vals[0]
    x_max = x_vals[1]
    x_min = 0
    
    num_angles = 0
    for x_init in range(x_max + 1):
        for y_init in range(y_min, y_max):
            pos = [0,0]
            x_vel = x_init
            y_vel = y_init
            while True:
                pos[0] += x_vel
                pos[1] += y_vel
                if x_vel > 0:
                    x_vel -= 1
                y_vel -= 1
                if pos[0] > x_vals[1] or pos[1] < y_vals[0]:
                    break
                elif pos[0] >= x_vals[0] and pos[1] <= y_vals[1]:
                    num_angles += 1
                    break
    print(num_angles)