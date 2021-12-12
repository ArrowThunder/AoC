with open('input.txt') as file:
    caves = {}
    for line in file:
        line = line.strip()
        path = line.split('-')
        if path[0] in caves.keys():
            caves[path[0]].append(path[1])
        else:
            caves[path[0]] = [path[1]]
        if path[1] in caves.keys():
            caves[path[1]].append(path[0])
        else:
            caves[path[1]] = [path[0]]
    paths = []
    stack = [['start']]
    while len(stack) > 0:
        here = stack.pop()
        for room in caves[here[-1]]:
            if room.lower() == room and room in here:
                continue
            elif room == 'end':
                paths.append(here.copy())
                paths[-1].append(room)
            else:
                stack.append(here.copy())
                stack[-1].append(room)
    print(len(paths))