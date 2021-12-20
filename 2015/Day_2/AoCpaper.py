with open('input.txt') as file:
    area = 0
    for line in file:
        dims = line.split('x')
        for i in range(len(dims)):
            dims[i] = int(dims[i])
        faces = [dims[0] * dims[1], dims[0] * dims[2], dims[1] * dims[2]]
        area += 2 * sum(faces) + min(faces)
    print(area)