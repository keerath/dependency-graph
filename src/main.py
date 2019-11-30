import networkx as nx


def find_parallelizable_nodes(graph: nx.DiGraph):
    def find_parallelizable_nodes_acc(graph: nx.DiGraph, parallelizable_nodes: list):
        if len(list(graph.nodes)) > 0:
            ## filter nodes with zero indegree i.e. not dependent on anything
            independent_nodes = list(map(lambda node_vs_degree: node_vs_degree[0],
                                         filter(lambda node_vs_degree: node_vs_degree[1] == 0, list(graph.in_degree))))
            ## remove them from graph and add them to parallelizable nodes
            graph.remove_nodes_from(independent_nodes)
            parallelizable_nodes.append(independent_nodes)
            return find_parallelizable_nodes_acc(graph, parallelizable_nodes)
        else:
            return parallelizable_nodes

    return find_parallelizable_nodes_acc(graph, [])


## Look at graph.png for a visual representation of this graph

if __name__ == '__main__':
    ## Look at graph.png for a visual representation of this graph
    graph1 = nx.DiGraph()
    graph1.add_nodes_from(range(0, 6))
    graph1.add_edge(5, 2)
    graph1.add_edge(5, 0)
    graph1.add_edge(4, 0)
    graph1.add_edge(4, 1)
    graph1.add_edge(2, 3)
    graph1.add_edge(3, 1)
    print(find_parallelizable_nodes(graph1))

    ## Look at IMG_1788.jpg for a visual representation of this graph
    graph2 = nx.DiGraph()
    graph2.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'G', 'H'])
    graph2.add_edge('A', 'C')
    graph2.add_edge('A', 'D')
    graph2.add_edge('A', 'E')
    graph2.add_edge('B', 'G')
    graph2.add_edge('B', 'H')
    print(find_parallelizable_nodes(graph2))
