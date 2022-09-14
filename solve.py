import networkx   as nx
from sys          import maxsize as infinite
from simple_queue import *

def bfs_path_length(graph, first_node):
    """
    Compute the shortest path length of the non-directed graph G
    starting from node first_node. Return a dictionary with the
    distance (in steps) from first_node to all the nodes.
    """

    distance = {}                 # distance from firstNode to all the nodes
    for node in graph.nodes():
        distance[node] = infinite

    Visible = []
    
    queue = Queue()
    queue.enqueue(1)
    History_queue = [1]
    
    distance[1] = 0

    while Queue:
        Current = queue.dequeue()
        if Current not in Visible:
            Visible.append(Current)
            Next_Visibles = graph[Current]
            for visible in Next_Visibles:
                if visible not in Visible and visible not in History_queue:
                    queue.enqueue(visible)
                    History_queue.append(visible)
                    distance[visible] = distance[Current]+1
        if queue.isEmpty():
            break
                    
    return distance
