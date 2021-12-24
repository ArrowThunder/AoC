# determining the probability of different outcomes
dirac_die = dict()
for key in range(3,10): # min of 3d3 is 3, max of 3d3 is 9
    dirac_die[key] = 0

for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            dirac_die[i + j + k] += 1

def move(player, dist):
    player += dist
    player = player % 10
    if player == 0:
        player = 10
    return player

def game(universe, index):
    new_universes = dict()
    new_universes['p1 wins'] = universe['p1 wins']
    new_universes['p2 wins'] = universe['p2 wins']
    gameover = True
    for key in universe.keys():
        if type(key) == str:
            continue
        else:
            gameover = False
        start_pos = key[index][0]
        start_score = key[index][1]
        for dist in dirac_die.keys():
            pos = move(start_pos, dist)
            score = start_score + pos
            num_universes = universe[key] * dirac_die[dist]
            if score >= 21:
                if index == 0:
                    new_universes['p1 wins'] += num_universes
                else:
                    new_universes['p2 wins'] += num_universes
                continue
            new_key = ((pos, score), key[1]) if index == 0 else (key[0], (pos, score))
            if new_key in new_universes:
                new_universes[new_key] += num_universes
            else:
                new_universes[new_key] = num_universes
    return new_universes, gameover

with open('input.txt') as file:
    # we'll keep track of the number of universes involved in each tuple of (position, score)
    universes = dict()
    p1_start = int(file.readline().strip().split()[-1])
    p2_start = int(file.readline().strip().split()[-1])
    universes[((p1_start, 0),(p2_start, 0))] = 1
    universes['p1 wins'] = 0
    universes['p2 wins'] = 0
    p1_turn = True
    gameover = False
    while not gameover:
        new_universes, gameover = game(universes, 0 if p1_turn else 1)
        universes.clear()
        universes.update(new_universes)
        p1_turn = not p1_turn
    p1_wins = universes['p1 wins']
    p2_wins = universes['p2 wins']
    print(max(p1_wins, p2_wins))