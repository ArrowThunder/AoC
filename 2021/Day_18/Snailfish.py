class Pair:
    left = None
    right = None
    parent = None
    
    def __init__(self, parent = None):
        self.left = None
        self.right = None
        self.parent = parent
    
    def explode(self):
        # print(self)
        curr = self.parent
        prev = self
        # do left side first
        while True:
            if curr == None:
                break
            elif curr.right is prev:
                if type(curr.left) == int:
                    curr.left += self.left
                    break
                else:
                    prev = curr
                    curr = curr.left
            elif curr.left is prev:
                prev = curr
                curr = curr.parent
            elif type(curr.right) == int:
                curr.right += self.left
                break
            else:
                prev = curr
                curr = prev.right
        curr = self.parent
        prev = self
        # now do the right side
        while True:
            if curr == None:
                break
            elif curr.left is prev:
                if type(curr.right) == int:
                    curr.right += self.right
                    break
                else:
                    prev = curr
                    curr = curr.right
            elif curr.right is prev:
                prev = curr
                curr = curr.parent
            elif type(curr.left) == int:
                curr.left += self.right
                break
            else:
                prev = curr
                curr = prev.left
        is_left = self.parent.left is self
        if is_left:
            self.parent.left = 0
        else:
            self.parent.right = 0
    
    def split_left(self):
        if self.left >= 10:
            # print(self.left)
            temp = Pair(self)
            temp.left = int(self.left / 2)
            temp.right = int((self.left + 1) / 2)
            self.left = temp
            return True
        else:
            return False
    
    def split_right(self):
        if self.right >= 10:
            # print(self.right)
            temp = Pair(self)
            temp.left = int(self.right / 2)
            temp.right = int((self.right + 1) / 2)
            self.right = temp
            return True
        else:
            return False
    
    def check_explosions(self, depth):
        if depth == 4:
            return self
        if type(self.left) == Pair:
            test = self.left.check_explosions(depth + 1)
            if test != None:
                return test
        if type(self.right) == Pair:
            test = self.right.check_explosions(depth + 1)
            if test != None:
                return test
        return None
    
    def check_split(self):
        if type(self.left) == int:
            if self.split_left():
                return True
        elif self.left.check_split():
            return True
        if type(self.right) == int:
            if self.split_right():
                return True
        elif self.right.check_split():
            return True
        else:
            return False
    
    def reduce(self):
        while True:
            # print(self)
            test = self.check_explosions(0)
            if test != None:
                test.explode()
            elif not self.check_split():
                break
                
    def magnitude(self):
        left = self.left if type(self.left) == int else self.left.magnitude()
        right = self.right if type(self.right) == int else self.right.magnitude()
        return (left * 3) + (right * 2)
            
    def __add__(self, other):
        output = Pair()
        output.left = self
        output.right = other
        self.parent = output
        other.parent = output
        output.reduce()
        return output
        
    def __IADD__(self, other):
        self = self + other
    
    def __str__(self):
        return '[' + str(self.left) + ',' + str(self.right) + ']'
    
def parse(string):
    root = None
    this = None
    left = True
    for char in string:
        if char == '[':
            # start new pair
            temp = Pair(this)
            if this == None:
                root = temp
            elif left:
                this.left = temp
            else:
                this.right = temp
            this = temp
            left = True
        elif char == ',':
            left = False
        elif char.isdigit():
            if left:
                this.left = int(char)
            else:
                this.right = int(char)
        elif char == ']':
            this = this.parent
            left = False
        else:
            raise Exception('unexpected character')
    return root
    
with open('input.txt') as file:
    root = parse(file.readline().strip())
    print(root)
    for line in file:
        root += parse(line.strip())
        # print()
    print(root.magnitude())