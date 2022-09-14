import networkx  as nx

from graph_utils import *
from solve       import *

graph = build_graph();

first_node = 1

distances = bfs_path_length(graph, first_node)
ordered_distances = dict(sorted(distances.items()))
print(ordered_distances)