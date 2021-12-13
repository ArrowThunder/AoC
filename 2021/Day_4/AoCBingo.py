class board:
    nums, tries, winning_num = None, None, None
    def __init__(self):
        self.nums = dict()
    
    def play(self, numbers):
        cols = [0,0,0,0,0]
        rows = [0,0,0,0,0]
        for j in range(len(numbers)):
            n = int(numbers[j])
            if n in self.nums:
                pos = self.nums[n]
                self.nums.pop(n)
                cols[pos[0]] += 1
                rows[pos[1]] += 1
                if 5 in cols or 5 in rows:
                    self.tries = j
                    self.winning_num = n
                    break
    
    def score(self):
        score = 0
        for n in self.nums.keys():
            score += n
        print(score)
        print(self.winning_num)
        return(score * self.winning_num)

minboard = None
with open("input.txt") as file:
    numbers = file.readline().split(',')
    lines = file.readlines()
    lines.pop(0)
    numboards = (len(lines)+1)/6
    for i in range(int(numboards)):
        b = board()
        for y in range(5):
            spaces = lines[6*i + y].split()
            for x in range(5):
                b.nums[int(spaces[x])] = (x,y)
        b.play(numbers)
        if minboard == None or b.tries < minboard.tries:
            minboard = b
print(minboard.score())