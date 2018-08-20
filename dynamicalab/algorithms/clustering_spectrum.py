import networkx as nx
import numpy as np

def clustering_spectrum(g):
    """This function extracts the clustering spectrum of a simple undirected graph. 
      
    **Parameters**
    
    g : nx.Graph
        A simple undirected graph without self-loops.
    
    
    .. warning::

      The graph must be **simple** (no multiedges), **undirected** and **without self-loops**.
    

    **Returns**

    clust_spect : dict
        Dictionary mapping each degree class (integers) to the corresponding average local clustering coefficient (float).


    **Example**
    

    .. code:: python

      import numpy as np
      import networkx as nx
      import matplotlib.pyplot as plt
      import dynamicalab.algorithms as algo

      # Gets a network and extracts its clustering spectrum.
      G = nx.karate_club_graph()
      clust_spect = algo.clustering_spectrum(G)

      # Plots the clustering spectrum.
      fig, ax = plt.subplots()
      plt.bar(clust_spect.keys(), clust_spect.values(), width=0.50, color='g')

      plt.title("Clustering spectrum")
      ax.set_ylabel("Average local clustering")
      ax.set_xlabel("Degree")
      ax.set_ylim(bottom=0, top=1)
      ax.set_xticks(np.arange(max(clust_spect.keys()) + 1))

      plt.show()
    
    .. image:: /_static/assets/clustering_spectrum_example.png
      :align: center

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