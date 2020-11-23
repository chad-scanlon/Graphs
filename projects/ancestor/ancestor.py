
from util import Stack, Queue
from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    # dict for each vert
    parents = {}
    # check if vert is in dict, add it if not
    for v in ancestors:
        if v[1] not in parents.keys():
            parents[v[1]] = {v[0]}
        else:
            parents[v[1]].add(v[0])

    # check if vert is in dict, then add it to queue for bfs
    if starting_node not in parents:
        return -1
    else:
        q = Queue()
        q.enqueue(starting_node)
        visited = set()
        path = None

        while q.size() > 0:
            path = q.dequeue()
            if path not in visited:
                visited.add(path)
                if path in parents:
                    for parent in parents[path]:
                        q.enqueue(parent)

        return path