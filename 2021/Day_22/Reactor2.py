def tuplify(my_list):
    return (
        my_list[0],
        my_list[1],
        my_list[2]
    )

def listify(my_tuple):
    return [
        my_tuple[0],
        my_tuple[1],
        my_tuple[2]
    ]

class Cuboid:
    min_coord = None
    max_coord = None
    on = None
    
    def __init__(self, a, b, on):
        self.min_coord = a
        self.max_coord = b
        self.on = on
        
    def volume(self):
        vol = 1
        for i in range(3):
            vol *= self.max_coord[i] + 1 - self.min_coord[i]
        # if vol < 1:
            # print('Volume: ' + str(vol))
            # raise Exception('impossible volume error')
        return vol
    
    def intersects(self, other):
        for i in range(3):
            if self.min_coord[i] > other.max_coord[i] or self.max_coord[i] < other.min_coord[i]:
                return False
        return True
    
    def overlap(self, other):
        if not self.intersects(other):
            return None
        new_min = (
            max(self.min_coord[0], other.min_coord[0]),
            max(self.min_coord[1], other.min_coord[1]),
            max(self.min_coord[2], other.min_coord[2])
        )
        new_max = (
            min(self.max_coord[0], other.max_coord[0]),
            min(self.max_coord[1], other.max_coord[1]),
            min(self.max_coord[2], other.max_coord[2])
        )
        return Cuboid(new_min, new_max, self.on)
    
    # returns a list of regions which combined encompass the area in self but not in other
    def subtract(self, other):
        diff = self.overlap(other)
        if diff == None:
            return [self], None
        # we will shave away up to 6 regions of self to carve out other
        work = self
        new = []
        for i in range(3):
            if diff.min_coord[i] > work.min_coord[i]:
                # slice off the cuboid along the lower (x,y,z)[i] plane
                moddable = listify(work.max_coord)
                moddable[i] = diff.min_coord[i] - 1
                new_max = tuplify(moddable)
                new.append(Cuboid(work.min_coord, new_max, self.on))
                
                # update the working region
                moddable = listify(work.min_coord)
                moddable[i] = diff.min_coord[i]
                work_min = tuplify(moddable)
                work = Cuboid(work_min, work.max_coord, self.on)
            if diff.max_coord[i] < work.max_coord[i]:
                # slice off the cuboid along the upper (x,y,z)[i] plan
                moddable = listify(work.min_coord)
                moddable[i] = diff.max_coord[i] + 1
                new_min = tuplify(moddable)
                new.append(Cuboid(new_min, work.max_coord, self.on))
                
                # update the working region
                moddable = listify(work.max_coord)
                moddable[i] = diff.max_coord[i]
                work_max = tuplify(moddable)
                work = Cuboid(work.min_coord, work_max, self.on)
        # if work.min_coord != diff.min_coord or work.max_coord != diff.max_coord:
            # raise Exception('cuboid subtraction error')
        # vol = diff.volume()
        # for section in new:
            # vol += section.volume()
        # if self.volume() != vol:
            # raise Exception('volume mismatch error')
        return new, diff
    
    # gives the operating volume after factoring in all regions
    def operate(self, regions):
        if self.on:
            operating = [self]
            missing = []
        else:
            operating = []
            missing = [self]
        for cuboid in regions:
            if self.on == cuboid.on:
                new = []
                for mini in operating:
                    remainder, difference = mini.subtract(cuboid)
                    if difference == None:
                        new.append(mini)
                        continue
                    new.extend(remainder)
                    missing.append(difference)
                operating = new
            else:
                new = []
                for mini in missing:
                    remainder, difference = mini.subtract(cuboid)
                    if difference == None:
                        new.append(mini)
                        continue
                    operating.append(difference)
                    new.extend(remainder)
                missing = new
        if len(operating) == 0:
            return 0
        else:
            vol = 0
            for region in operating:
                vol += region.volume()
            return vol if self.on else -1 * vol
    
    def __str__(self):
        output = 'From ' + str(self.min_coord) + ' to ' + str(self.max_coord) + ': ' + str(self.volume()) + ' cubes '
        output += 'on' if self.on else 'off'
        return output
    
def parse_token(string):
    string = string.split('=')
    output = string[1].split('..')
    return [int(output[0]), int(output[1])]

with open('input.txt') as file:
    regions = []
    cubes_on = 0
    initializing = True
    for line in file:
        line = line.strip().split()
        if len(line) < 2:
            continue
        command = line[0]
        tokens = line[1].split(',')
        x = parse_token(tokens[0])
        y = parse_token(tokens[1])
        z = parse_token(tokens[2])
        a, b = (x[0],y[0],z[0]), (x[1],y[1],z[1])
        if initializing and abs(a[0]) > 50:
            print(cubes_on)
            regions = []
            initializing = False
        on = True if command == 'on' else False
        new = Cuboid(a, b, on)
        cubes_on += new.operate(regions)
        regions.append(new)
    print(cubes_on)