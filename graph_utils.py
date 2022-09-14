import networkx as nx

def build_graph():
    first_line = input().split()
    num_nodes  = int(first_line[0])
    num_edges  = int(first_line[1])
    
    graph = nx.Graph()

    # Grafo unidirecional con num_nodes
    for i in range (1, num_nodes+1):
        graph.add_node(i)
    
    #Aristas
    for i in range(1, num_edges+1):
        linea = input().split()
        graph.add_edge(int(linea[0]), int(linea[1]))

    return graph
    