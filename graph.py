from collections import defaultdict


class graph:
    """
    Data structure of graph.
    """

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, vertex1, vertex2, weight=None):
        self.graph[vertex1].append({'ID': vertex2, 'weight': weight})
        self.graph[vertex2].append({'ID': vertex1, 'weight': weight})


if __name__ == '__main__':
    g = graph()
    g.addEdge('a', 'b', 2)
    g.addEdge('a', 'c', 3)
    g.addEdge('b', 'c', 4)
    print(g.graph)
