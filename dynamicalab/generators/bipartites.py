
from dynamicalab import Dataset


def plants_pollinators_Ramirez1992(save_path="./data"):
	"""Plant pollinators dataset of `Ramirez et al., 1992 <https://www.nceas.ucsb.edu/interactionweb/html/ramirez_1992.html>`_  .
	
	**Reference**
	
	Ramirez, N., and Y. Brito. 1992. Pollination Biology in a Palm Swamp Community in the Venezuelan Central Plains. Botanical Journal of the Linnean Society 110:277-302.

	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.

	"""
	url = "https://www.nceas.ucsb.edu/interactionweb/data/plant_pollinator/text/ram_matr.txt"
	data_type = "bipartite"
	data_name = "ram_matr.txt"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "https://www.nceas.ucsb.edu/interactionweb/html/ramirez_1992.html",
		"description" : 'This study was conducted in the central plains of Guarico State, Venezuela. Field observations were made in the years 1983, 1984 and 1989. This paper characterizes the floral biology and pollination spectrum of the "morichal" community, and tests whether pollination systems and unspecialized pollen transpotation are in accord with the high proportion of self-compatibility found in the "morichal." (The "morichal" is a tropical swamp community dominated by Mauritia flexuosa.)',
		"data description" : 'The authors recorded the identities of flower visitor and plant species and their interactions. Data are presented as a binary interaction matrix, in which cells with a "1" indicate an interaction between a pair of species, and a "0" indicates no interaction.',
		"source" : "Ramirez, N., and Y. Brito. 1992. Pollination Biology in a Palm Swamp Community in the Venezuelan Central Plains. Botanical Journal of the Linnean Society 110:277-302."
	}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data


def plants_pollinators_McCullen1993(save_path="./data"):
	"""Plant pollinators dataset of `McCullen C.K., 1993 <https://www.nceas.ucsb.edu/interactionweb/html/mcmullen_1993.html>`_  .
	
	**Reference**
	
	McCullen, C. K. 1993. Flower-visiting insects of the Galapagos Islands. Pan-Pacific Entomologist 69:95-106.

	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.

	"""
	url = "https://www.nceas.ucsb.edu/interactionweb/data/plant_pollinator/text/mc_mullen.txt"
	data_type = "bipartite"
	data_name = "mc_mullen.txt"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "https://www.nceas.ucsb.edu/interactionweb/html/mcmullen_1993.html",
		"description" : 'This study presents a compilation of records on plant-flower visitor interactions in the Galápagos archipelago found in the literature. Results of a field study conducted on Pinta Island recording the interactions between six plant species and their flower visitors are also reported.',
		"data description" : 'The author recorded the identities of flower visitor and plant species and their interactions. Data are presented as a binary interaction matrix, in which cells with a "1" indicate an interaction between a pair of species, and a "0" indicates no interaction.',
		"source" : "McCullen, C. K. 1993. Flower-visiting insects of the Galapagos Islands. Pan-Pacific Entomologist 69:95-106."
	}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data





