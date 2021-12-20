class Node:
    distance = None
    edges = []
    name = None
    replaced = False
    
    def __init__(self, name):
        self.distance = None
        self.replaced = False
        self.edges = []
        self.name = name
    
    def add_edge(self, node, distance):
        self.edges.append((distance, node))
    
    def __lt__(self, other):
        if self.distance == None:
            return False
        elif other.distance == None:
            return True
        else:
            return self.distance < other.distance

def explore_paths(path, node):
    max_path = None
    for edge in node.edges:
        if not edge[1].name in path:
            test_path = path.copy()
            test_path[0] += edge[0]
            test_path.append(edge[1].name)
            test_path = explore_paths(test_path, edge[1])
            if max_path == None or test_path[0] > max_path[0]:
                max_path = test_path
    if max_path == None:
        return path
    else:
        return max_path

with open('input.txt') as file:
    nodes = dict()
    edges = []
    for line in file:
        line = line.strip().split()
        if len(line) != 5:
            break
        if not line[0] in nodes:
            nodes[line[0]] = Node(line[0])
        if not line[2] in nodes:
            nodes[line[2]] = Node(line[2])
        nodes[line[0]].add_edge(nodes[line[2]],int(line[4]))
        nodes[line[2]].add_edge(nodes[line[0]],int(line[4]))
        edges.append((int(line[4]),line[0],line[2]))
    max_path = None
    for node in nodes.keys():
        path = [0, node]
        path = explore_paths(path, nodes[node])
        if max_path == None or path[0] > max_path[0]:
            max_path = path
    print(max_path[0])