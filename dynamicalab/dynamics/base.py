import os
import numpy as np
import abc

class BaseDynamics(metaclass=abc.ABCMeta):
    """
    Base class for all dynamics processes. All dynamics have
    the ``__call__`` method implemented.

    **Example**

    .. code:: python

            import networkx as nx
            import dynamicalab.drawing as draw
            import matplotlib.pyplot as plt
            
            G = nx.erdos_renyi_graph(20,0.1)
            T = np.arange(0,100)
            dynamics = Dynamics()
            X = dynamics(G, T)
    
    ``X`` is a numpy array of shape ``(len(T), N)``.
    """
    def __init__(self):
        return

    @abc.abstractmethod
    def __call__(self, G, T, x0=None):
        """Generates a sequence of states for each time
    
        **Params**

        G : nx.Graph
            Graph structure 

        T : list
            List of times. 

        x0 : np.array(N) : (default=None)
            Initial state of each node. The node index should match the 
            node index in `x0`. If `x0==None`, the initial state is build
            using `self.best_x0` method.
 
        **Returns**

        ``np.array(len(T), N)`` : Numpy array of activities

        """
        return

    def best_x0(self, G):
        N = G.number_of_nodes()
        return np.random.random(N)
