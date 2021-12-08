with open('input.txt') as file:
    line = file.readline().split(',')
    fish = []
    for f in line:
        fish.append(int(f))
    for day in range(80):
        newfish = []
        for i in range(len(fish)):
            fish[i] = fish[i] - 1
            if fish[i] == -1:
                fish[i] = 6
                newfish.append(8)
        fish.extend(newfish)
    print(len(fish))