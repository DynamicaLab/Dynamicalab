import networkx as nx
import numpy as np

def clustering_spectrum(g):
    """This function extracts the clustering spectrum of a simple undirected graph. 
      

      **Parameters**
      
    
      graph : nx.Graph
          A simple undirected graph without self-loops.
      
      
      .. warning::

        The graph must be **simple** (no multiedges), **undirected** and **without self-loops**.
      

      **Retuns**

      clust_spect : dict
          Dictionary mapping each degree class to the corresponding average local clustering coefficient.


      **Example**
      

      .. code:: python

        import networkx as nx
        import dynamicalab.algorithms as algo

        G = nx.florentine_families_graph()
        onion, kcore = algo.clustering_spectrum(G)
      

    """
    # Gets the degree and the local clustering coefficient of each node.
    deg = g.degree()
    clu = nx.clustering(g)
    # Puts them in a list preserving the order.
    d = [deg[n] for n in g.nodes()]
    c = [clu[n] for n in g.nodes()]
    # Returns a dictionary mapping each degree class to the corresponding average local
    #   clustering coefficient.
    return {k : x / n for x,k,n in zip(
                 np.histogram(d, bins=np.arange(0.5, np.max(d)+1.5, 1), weights=c)[0],
                 np.arange(1, np.max(d)+2, 1),
                 np.histogram(d, bins=np.arange(0.5, np.max(d)+1.5, 1))[0]) if n > 0}