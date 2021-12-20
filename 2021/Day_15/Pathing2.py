import time
import heapq

class Node:
    point = None
    distance = None
    replaced = False
    
    def __init__(self, point):
        self.point = point
        self.distance = None
        self.replaced = False
    
    def update(self, distance):
        if self.distance == None or distance < self.distance:
            new = Node(self.point)
            new.distance = distance
            self.replaced = True
            return new
        else:
            return None
    
    def neighbors(self, goal):
        n = []
        if self.point[0] > 0:
            n.append((self.point[0] - 1, self.point[1]))
        if self.point[1] > 0:
            n.append((self.point[0], self.point[1] - 1))
        if self.point[0] < goal[0]:
            n.append((self.point[0] + 1, self.point[1]))
        if self.point[1] < goal[1]:
            n.append((self.point[0], self.point[1] + 1))
        return n
    
    def __lt__(self, other):
        if self.distance == None:
            return False
        elif other.distance == None:
            return True
        else:
            return self.distance < other.distance

start_time = None

with open('input.txt') as file:
    risk_base = []
    for line in file:
        line = line.strip()
        risk_line = []
        for char in line:
            risk_line.append(int(char))
        if len(risk_line) > 0:
            risk_base.append(risk_line.copy())
    risks = []
    for big_row in range(5):
        for row in risk_base:
            risks.append([])
        for big_col in range(5):
            for row in range(len(risk_base)):
                for col in range(len(risk_base)):
                    num = (risk_base[row][col] + big_col + big_row) % 9
                    if num == 0:
                        num = 9
                    risks[row + big_row * len(risk_base)].append(num)
    
    goal = (len(risks) - 1, len(risks[0]) - 1)
    nodes = dict()
    for row in range(len(risks)):
        for col in range(len(risks[0])):
            nodes[(row, col)] = Node((row, col))
    nodes[(0,0)].distance = 0
    heap = [nodes[(0,0)]]
    heapq.heapify(heap)
    min_node = None
    start_time = time.time()
    while True:
        min_node = heapq.heappop(heap)
        if min_node.replaced:
            continue
        elif min_node.point == goal:
            break
        for point in min_node.neighbors(goal):
            new = nodes[point].update(min_node.distance + risks[point[0]][point[1]])
            if new != None:
                nodes[point] = new
                heapq.heappush(heap, new)
    print(min_node.distance)

end_time = time.time()
print(end_time - start_time)