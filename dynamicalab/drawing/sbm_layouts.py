import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


def sample_from_circle(n, centroid=(0,0), radius=1):
    theta = np.random.random(n)*360
    r = np.sqrt(np.random.random(n)*radius)
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    return x+centroid[0], y+centroid[1]
    

def sample_nodes_from_centers(node_subsets, centroids, radius_scale=None):
    assert len(node_subsets) == len(centroids)
    if radius_scale==None:
        radius_scale = [1]*len(node_subsets)

    pos = {}
    for i,subset in enumerate(node_subsets):
        x, y = sample_from_circle(len(subset), centroid=centroids[i], radius=len(subset)*radius_scale[i])
        for j,node in enumerate(subset):
            pos[node] = np.array([x[j], y[j]])
    return pos

def split_edges(G, node_subsets):
    H = G.copy()
    edge_bunchs = []
    for i, nodes_a in enumerate(node_subsets):
        nodes = np.unique(list(nodes_a))
        sub = H.subgraph(nodes).copy()
        edge_bunchs.append(sub.edges())
        H.remove_edges_from(sub.edges())
        
    for i, nodes_a in enumerate(node_subsets):
        for j, nodes_b in enumerate(node_subsets):
            if i!=j:
                nodes = np.unique(list(nodes_a) + list(nodes_b))
                sub = H.subgraph(nodes).copy()
                edge_bunchs.append(sub.edges())
                H.remove_edges_from(sub.edges())
                
    return reversed(edge_bunchs)


def clustered_layout(G, groups, centroids, radius_scale=None):
    """This function constructs a layout where nodes are sampled in circles around centroids of groups.

    **Parameters**

    G : Networkx Graph
        A Networkx ``Graph`` or ``DiGraph``.

    groups : list of lists
        A list of groups of nodes. Each element of groups must be a list of ``node_id``.

    centroids : list of lists
        Position of the centers of the groups

    radius_scale : list of float : (default=None)
        Scaling of the radius for each group. If None, then the scaling is equal to 1 for all groups. Smaller scaling increases the nodes density.

    **Returns**

    dict 
        Dictionary of positions that can be use directly with ``draw_networks``. Each key is a ``node_id`` (from ``groups``) and the value is a position ``[x,y]``. 

    list of edges
        Split of edges between each group. Makes the plot much simpler. Check the example.

    **Raise**
    
    ``ValueError``
        Occurs if ``groups`` does not contain all nodes (low criterion).

    **Example**
    
    .. code:: python

        import numpy as np
        import matplotlib.pyplot as plt
        import networkx as nx
        import dynamicalab.drawing as draw

        # Generate a network
        pin = [0.05, 0.2]
        pout= 0.003
        sizes = [100,250]
        G = nx.random_partition_graph(sizes, 0.25, 0.01)

        node_subsets = [range(0,sizes[0]), range(sizes[0], sizes[0]+sizes[1])]
        centroids = [(0,0), (4,4)]
        radius_scale = [0.02,0.03]

        # Get layout
        pos, edge_bunchs = draw.clustered_layout(G, node_subsets, centroids, radius_scale)

        # Draw
        plt.figure(figsize=(10,10))

        node_colors = ['#b2182b', '#2166ac']
        for i, nodes in enumerate(node_subsets):
            nx.draw_networkx_nodes(G, pos=pos, node_size=30, nodelist=nodes, node_color=node_colors[i])

        colors = ['#bdbdbd', '#bdbdbd', '#67a9cf', '#ef8a62']
        for i, edges in enumerate(edge_bunchs):
            nx.draw_networkx_edges(G, pos=pos, alpha=0.2, edgelist=edges, edge_color=colors[i])
            
        plt.axis("off")


    .. image:: /_static/assets/cluster_layout.png
            :align: center

    
    """
    N = G.number_of_nodes()
    if (N!=np.sum([len(u) for u in groups])):
        raise ValueError("All nodes must be grouped in list in groups.")
        return

    pos = sample_nodes_from_centers(groups, centroids, radius_scale)
    edges = split_edges(G, groups)

    return pos, edges