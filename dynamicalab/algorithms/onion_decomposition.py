import networkx as nx
import numpy as np

def onion_decomposition(graph):
    """This function extracts the onion decomposition and the k-core decomposition of a simple undirected graph. 
      

      **Parameters**
      
    
      graph : nx.Graph
          The simple undirected graph without self-loops.
      

      **Retuns**


      onion : dict
          Dictionary mapping the vertices (identified by their name) to their layer in the onion decomposition.

      kcore : dict
          Dictionary mapping the vertices (identified by their name) to the maximal k-core to which they belong.


      **References**
      .. [1] L. Hébert-Dufresne, J. A. Grochow, and A. Allard
         Multi-scale structure and topological anomaly detection via a new network statistic: The onion decomposition
         [Scientific Reports 6, 31708 (2016)](http://dx.doi.org/10.1038/srep31708)

      
      **Example**
      

      .. code:: python

        import networkx as nx
        import dynamicalab.algorithms as algo

        G = nx.florentine_families_graph()
        onion, kcore = algo.onion_decomposition()
        

    """
    # Creates a copy of the graph (to be able to remove vertices and edges) and .
    _the_graph = nx.Graph(graph).to_undirected()
    _the_graph.remove_edges_from( _the_graph.selfloop_edges() )
    # Dictionaries to register the k-core/onion decompositions. 
    _coreness_map = {}
    _layer_map = {}
    # Performs the onion decomposition.
    _current_core = 1
    _current_layer = 1
    while _the_graph.number_of_nodes() > 0:
        # Sets properly the current core.
        _current_degree_list = list(_the_graph.degree().values())
        if (len(_current_degree_list) > 0) and (np.min(_current_degree_list) >= (_current_core+1)):
            _current_core  = np.min(_current_degree_list)
        # Identifies vertices in the current layer.
        _this_layer_ = []
        for v in _the_graph.nodes():
            if _the_graph.degree()[v] <= _current_core:
                _this_layer_.append(v)
        # Identifies the core/layer of the vertices in the current layer.
        for v in _this_layer_:
            _coreness_map[v] = _current_core
            _layer_map[v] = _current_layer
            _the_graph.remove_node(v)
        # Updates the layer count.
        _current_layer = _current_layer + 1
    # Returns the dictionaries containing the k-shell and onion layer of each vertices.
    return (_layer_map, _coreness_map)