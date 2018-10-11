
from dynamicalab import Dataset


def plants_pollinators(save_path):
	"""Iterator through all plants pollinators datasets.
	
	**Parameter**

	save_path : String
		Directory to which the data will be saved.
	
	**Example**

	.. code:: python

		for data in dlb.plants_pollinators("./da"):
			G = data.graph()

	.. note:: 

		It loads all methods of ``Dynamicalab`` for which the name contains ``plants_pollinators_``. 
		Therefore, the name convention must be enforced.

	"""
	import dynamicalab as dlb
	index = 0
	methods = dir(dlb)
	pp_methods = [getattr(dlb,method) for method in methods if ("plants_pollinators_" in method)]
	datasets = [method(save_path) for method in pp_methods]

	while index < len(datasets):
		yield datasets[index]
		index += 1

def plants_pollinators_Ramirez1992(save_path="./data"):
	"""Plant pollinators dataset of `Ramirez et al., 1992 <https://www.nceas.ucsb.edu/interactionweb/html/ramirez_1992.html>`_  .
	
	- Nodes: **81**
	- Edges: **109**
	- Bipartite: **True**
	- Components: **5**

	**Reference**
	
	Ramirez, N., and Y. Brito. 1992. Pollination Biology in a Palm Swamp Community in the Venezuelan Central Plains. Botanical Journal of the Linnean Society 110:277-302.
	
	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	


    .. image:: /_static/assets/dataset/ramirez1992.png 
        :align: center


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
	
	- Nodes: **159**
	- Edges: **204**
	- Bipartite: **True**
	- Components: **4**


	**Reference**
	
	McCullen, C. K. 1993. Flower-visiting insects of the Galapagos Islands. Pan-Pacific Entomologist 69:95-106.

	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	

    .. image:: /_static/assets/dataset/mccullen1993.png 
        :align: center

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

def plants_pollinators_Arroyo1992_I(save_path="./data"):    
	"""Plant pollinators dataset of `Arroyo et al., 1982 <https://www.nceas.ucsb.edu/interactionweb/html/arroyo_1982.html>`_  at elevation I.
	
	- Nodes: **186**
	- Edges: **365**
	- Bipartite: **True**
	- Components: **3**

	**Reference**
	
	Arroyo, M. T. K., R. B. Primack, and J. J. Armesto. 1982. Community studies in pollination ecology in the high temperate Andes of Central Chile. I. Pollination mechanisms and altitudinal variation. American Journal of Botany 69:82-97.

	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	
	.. image:: /_static/assets/dataset/arroyo1992I.png 
		:align: center


	"""
	url = "https://www.nceas.ucsb.edu/interactionweb/data/plant_pollinator/text/arr_1_matr.txt"
	data_type = "bipartite"
	data_name = "arr_1_matr.txt"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "https://www.nceas.ucsb.edu/interactionweb/html/arroyo_1982.html",
		"description" : 'This study took place at three different altitudinal levels in the Andean (alpine) zone on the Cordon del Crepo in central Chile. This paper reports the results of a community-oriented study on pollination mechanisms in the high temperate Andes and discusses how pollination mechanisms vary with altitude.',
		"data description" : 'The authors recorded the identities of insect and plant species and their interactions. Data are presented as a binary interaction matrix, in which cells with a "1" indicate an interaction between a pair of species, and a "0" indicates no interaction. ',
		"source" : 'Arroyo, M. T. K., R. B. Primack, and J. J. Armesto. 1982. Community studies in pollination ecology in the high temperate Andes of Central Chile. I. Pollination mechanisms and altitudinal variation. American Journal of Botany 69:82-97.'	}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data


def plants_pollinators_Arroyo1992_II(save_path="./data"):    
	"""Plant pollinators dataset of `Arroyo et al., 1982 <https://www.nceas.ucsb.edu/interactionweb/html/arroyo_1982.html>`_  at elevation II.
	
	- Nodes: **103**
	- Edges: **183**
	- Bipartite: **True**
	- Components: **3**


	**Reference**
	
	Arroyo, M. T. K., R. B. Primack, and J. J. Armesto. 1982. Community studies in pollination ecology in the high temperate Andes of Central Chile. I. Pollination mechanisms and altitudinal variation. American Journal of Botany 69:82-97.

	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.

	.. image:: /_static/assets/dataset/arroyo1992II.png 
		:align: center

	"""
	url = "https://www.nceas.ucsb.edu/interactionweb/data/plant_pollinator/text/arr_2_matr.txt"
	data_type = "bipartite"
	data_name = "arr_2_matr.txt"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "https://www.nceas.ucsb.edu/interactionweb/html/arroyo_1982.html",
		"description" : 'This study took place at three different altitudinal levels in the Andean (alpine) zone on the Cordon del Crepo in central Chile. This paper reports the results of a community-oriented study on pollination mechanisms in the high temperate Andes and discusses how pollination mechanisms vary with altitude.',
		"data description" : 'The authors recorded the identities of insect and plant species and their interactions. Data are presented as a binary interaction matrix, in which cells with a "1" indicate an interaction between a pair of species, and a "0" indicates no interaction. ',
		"source" : 'Arroyo, M. T. K., R. B. Primack, and J. J. Armesto. 1982. Community studies in pollination ecology in the high temperate Andes of Central Chile. I. Pollination mechanisms and altitudinal variation. American Journal of Botany 69:82-97.'	}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data

def plants_pollinators_Arroyo1992_III(save_path="./data"):    
	"""Plant pollinators dataset of `Arroyo et al., 1982 <https://www.nceas.ucsb.edu/interactionweb/html/arroyo_1982.html>`_  at elevation III.
	
	- Nodes: **69**
	- Edges: **87**
	- Bipartite: **True**
	- Components: **3**


	**Reference**
	
	Arroyo, M. T. K., R. B. Primack, and J. J. Armesto. 1982. Community studies in pollination ecology in the high temperate Andes of Central Chile. I. Pollination mechanisms and altitudinal variation. American Journal of Botany 69:82-97.

	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	
	.. image:: /_static/assets/dataset/arroyo1992III.png 
		:align: center

	"""
	url = "https://www.nceas.ucsb.edu/interactionweb/data/plant_pollinator/text/arr_3_matr.txt"
	data_type = "bipartite"
	data_name = "arr_3_matr.txt"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "https://www.nceas.ucsb.edu/interactionweb/html/arroyo_1982.html",
		"description" : 'This study took place at three different altitudinal levels in the Andean (alpine) zone on the Cordon del Crepo in central Chile. This paper reports the results of a community-oriented study on pollination mechanisms in the high temperate Andes and discusses how pollination mechanisms vary with altitude.',
		"data description" : 'The authors recorded the identities of insect and plant species and their interactions. Data are presented as a binary interaction matrix, in which cells with a "1" indicate an interaction between a pair of species, and a "0" indicates no interaction. ',
		"source" : 'Arroyo, M. T. K., R. B. Primack, and J. J. Armesto. 1982. Community studies in pollination ecology in the high temperate Andes of Central Chile. I. Pollination mechanisms and altitudinal variation. American Journal of Botany 69:82-97.'	}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data

def plants_pollinators_Barrett1987(save_path="./data"):    
	"""Plant pollinators dataset of `Barrett & Helenurm, 1987 <https://www.nceas.ucsb.edu/interactionweb/html/barrett_helenurm_1987.html>`_ .
	
	- Nodes: **114**
	- Edges: **167**
	- Bipartite: **True**
	- Components: **2**


	**Reference**
	
	Barrett, S. C. H., and K. Helenurm. 1987. The Reproductive-Biology of Boreal Forest Herbs.1. Breeding Systems and Pollination. Canadian Journal of Botany 65:2036-2046.
	
	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	
	.. image:: /_static/assets/dataset/barrett1987.png 
		:align: center

	"""
	url = "https://www.nceas.ucsb.edu/interactionweb/data/plant_pollinator/text/barrett_matr_f.txt"
	data_type = "bipartite"
	data_name = "barrett_matr_f.txt"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "https://www.nceas.ucsb.edu/interactionweb/html/barrett_helenurm_1987.htm",
		"description" : 'This study took place in the boreal forest of central New Brunswick, Canada, from May to September of 1978, 1979, and 1980. The objective was to investigate the role of animals in pollination and seed dispersal. The study was designed to provide basic descriptive information on breeding systems, pollination biology, and phenology of understory herbs.',
		"data description" : 'The authors recorded their data by counting the number of individual flower visitors caught on each plant species. The total number of individuals collected on each plant species provide a rough estimate of the level of visitation that each species received. Data are presented as an interaction frequency matrix, in which cells with positive integers indicate the frequency of interaction between a pair of species, and cells with zeros indicate no interaction.',
		"source" : 'Barrett, S. C. H., and K. Helenurm. 1987. The Reproductive-Biology of Boreal Forest Herbs.1. Breeding Systems and Pollination. Canadian Journal of Botany 65:2036-2046.'
	}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data



def plants_pollinators_Robsertson1992(save_path="./data"):    
	"""Plant pollinators dataset of `Robertson 1992 <https://www.nceas.ucsb.edu/interactionweb/html/robertson_1929.html>`_ .
	
	- Nodes: **1500**
	- Edges: **15255**
	- Bipartite: **True**
	- Components: **1**


	**Reference**
	
	Original data: Robertson, C. 1929. Flowers and insects: lists of visitors to four hundred and fifty-three flowers. Carlinville, IL, USA, C. Robertson.

	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	
	"""
	url = "https://www.nceas.ucsb.edu/interactionweb/data/plant_pollinator/text/robertson_1929_matr.txt"
	data_type = "bipartite"
	data_name = "robertson_1929_matr.txt"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "https://www.nceas.ucsb.edu/interactionweb/html/robertson_1929.html",
		"description" : 'The author listed 1429 animal species visiting flowers of 456 plant species that grew in a small area in southwestern Illinois, USA. Marlin and LaBerge (2001) describe Robertson’s methods.',
		"data description" : 'The author recorded the identities of flower visitor and plant species and their interactions. Data are presented as a binary interaction matrix, in which cells with a "1" indicate an interaction between a pair of species, and a "0" indicates no interaction.',
		"source" : 'Original data: Robertson, C. 1929. Flowers and insects: lists of visitors to four hundred and fifty-three flowers. Carlinville, IL, USA, C. Robertson.'
	}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data


def plants_pollinators_Kaiser2010(save_path="./data"):    
	"""Plant pollinators dataset of `Kaiser-Bunbury 2010 <https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1461-0248.2009.01437.x>`_ .
	
	- Nodes: **38**
	- Edges: **46**
	- Bipartite: **True**
	- Components: **2**


	**Reference**
	
	Original data: Kaiser-Bunbury, C. N., S. Muff, J. Memmott, C. B. Müller, and A. Caflisch. 2010. The robustness of pollination networks to the loss of species and interactions: A quantitative approach incorporating pollinator behaviour. Ecology Letters 13:442-452.

	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	
	.. image:: /_static/assets/dataset/kaiser2010.png 
		:align: center

	"""
	url = "http://www.web-of-life.es/networkjson.php?id=M_PL_060_24"
	data_type = "weboflife_json"
	data_name = "networkjson.php?id=M_PL_060_24"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "http://www.web-of-life.es/map.php?type=5",
		"abstract" : 'Species extinctions pose serious threats to the functioning of ecological communities worldwide. We used two qualitative and quantitative pollination networks to simulate extinction patterns following three removal scenarios: random removal and systematic removal of the strongest and weakest interactors. We accounted for pollinator behaviour by including potential links into temporal snapshots (12 consecutive 2‐week networks) to reflect mutualists’ ability to ‘switch’ interaction partners (re‐wiring). Qualitative data suggested a linear or slower than linear secondary extinction while quantitative data showed sigmoidal decline of plant interaction strength upon removal of the strongest interactor. Temporal snapshots indicated greater stability of re‐wired networks over static systems. Tolerance of generalized networks to species extinctions was high in the random removal scenario, with an increase in network stability if species formed new interactions. Anthropogenic disturbance, however, that promote the extinction of the strongest interactors might induce a sudden collapse of pollination networks.',
		"source" : 'Kaiser-Bunbury, C. N., S. Muff, J. Memmott, C. B. Müller, and A. Caflisch. 2010. The robustness of pollination networks to the loss of species and interactions: A quantitative approach incorporating pollinator behaviour. Ecology Letters 13:442-452.'
	}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data





