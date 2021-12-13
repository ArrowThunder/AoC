with open('input.txt') as file:
    crabs = file.readline().split(',')
    for i in range(len(crabs)):
        crabs[i] = int(crabs[i])
    ave = sum(crabs)/len(crabs)
    fuel = []
    for c in crabs:
        n = abs(c - int(ave))
        fuel.append((n * (n+1))/2)
    print(int(sum(fuel)))