import numpy as np
from numpy.random import random
from .base import BaseDynamics

class SISDynamics(BaseDynamics):
    """Markovian discrete time Suceptible-infected-suceptible process on networks. 
    """
    def __init__(self, p, q, self_activation=0):
        """
        **Parameters**

        p : Float
            Probability of infection

        q : Float
            Probability of recovery

        self_activation : Float : (default=0)
            Probability of spontaneous activation
        

        Note that the `__call__(G, T)` method is independent of ``T[i]-T[i+1]``. Only ``len(T)`` is 
        taken into account for the number of steps.
        """
        super(SISDynamics, self).__init__()
        self.p = p
        self.q = q
        self.self_activation = self_activation
        self.infected_node_set = set()

    def __call__(self, G, T, x0=None):
        
        if x0 is None:
            x0 = self.best_x0(G)

        #initialize
        for node in range(len(x0)):
            if x0[node] == 1:
                self.infected_node_set.add(node)
        X = []

        for t in T:
            self.__step(G)
            X.append(self.__get_state(G))
            
        self.infected_node_set = set()
        return np.array(X)

    def best_x0(self, G):
        """Convenient method to get a good initial state given as a random infection.
    
        **Params**

        G : nx.Graph
            Network structure

        **Returns**

        np.array(N): Binary state of each node.
        """
        N = G.number_of_nodes()
        return np.random.randint(0,2, size=(N,))

    def __step(self, G):
        """Realize a time step of the process
        """
        new_infected_node_set = self.infected_node_set.copy()
        #look for new infections
        for node in self.infected_node_set:
            #try to infect neighbors
            for neighbor in G.neighbors(node):
                if random() < self.p:
                    new_infected_node_set.add(neighbor)

        #look for recuperations
        for node in self.infected_node_set:
            #try to recuperate
            if random() < self.q:
                new_infected_node_set.remove(node)
        #set new infected nodes
        self.infected_node_set = new_infected_node_set

    def __get_state(self, G):
        """Returns the current state"""
        x = np.zeros(len(G))
        for node in self.infected_node_set:
            x[node] = 1

        # Random activation
        if self.self_activation>0:
            rdm_act = np.random.choice([0,1], size=len(x), p=[1-self.self_activation, self.self_activation])
            x = np.minimum(x+rdm_act, 1)
        return x




