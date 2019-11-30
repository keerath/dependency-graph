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
    graph = nx.DiGraph()
    graph.add_nodes_from(range(0, 6))
    graph.add_edge(5, 2)
    graph.add_edge(5, 0)
    graph.add_edge(4, 0)
    graph.add_edge(4, 1)
    graph.add_edge(2, 3)
    graph.add_edge(3, 1)
    par_nodes = find_parallelizable_nodes(graph)
    print(par_nodes)
