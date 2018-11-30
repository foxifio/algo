import copy
import math
from collections import defaultdict


class Graph(object):
    def __init__(self, vertex=[]):
        self.vertex = set()
        self.neighbours = defaultdict(set)
        self.dist = {}

    def add_vertex(self, *vertexs):
        [self.vertex.add(n) for n in vertexs]

    def add_edge(self, froom, to, d=1e309):
        self.add_vertex(froom, to)
        self.neighbours[froom].add(to)
        self.dist[froom, to] = d

    def Deixtra(self, start, maxD=1e309):
        totalDistance = defaultdict(lambda: 1e309)
        totalDistance[start] = 0  #
        temp_vertex = {}
        unvisited = copy.copy(self.vertex)

        while unvisited:
            current = unvisited.intersection(totalDistance.keys())
            if not current: break
            min_node = min(current, key=totalDistance.get)
            unvisited.remove(min_node)

            for neighbour in self.neighbours[min_node]:
                d = totalDistance[min_node] + self.dist[min_node, neighbour]
                if totalDistance[neighbour] > d and maxD >= d:
                    totalDistance[neighbour] = d
                    temp_vertex[neighbour] = min_node
        return totalDistance, temp_vertex

    def min_path(self, start, end, maxD=1e309):
        totalDistance, temp_vertex = self.Deixtra(start, maxD)
        dist = totalDistance[end]
        backpath = [end]
        try:
            while end != start:
                end = temp_vertex[end]
                backpath.append(end)
            path = list(reversed(backpath))
        except KeyError:
            path = None

        return dist, path


def read_file(filename):
    with open(filename) as file:
        lines = file.readlines()

    vertex_count = int(lines[0].split(" ")[0])
    clients = list(map(int, lines[1].split(" ")))
    vertexs = []
    for i in range(1, vertex_count + 1):
        vertexs.append(i)

    return vertexs, clients, lines[2:]


vertexs, clients, edges = read_file("gamsrv.in")

graph = Graph(vertexs)

for edge in edges:
    values = list(map(int, edge.split(" ")))
    graph.add_edge(values[0], values[1], values[2])
    graph.add_edge(values[1], values[0], values[2])

min_total_path = math.inf
for node in range(1, vertexs.__len__() + 1):
    if vertexs in clients:
        continue

    max_path_length = graph.min_path(node, clients[0])[0]

    for j in range(1, clients.__len__()):
        path_length = graph.min_path(node, clients[j])[0]
        if max_path_length < path_length:
            max_path_length = path_length

    if min_total_path > max_path_length:
        min_total_path = max_path_length

print(min_total_path)
