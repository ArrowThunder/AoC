def spawn_calc(init, days):
    fish = { init:1 }
    for day in range(days):
        newfish = {}
        for k in fish.keys():
            if k == 0:
                if 6 in newfish:
                    newfish[6] += fish[k]
                else:
                    newfish[6] = fish[k]
                newfish[8] = fish[k]
            else:
                if (k-1) in newfish:
                    newfish[k-1] += fish[k]
                else:
                    newfish[k-1] = fish[k]
        fish = newfish
    return sum(fish.values())

with open('input.txt') as file:
    line = file.readline().split(',')
    fish = []
    for f in line:
        fish.append(int(f))
    fish_spawned = {}
    total = 0
    for f in fish:
        if f not in fish_spawned:
            fish_spawned[f] = spawn_calc(f, 256)
        total += fish_spawned[f]
    print(total)