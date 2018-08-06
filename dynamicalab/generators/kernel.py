
import networkx as nx
import numpy as np
import random as rdm


def generalized_PA_model(nu, p, N, directed=False, max_step=1e4):
	"""Generates a network using the generalized preferential attachment model. The process goes as follows:

		1. Initialize the network with two connected nodes.
		2. Choose a birth event with probability ``p``, or a growing event with probability ``1-p``. Then:
			a. If a birth event, choose and place a new node in the network.
			b. If a growth event, choose an existing node proportionnal to its total degree powers ``nu``.
		3. Choose an existing node following 2b.
		4. Connect the node from step 2 with node from step 3.
		5. Repeat steps 2,3,4 until the number ``N`` is reached.

	**Parameters**
	
	nu : float
		Kernel power.
	
	p : float
		Birth probability.

	N : int
		Number of nodes. The estimated steps to reach ``N`` nodes is ``N/p``.

	directed : bool : (default=False)
		Construct a directed network. If true, new edges are connected toward older nodes and the output is a ``nx.Digraph``
	
	max_step : int : (default=1e4)
		Maximum number of events before the algorithm ends. This does not apply if the desired number of nodes is reached.

	**Returns**
	
	nx.Digraph or nx.Graph
		The resulting graph.

	**Raise**

		``ValueError`` 
			Occurs if the birth probability ``p`` is smaller or equal to zero.
	
	**Example**
		
	.. code:: python

		import dynamicalab as dlb

		nu = 1.0
		p = 1.0
		N = 40
		G = dlb.generalized_PA_model(nu, p, N)
	

	.. note:: 
		
		See `Young et al., 2018 <https://arxiv.org/pdf/1803.09191.pdf>`_ for an intensive description of the model.


	
	.. image:: /_static/assets/zoo.png
		:align: center 
	
	
	Example of networks for ``p=1``. Figure inspired of `Young et al., 2018 <https://arxiv.org/pdf/1803.09191.pdf>`_.

		

	"""

	def add_edge(nodeA, nodeB, G, k, directed):
		k[nodeA] += 1
		k[nodeB] += 1
		G.add_edge(nodeA, nodeB)
		if directed: 
			G.add_edge(nodeB, nodeA)


	def choose_existing_node(degrees, nu, tot_k):
		k_ch = rdm.random()*tot_k
		for i, k in enumerate(degrees):
			if k_ch-(k**nu)<=0.0:
				return i
			else:
				k_ch -= (k**nu)



	if p<=0:
		raise ValueError("p must be larger than 0. ")

	degrees = [0]*N
	G = nx.DiGraph() if directed else nx.Graph()

	# Step 1. Initiate the network
	add_edge(0, 1, G, degrees, directed)

	n_nodes = 2
	nodeB, nodeA = 0, 0

	for t in range(int(max_step)):

		tot_k = np.sum([k**nu for k in degrees[:n_nodes]])

		if rdm.random()<p:
			nodeA = n_nodes
			n_nodes += 1
		else:
			nodeA = choose_existing_node(degrees, nu, tot_k)

		nodeB = choose_existing_node(degrees, nu, tot_k)
		add_edge(nodeA, nodeB, G, degrees, directed)

		if (n_nodes>=N):
			return G

	raise RuntimeWarning("Maximum number of steps reached")
	return G














