with open('input.txt') as file:
    crabs = file.readline().split(',')
    for i in range(len(crabs)):
        crabs[i] = int(crabs[i])
    crabs.sort()
    pos = len(crabs)/2 - 1
    ave = 0
    if pos != int(pos):
        ave = crabs[int(pos)]
    else:
        ave = round((crabs[int(pos)] + crabs[int(pos)-1])/2)
    fuel = []
    for c in crabs:
        fuel.append(abs(c - int(ave)))
    print(sum(fuel))