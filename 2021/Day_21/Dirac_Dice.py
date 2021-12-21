class Die:
    num = None
    
    def __init__(self):
        self.num = 1
    
    def get(self):
        to_return = self.num
        self.num += 1
        if self.num >= 101:
            self.num = 1
        return to_return

def move(player, dist):
    player += dist
    player = player % 10
    if player == 0:
        player = 10
    return player

def game(player, die):
    rolls = die.get() + die.get() + die.get()
    return move(player, rolls)

with open('input.txt') as file:
    p1 = int(file.readline().strip().split()[-1])
    p2 = int(file.readline().strip().split()[-1])
    p1_score = 0
    p2_score = 0
    p1_turn = True
    num_rolls = 0
    die = Die()
    while True:
        if p1_turn:
            p1 = game(p1, die)
            num_rolls += 3
            p1_score += p1
            if p1_score >= 1000:
                break
        else:
            p2 = game(p2, die)
            num_rolls += 3
            p2_score += p2
            if p2_score >= 1000:
                break
        p1_turn = not p1_turn
    print(min(p1_score, p2_score) * num_rolls)