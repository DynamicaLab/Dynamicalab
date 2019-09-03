import numpy as np
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


def merge_duplicated_nodes(G, based_on="name", get_node_attr_fct=None, relabel=False):
	"""Merge duplicated nodes based on either a key attribute (`based_on`)
	on using a certain function to extract the node key.

	**Parameters**

	G : nx.Graph
		Networkx graph

	based_on : String
		If not None, will be used to extract node identity as `node["attr_dict"][based_on]`.
		If None, the `get_node_attr_fct` will be used.
	
	get_node_attr_fct : method
		If `based_on` is None, `get_node_attr_fct` is used to extract node identity as `get_node_attr_fct(node)`.

	relabel : bool
		If True, relabel the nodes to be between 0 and the new number of nodes. Else, keep the original relabeling.
	
	**Returns**

	Network graph 

	if `relabel==True`, the mapping will be returned : `G, mapping`

	"""
	if based_on is None:
		if get_node_attr_fct is None:
			raise KeyError("Parameter get_node_attr_fct must be defined.")

		u = np.array([get_node_attr_fct(node) for i,node in G.nodes(data=True)])
	else:
		u = np.array([node["attr_dict"][based_on] for i,node in G.nodes(data=True)])

	for unique_node in np.unique(u):
		v = np.argwhere(np.array(u)==unique_node)
		if len(v)>1:
			for k in range(len(v)-1):
				G = nx.contracted_nodes(G, int(v[0]), int(v[k+1]))
	if relabel:
		mapping = {}
		for i,node in enumerate(G.nodes()):
			mapping[node] = i
		G = nx.relabel_nodes(G, mapping)
		return G, mapping

	return G