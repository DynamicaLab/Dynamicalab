from dynamicalab import Dataset

def connectomes(save_path):
	"""Iterator through all connectomes datasets.
	
	**Parameter**

	save_path : String
		Directory to which the data will be saved.
	
	**Example**

	.. code:: python

		for data in dlb.connectomes("./da"):
			G = data.graph()

	.. note:: 

		It loads all methods of ``Dynamicalab`` for which the name contains ``connectomes_``. 
		Therefore, the name convention must be enforced.

	"""
	import dynamicalab as dlb
	index = 0
	methods = dir(dlb)
	pp_methods = [getattr(dlb,method) for method in methods if ("connectomes_" in method)]
	datasets = [method(save_path) for method in pp_methods]

	while index < len(datasets):
		yield datasets[index]
		index += 1


def connectomes_CElegansSNAP(save_path="./data"):    
	"""This is a neural network of neurons and synapses in C. elegans, a type of worm. This dataset also includes two-dimensional spatial positions of the rostral ganglia neurons, by `SNAP <https://snap.stanford.edu/data/C-elegans-frontal.html>`_ .
	
	**Reference**
	
	Marcus Kaiser and Claus C. Hilgetag. "Nonoptimal component placement, but short processing paths, due to long-distance projections in neural systems." PLoS Comput Biol 2.7 (2006): e95.
	
	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	
	"""
	url = "https://snap.stanford.edu/data/C-elegans-frontal.txt.gz"
	data_type = "edgelist"
	data_name = "C-elegans-frontal.txt.gz"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "http://www-personal.umich.edu/~mejn/netdata/",
		"description" : "This is a neural network of neurons and synapses in C. elegans, a type of worm. This dataset also includes two-dimensional spatial positions of the rostral ganglia neurons.",
		"source" : 'Marcus Kaiser and Claus C. Hilgetag. "Nonoptimal component placement, but short processing paths, due to long-distance projections in neural systems." PLoS Comput Biol 2.7 (2006): e95.'	
		}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data

def connectomes_CElegans1986(save_path="./data"):    
	"""Neural network of the nematode C. Elegans by `White et al. <https://www.nceas.ucsb.edu/interactionweb/html/arroyo_1982.html>`_ .
	
	**Reference**
	
	J. G. White, E. Southgate, J. N. Thompson, and S. Brenner, "The structure of the nervous system of the nematode C. Elegans", Phil. Trans. R. Soc. London 314, 1-340 (1986).
	
	D. J. Watts and S. H. Strogatz, "Collective dynamics of `small-world' networks", Nature 393, 440-442 (1998).

	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	
	.. warning::

		It doesn't work yet because data are contain multiedges.


	"""
	url = "http://www-personal.umich.edu/~mejn/netdata/celegansneural.zip"
	data_type = "gml"
	data_name = "celegansneural.gml"
	compress_type = "ZIP"
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "http://www-personal.umich.edu/~mejn/netdata/",
		"description" : 'This study took place at three different altitudinal levels in the Andean (alpine) zone on the Cordon del Crepo in central Chile. This paper reports the results of a community-oriented study on pollination mechanisms in the high temperate Andes and discusses how pollination mechanisms vary with altitude.',
		"data description" : "The file celegansneural.gml describes a weighted, directed network representing the neural network of C. Elegans.  The data were taken from the web site of Prof. Duncan Watts at Columbia University, http://cdg.columbia.edu/cdg/datasets.  The nodes in the original data were not consecutively numbered, so they have been renumbered to be consecutive. The original node numbers from Watts' data file are retained as the labels of the nodes.  Edge weights are the weights given by Watts. ",
		"source" : 'J. G. White, E. Southgate, J. N. Thompson, and S. Brenner, "The structure of the nervous system of the nematode C. Elegans", Phil. Trans. R. Soc. London 314, 1-340 (1986).\n\nD. J. Watts and S. H. Strogatz, \"Collective dynamics of small-world networks\", Nature 393, 440-442 (1998).'	
		}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data



  
