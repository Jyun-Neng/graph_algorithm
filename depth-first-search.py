from collections import defaultdict
from graph import graph


def DFSVisit(depth, vertex, visited, graph):
    """
    Recursive call function.
    """
    visited[vertex] = True
    print('vertex: ' + vertex + ' depth: %d' % depth)

    for v in graph[vertex]:
        if visited[v['ID']] is not True:
            new_depth = depth + 1   # next depth
            DFSVisit(new_depth, v['ID'], visited, graph)


def DFS(graph, root):
    """
    Depth first search algorithm.
    Time complexity is O(V+E).
    """
    visited = defaultdict(dict)

    # initialization
    for v in graph:
        visited[v] = False

    # Here I do not handle disconnected graph
    # so it traverses only the vertices that are reachable from the source vertex
    DFSVisit(0, root, visited, graph)


if __name__ == '__main__':
    g = graph()
    g.addEdge('a', 'b')
    g.addEdge('b', 'c')
    g.addEdge('a', 'c')
    g.addEdge('a', 'i')
    g.addEdge('c', 'd')
    g.addEdge('d', 'e')
    g.addEdge('d', 'f')
    g.addEdge('g', 'h')
    DFS(g.graph, 'a')
