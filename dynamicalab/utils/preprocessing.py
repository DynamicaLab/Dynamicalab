
import networkx as nx

def largest_connected_component(G, relabel=False):
	"""Extract the largest connected component of the graph.
	
		
	**Parameters**

	G : nx.Graph
		Networkx graph

	relabel : bool
		If True, relabel the nodes to be between 0 and the new number of nodes. Else, keep the original relabeling.
	
	**Returns**

	nx.Graph

	"""
	
	#1. Keep largest connected component
	Gc = max(nx.connected_component_subgraphs(G), key=len)
	mapping = {}
	for i,node in enumerate(Gc.nodes()):
		mapping[node] = i
	if relabel:
		Gc=nx.relabel_nodes(Gc,mapping)
	
	return Gc