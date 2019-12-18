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
	data_type = "edgelist_directed"
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