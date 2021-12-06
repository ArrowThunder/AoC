class lineseg:
    xy1 = [] # an (x,y) tuple
    xy2 = [] # another (x,y) tuple
    slope = 0.0 # a float
    
    # initialize, and calculate the slope based on the two points
    def __init__(self, xy1, xy2):
        self.xy1 = (int(xy1[0]),int(xy1[1]))
        self.xy2 = (int(xy2[0]),int(xy2[1]))
        denom = self.xy2[0] - self.xy1[0]
        if denom == 0:
            self.slope = float('inf')
        else:
            self.slope = (self.xy2[1]-self.xy1[1])/denom
    
    # determine if a point is within the box sharing xy1 and xy2 as corners
    def boxes(self, point):
        return (min(self.xy1[0],self.xy2[0]) <= point[0] and point[0] <= max(self.xy1[0],self.xy2[0])) and (min(self.xy1[1],self.xy2[1]) <= point[1] and point[1] <= max(self.xy1[1],self.xy2[1]))
    
    # determine if a point is on the line segment
    def contains(self, point):
        if self.slope == float('inf') or self.slope == 0:
            return self.boxes(point)
        else:
            return point[1] == self.slope * (point[0] - self.xy1[0]) + self.xy1[1] and self.boxes(point)
    
    # calculate any points that would intersect between the two line segments
    def intersect(self, line):
        denom = self.slope - line.slope
        output = []
        if self.slope == line.slope:
            # deal with mathbreaking case
            if self.slope == float('inf'):
                if self.xy1[0] != line.xy1[0]:
                    return None
                else:
                    a_min = min(self.xy1[1],self.xy2[1])
                    a_max = max(self.xy1[1],self.xy2[1])
                    b_min = min(line.xy1[1],line.xy2[1])
                    b_max = max(line.xy1[1],line.xy2[1])
                    if a_max >= b_min or b_max >= a_min:
                        for y in range(max(a_min,b_min), min(a_max,b_max) + 1):
                            output.append((self.xy1[0],float(y)))
                        return output
                    else:
                        return None
            
            # check for co-linear lines
            if self.contains(line.xy1) or self.contains(line.xy2):
                a_min = min(self.xy1[0],self.xy2[0])
                a_max = max(self.xy1[0],self.xy2[0])
                b_min = min(line.xy1[0],line.xy2[0])
                b_max = max(line.xy1[0],line.xy2[0])
                if a_max >= b_min or b_max >= a_min:
                    for x in range(max(a_min,b_min), min(a_max,b_max) + 1):
                        y = self.slope * (x - self.xy1[0]) + self.xy1[1]
                        if int(y) == y:
                            output.append((x,y))
                    return output
                else:
                    return None
        elif self.slope == float('inf'):
            x = self.xy1[0]
            if x > max(line.xy1[0],line.xy2[0]) or x < min(line.xy1[0],line.xy2[0]):
                return None
            y = line.slope * (x - line.xy1[0]) + line.xy1[1]
            if int(y) == y and y <= max(self.xy1[1],self.xy2[1]) and y >= min(self.xy1[1],self.xy2[1]):
                return (x,y)
            else:
                return None
        elif line.slope == float('inf'):
            x = line.xy1[0]
            if x > max(self.xy1[0],self.xy2[0]) or x < min(self.xy1[0],self.xy2[0]):
                return None
            y = self.slope * (x - self.xy1[0]) + self.xy1[1]
            if int(y) == y and y <= max(line.xy1[1],line.xy2[1]) and y >= min(line.xy1[1],line.xy2[1]):
                return (x,y)
            else:
                return None
        else:
            x = (self.slope * self.xy1[0] - line.slope * line.xy1[0] + line.xy1[1] - self.xy1[1])/denom
            y = self.slope * (x - self.xy1[0]) + self.xy1[1]
            if int(y) == y and self.boxes((x,y)) and line.boxes((x,y)):
                return (x,y)
            else:
                return None
    
    # for debugging purposes, help print this object pretty
    def __str__(self):
        return 'y = ' + str(self.slope) + '(x - ' + str(self.xy1[0]) + ') + ' + str(self.xy1[1]) + ' to (' + str(self.xy2[0]) + ',' + str(self.xy2[1]) + ')'

def parse_line(entry):
    sliced = entry.split()
    xy1 = sliced[0].split(',')
    xy2 = sliced[2].split(',')
    return xy1, xy2

def main():
    with open('input.txt') as file:
        lines = []
        intersects = set()
        linecount = 0
        for entry in file:
            xy1, xy2 = parse_line(entry)
            new_seg = lineseg(xy1, xy2)
            if new_seg.slope != float('inf') and new_seg.slope != 0.0:
                continue
            for seg in lines:
                intersect = seg.intersect(new_seg)
                if intersect == None:
                    continue
                elif isinstance(intersect,list):
                    for point in intersect:
                        intersects.add(point)
                else:
                    intersects.add(intersect)
            lines.append(lineseg(xy1,xy2))
        print(len(intersects))
        print(len(lines))
main()