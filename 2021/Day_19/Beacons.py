import math

def det(matrix):
    x,y,z = matrix
    a,b,c = x
    d,e,f = y
    g,h,i = z
    return sum([a*e*i,b*f*g,c*d*h,-1*c*e*g,-1*b*d*i,-1*a*f*h])

# get the transformation matrices
def transformations():
    matrices = []
    cols = [0,1,2]
    for x_plus in [True,False]:
        for x_pos in cols:
            my_cols = cols.copy()
            my_cols.remove(x_pos)
            for y_pos in my_cols:
                z_pos = my_cols.copy()
                z_pos.remove(y_pos)
                z_pos = z_pos[0]
                for y_plus in [True,False]:
                    for z_plus in [True,False]:
                        matrix = [[0,0,0],[0,0,0],[0,0,0]]
                        matrix[0][x_pos] = 1 if x_plus else -1
                        matrix[1][y_pos] = 1 if y_plus else -1
                        matrix[2][z_pos] = 1 if z_plus else -1
                        if det(matrix) > 0:
                            matrices.append(matrix)
    return matrices

# tforms = transformations()
# for rot in tforms:
    # beac = (1,2,3)
    # output = (
        # beac[0] * rot[0][0] + beac[1] * rot[1][0] + beac[2] * rot[2][0],
        # beac[0] * rot[0][1] + beac[1] * rot[1][1] + beac[2] * rot[2][1],
        # beac[0] * rot[0][2] + beac[1] * rot[1][2] + beac[2] * rot[2][2]
    # )
    # to_print = []
    # for num in output:
        # if num == 1:
            # to_print.append('x')
        # elif num == 2:
            # to_print.append('y')
        # elif num == 3:
            # to_print.append('z')
        # elif num == -1:
            # to_print.append('-x')
        # elif num == -2:
            # to_print.append('-y')
        # elif num == -3:
            # to_print.append('-z')
        # else:
            # to_print.append('err')
    # print(to_print)

with open('input.txt') as file:
    sensors = []
    sensor = -1
    for line in file:
        line = line.strip()
        if len(line) == 0:
            continue
        line = line.split()
        if line[0] == '---':
            sensor += 1
            sensors.append(set())
        else:
            point = line[0].split(',')
            beacon = (int(point[0]),int(point[1]),int(point[2]))
            sensors[sensor].add(beacon)
    rotations = transformations()
    # we'll define sensor 1 to be (0,0), and build it up with the other sensors
    offsets = [None] * len(sensors)
    offsets[0] = (0,0,0)
    num_pairs = 0
    while len(sensors) > 1:
        breaking = True
        for i in range(len(sensors)):
            if offsets[i] != None:
                continue
            else:
                breaking = False
                print(i)
            for rot in rotations:
                relative = set()
                for beac in sensors[i]:
                    # rotate this point
                    rot_b = (
                        beac[0] * rot[0][0] + beac[1] * rot[1][0] + beac[2] * rot[2][0],
                        beac[0] * rot[0][1] + beac[1] * rot[1][1] + beac[2] * rot[2][1],
                        beac[0] * rot[0][2] + beac[1] * rot[1][2] + beac[2] * rot[2][2]
                    )
                    relative.add(rot_b)
                best_matches = set()
                best_shifted = None
                best_offset = None
                for anchor in sensors[0]:
                    for forced in relative:
                        offset = (anchor[0]-forced[0],anchor[1]-forced[1],anchor[2]-forced[2])
                        shifted = set()
                        matches = set()
                        for point in relative:
                            shifted_point = (point[0]+offset[0],point[1]+offset[1],point[2]+offset[2])
                            shifted.add(shifted_point)
                            if shifted_point in sensors[0]:
                                matches.add(shifted_point)
                        if len(matches) > len(best_matches):
                            best_matches = matches
                            best_shifted = shifted
                            best_offset = offset
                        if len(best_matches) >= 12:
                            break
                    if len(best_matches) >= 12:
                        break
                if len(best_matches) >= 12:
                    sensors[0].update(best_shifted)
                    offsets[i] = best_offset
                    num_pairs += 1
        if breaking:
            break
        else:
            print('looped all sensors, ' + str(num_pairs) + ' pairs found so far')
    print(len(sensors[0]))
    max_dist = 0
    for i in range(len(offsets)):
        offi = offsets[i]
        for j in range(i + 1, len(offsets)):
            offj = offsets[j]
            dist = abs(offi[0] - offj[0]) + abs(offi[1] - offj[1]) + abs(offi[2] - offj[2])
            if dist > max_dist:
                max_dist = dist
    print(max_dist)