class board:
    nums = {}
    tries = float('inf')
    winningNum = -1
    def copy(self):
        toReturn = board()
        toReturn.nums = self.nums.copy()
        toReturn.tries = self.tries
        toReturn.winningNum = self.winningNum
        return toReturn
    def destroy(self):
        self.nums.clear()
        self.tries = float('inf')
        winningNum = -1

minboard = board()
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
        cols = [0,0,0,0,0]
        rows = [0,0,0,0,0]
        for j in range(len(numbers)):
            n = int(numbers[j])
            if n in b.nums:
                pos = b.nums[n]
                b.nums.pop(n)
                cols[pos[0]] += 1
                rows[pos[1]] += 1
                if 5 in cols or 5 in rows:
                    #winner
                    b.tries = float(j)
                    b.winningNum = int(n)
                    break
        if b.tries < minboard.tries:
            minboard = b.copy()
        b.destroy()
score = 0
for n in minboard.nums.keys():
    score += n
print(score)
print(minboard.winningNum)
print(score * minboard.winningNum)