from collections import defaultdict
from graph import graph


def BFS(graph, root):
    """
    Breadth first search algorithm.
    Time complexity is O(V+E).
    """
    visited = defaultdict(dict)
    depth = defaultdict(dict)

    # initialization
    for v in graph:
        visited[v] = False
        depth[v] = -1
    queue = []
    # push root
    queue.append(root)
    visited[root] = True
    depth[root] = 0
    # search
    while queue: # all vertices will be pushed to queue once O(V)
        s = queue.pop(0)
        print('vertex: ' + s + ' depth: %d, ' % depth[s], end=" ")
        for v in graph[s]: # all adjancent vertices will be scanned O(E)
            if visited[v['ID']] is not True:
                visited[v['ID']] = True
                depth[v['ID']] = depth[s] + 1
                queue.append(v['ID'])
    print('\0')


if __name__ == '__main__':
    g = graph()
    g.addEdge('a', 'b')
    g.addEdge('b', 'c')
    g.addEdge('a', 'c')
    g.addEdge('c', 'd')
    g.addEdge('d', 'e')
    g.addEdge('d', 'f')
    g.addEdge('g', 'h')
    BFS(g.graph, 'a')
