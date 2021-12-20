with open('input.txt') as file:
    ribbon = 0
    for line in file:
        dims = line.split('x')
        for i in range(len(dims)):
            dims[i] = int(dims[i])
        ribbon += 2 * sum(dims) - 2 * max(dims) + dims[0] * dims[1] * dims[2]
    print(ribbon)