
from dynamicalab import Dataset


def plants_pollinators(save_path):
	"""Iterator through all plants pollinators datasets.
	
	**Parameter**

	save_path : String
		Directory to which the data will be saved.
	
	**Example**

	.. code:: python

		for method_name, data in dlb.plants_pollinators("./da"):
			G = data.graph()

	.. note:: 

		It loads all methods of ``Dynamicalab`` for which the name contains ``plants_pollinators_``. 
		Therefore, the name convention must be enforced.

	"""
	import dynamicalab as dlb
	index = 0
	methods = dir(dlb)
	pp_methods = [getattr(dlb,method) for method in methods if ("plants_pollinators_" in method)]
	names = [method.__name__ for method in pp_methods]
	datasets = [method(save_path) for method in pp_methods]

	while index < len(datasets):
		yield names[index], datasets[index]
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



def plants_pollinators_Petanidou1991(save_path="./data"):    
	"""Plant pollinators dataset of `Petanidou 1991 <http://thesis.ekt.gr/thesisBookReader/id/10184#page/1/mode/2up>`_ .
	
	- Nodes: **797** (131 plants, 666 pollinators)
	- Edges: **2933**
	- Bipartite: **True**
	- Components: **2**


	**Reference**
	
	Petanidou, T. (1991). Pollination ecology in a phryganic ecosystem. Unp. PhD. Thesis, Aristotelian University, Thessaloniki.

	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	
	"""
	url = "http://www.web-of-life.es/networkjson.php?id=M_PL_015"
	data_type = "weboflife_json"
	data_name = "networkjson.php?id=M_PL_015"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "http://www.web-of-life.es/map.php?type=5",
		"source" : 'Petanidou, T. (1991). Pollination ecology in a phryganic ecosystem. Unp. PhD. Thesis, Aristotelian University, Thessaloniki.'
	}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data



def plants_pollinators_Clements1923(save_path="./data"):    
	"""Plant pollinators dataset of `Clements 1923 <http://ia802604.us.archive.org/21/items/experimentalpoll00clem/experimentalpoll00clem.pdf>`_ .
	
	- Nodes: **371** (96 plants, 275 pollinators)
	- Edges: **923**
	- Bipartite: **True**
	- Components: **6**


	**Reference**
	
	Clements, R. E., and F. L. Long. 1923, Experimental pollination. An outline of the ecology of flowers and insects. Washington, D.C., USA, Carnegie Institute of Washington.

	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	
	.. image:: /_static/assets/dataset/clements1923.png 
		:align: center


	"""
	url = "http://www.web-of-life.es/networkjson.php?id=M_PL_005"
	data_type = "weboflife_json"
	data_name = "networkjson.php?id=M_PL_005"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "http://www.web-of-life.es/map.php?type=5",
		"source" : 'Clements, R. E., and F. L. Long. 1923, Experimental pollination. An outline of the ecology of flowers and insects. Washington, D.C., USA, Carnegie Institute of Washington.'
	}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data


def plants_pollinators_Dicks2002I(save_path="./data"):    
	"""Plant pollinators dataset of `Dicks 2002 <https://besjournals.onlinelibrary.wiley.com/doi/pdf/10.1046/j.0021-8790.2001.00572.x>`_ .
	
	- Nodes: **78** (17 plants, 61 pollinators)
	- Edges: **146**
	- Bipartite: **True**
	- Components: **1**


	**Reference**
	
	Dicks, LV, Corbet, SA and Pywell, RF 2002. Compartmentalization in plant–insect flower visitor webs. J. Anim. Ecol. 71: 32–43.

	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	
	.. image:: /_static/assets/dataset/dicks2002I.png 
		:align: center


	"""
	url = "http://www.web-of-life.es/networkjson.php?id=M_PL_006"
	data_type = "weboflife_json"
	data_name = "networkjson.php?id=M_PL_006"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "http://www.web-of-life.es/map.php?type=5",
		"source" : 'Dicks, LV, Corbet, SA and Pywell, RF 2002. Compartmentalization in plant–insect flower visitor webs. J. Anim. Ecol. 71: 32–43.'
	}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data

def plants_pollinators_Dicks2002II(save_path="./data"):    
	"""Plant pollinators dataset of `Dicks 2002 <https://besjournals.onlinelibrary.wiley.com/doi/pdf/10.1046/j.0021-8790.2001.00572.x>`_ .
	
	- Nodes: **52** (16 plants, 36 pollinators)
	- Edges: **85**
	- Bipartite: **True**
	- Components: **2**


	**Reference**
	
	Dicks, LV, Corbet, SA and Pywell, RF 2002. Compartmentalization in plant–insect flower visitor webs. J. Anim. Ecol. 71: 32–43.

	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	
	.. image:: /_static/assets/dataset/dicks2002II.png 
		:align: center


	"""
	url = "http://www.web-of-life.es/networkjson.php?id=M_PL_007"
	data_type = "weboflife_json"
	data_name = "networkjson.php?id=M_PL_007"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "http://www.web-of-life.es/map.php?type=5",
		"source" : 'Dicks, LV, Corbet, SA and Pywell, RF 2002. Compartmentalization in plant–insect flower visitor webs. J. Anim. Ecol. 71: 32–43.'
	}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data

def plants_pollinators_Dupont2003(save_path="./data"):    
	"""Plant pollinators dataset of `Dupont 2003 <https://www.jstor.org/stable/3683371>`_ .
	
	- Nodes: **49** (11 plants, 38 pollinators)
	- Edges: **106**
	- Bipartite: **True**
	- Components: **1**


	**Reference**
	
	Dupont YL, Hansen DM and Olesen JM (2003) Structure of a plant-flower-visitor network in the high-altitude sub-alpine desert of Tenerife, Canary Islands. Ecography 26:301-310.

	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	
	.. image:: /_static/assets/dataset/dupont2003.png 
		:align: center


	"""
	url = "http://www.web-of-life.es/networkjson.php?id=M_PL_008"
	data_type = "weboflife_json"
	data_name = "networkjson.php?id=M_PL_008"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "http://www.web-of-life.es/map.php?type=5",
		"source" : 'Dupont YL, Hansen DM and Olesen JM (2003) Structure of a plant-flower-visitor network in the high-altitude sub-alpine desert of Tenerife, Canary Islands. Ecography 26:301-310.'
	}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data


def plants_pollinators_Elberling1999I(save_path="./data"):    
	"""Plant pollinators dataset of `Elberling 1999 <https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1600-0587.1999.tb00507.x>`_ .
	
	- Nodes: **142** (24 plants, 118 pollinators)
	- Edges: **242**
	- Bipartite: **True**
	- Components: **1**


	**Reference**
	
	Elberling, H. & Olesen, J. M. 1999. The structure of a high latitude plant-pollinator system: The dominance of flies. Ecography 22:314-323.

	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	
	.. image:: /_static/assets/dataset/elberling1999I.png 
		:align: center


	"""
	url = "http://www.web-of-life.es/networkjson.php?id=M_PL_009"
	data_type = "weboflife_json"
	data_name = "networkjson.php?id=M_PL_009"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "http://www.web-of-life.es/map.php?type=5",
		"source" : 'Elberling, H. & Olesen, J. M. 1999. The structure of a high latitude plant-pollinator system: The dominance of flies. Ecography 22:314-323.'
	}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data


def plants_pollinators_Elberling1999II(save_path="./data"):    
	"""Plant pollinators dataset of `Elberling 1999 <https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1600-0587.1999.tb00507.x>`_ .
	
	- Nodes: **107** (31 plants, 76 pollinators)
	- Edges: **456**
	- Bipartite: **True**
	- Components: **1**


	**Reference**
	
	Unpublished. Found on Web of life.

	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	
	.. image:: /_static/assets/dataset/elberling1999II.png 
		:align: center


	"""
	url = "http://www.web-of-life.es/networkjson.php?id=M_PL_010"
	data_type = "weboflife_json"
	data_name = "networkjson.php?id=M_PL_010"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "http://www.web-of-life.es/map.php?type=5",
		"source" : 'Unpublished'
	}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data


def plants_pollinators_Olesen2002I(save_path="./data"):    
	"""Plant pollinators dataset of `Olesen 2002 <https://esajournals.onlinelibrary.wiley.com/doi/abs/10.1046/j.1472-4642.2002.00148.x>`_ .
	
	- Nodes: **27** (14 plants, 13 pollinators)
	- Edges: **52**
	- Bipartite: **True**
	- Components: **1**


	**Reference**
	
	Olesen, J.M., Eskildsen, L.I. & Venkatasamy, S. (2002). Div. Distr., 8:181-192.

	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	
	.. image:: /_static/assets/dataset/olesen2002.png 
		:align: center


	"""
	url = "http://www.web-of-life.es/networkjson.php?id=M_PL_011"
	data_type = "weboflife_json"
	data_name = "networkjson.php?id=M_PL_011"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "http://www.web-of-life.es/map.php?type=5",
		"source" : 'Olesen, J.M., Eskildsen, L.I. & Venkatasamy, S. (2002). Div. Distr., 8:181-192.',
		"abstract": "The structure of pollination networks is described for two oceanic islands, the Azorean Flores and the Mauritian Ile aux Aigrettes. At each island site, all interactions between endemic, non‐endemic native and introduced plants and pollinators were mapped. Linkage level, i.e. number of species interactions per species, was significantly higher for endemic species than for non‐endemic native and introduced species. Linkage levels of the two latter categories were similar. Nine types of interaction may be recognized among endemic, non‐endemic native and introduced plants and pollinators. Similar types had similar frequencies in the two networks. Specifically, we looked for the presence of ‘invader complexes’ of mutualists, defined as groups of introduced species interacting more with each other than expected by chance and thus facilitating each other’s establishment. On both islands, observed frequencies of interactions between native (endemic and non‐endemic) and introduced pollinators and plants differed from random. Introduced pollinators and plants interacted less than expected by chance. Thus, the data did not support the existence of invader complexes. Instead, our study suggested that endemic super‐generalist species, i.e. pollinators or plant species with a very wide pollination niche, include new invaders in their set of food plants or pollinators and thereby improve establishment success of the invaders. Reviewing other studies, super generalists seem to be a widespread island phenomenon, i.e. island pollination networks include one or a few species with a very high generalization level compared to co‐occurring species. Low density of island species may lead to low interspecific competition, high abundance and ultimately wide niches and super generalization."
	}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data

def plants_pollinators_Olerton2003(save_path="./data"):    
	"""Plant pollinators dataset of  `Ollerton 2003 <https://academic.oup.com/aob/article-pdf/92/6/807/392524/mcg206.pdf>`_ .

	- Nodes: **65** (9 plants, 56 pollinators)
	- Edges: **103**
	- Bipartite: **True**
	- Components: **1**


	**Reference**
	
	Ollerton, J., S. D. Johnson, L. Cranmer, and S. Kellie. 2003. The pollination ecology of an assemblage of grassland asclepiads in South Africa. Annals of Botany 92:807-834.

	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	
	.. image:: /_static/assets/dataset/olerton2003.png 
		:align: center


	"""
	url = "http://www.web-of-life.es/networkjson.php?id=M_PL_013"
	data_type = "weboflife_json"
	data_name = "networkjson.php?id=M_PL_013"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "http://www.web-of-life.es/map.php?type=5",
		"source" : 'Ollerton, J., S. D. Johnson, L. Cranmer, and S. Kellie. 2003. The pollination ecology of an assemblage of grassland asclepiads in South Africa. Annals of Botany 92:807-834.',
		"abstract": "The KwaZulu-Natal region of South Africa hosts a large diversity of asclepiads (Apocynaceae: Asclepiadoideae), many of which are endemic to the area. The asclepiads are of particular interest because of their characteristically highly evolved  ̄oral morphology. During 3 months of ®eldwork (November 2000 to January 2001) the  ̄ower visitors and pollinators to an assemblage of nine asclepiads at an upland grassland site were studied. These observations were augmented by laboratory studies of  ̄ower morphology (including scan- ning electron microscopy) and  ̄ower colour (using a spectrometer). Two of the specialized pollination systems that were documented are new to the asclepiads: fruit chafer pollination and pompilid wasp pollination. The lat- ter is almost unique in the angiosperms. Taxa possessing these speci®c pollination systems cluster together in multidimensional phenotype space, suggesting that there has been convergent evolution in response to similar selection to attract identical pollinators. Pollination niche breadth varied from the very specialized species, with only one pollinator, to the more generalized, with up to ten pollinators. Pollinator sharing by the specialized taxa does not appear to have resulted in niche differentiation in terms of the temporal or spatial dimensions, or with regards to placement of pollinaria. Nestedness analysis of the data set showed that there was predictability and structure to the pattern of plant-pollinator interactions, with generalist insects visiting specialized plants and vice versa. The research has shown that there is still much to be learned about plant-pollinator interactions in areas of high plant diversity such as South Africa."
	}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data

def plants_pollinators_Hocking1968(save_path="./data"):    
	"""Plant pollinators dataset of  `Hocking 1968 <https://www.jstor.org/stable/3565022>`_ .

	- Nodes: **110** (29 plants, 81 pollinators)
	- Edges: **179**
	- Bipartite: **True**
	- Components: **2**


	**Reference**
	
	Hocking, B. 1968. Insect-flower associations in the high Arctic with special reference to nectar. Oikos 19:359-388.

	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	
	.. image:: /_static/assets/dataset/hocking1968.png 
		:align: center


	"""
	url = "http://www.web-of-life.es/networkjson.php?id=M_PL_014"
	data_type = "weboflife_json"
	data_name = "networkjson.php?id=M_PL_014"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "http://www.web-of-life.es/map.php?type=5",
		"source" : 'Hocking, B. 1968. Insect-flower associations in the high Arctic with special reference to nectar. Oikos 19:359-388.',
		"abstract": "665 measurements of nectar concentration and 983 of nectar volume per day, distributed among 37 out of 43 species of flowering plants examined, are recorded and analysed. Nectar production per unit area per season was substantially less at Lake Hazen, 82° N, than at Churchill, 58°N. Nectar yield in mg sugar/flower/day was higher at Lake Hazen than at Churchill in eight of the ten species for which data were obtained at both localities. There is competition between flowers for pollinators rather than among pollinators for nectar. Heliotropic flowers, notably Dryas and Papaver, focus sunlight falling on them in the region of the germ cells; it is shown that the thermal increments obtainable by black insects resting in these flowers can be important. 184 different plant species - insect species associations are reported, based on about 350 observations and 760 insect specimens; these associations fall into 9 activity categories (some into more than one), as follows: ambush (6), basking (4), flying over (20), hidden in (20), courtship behaviour (1), nectar feeding (23), ovipositing (2), pollen feeding or collecting (12), resting on or uncertain (96). It is concluded that flowers and floral groups are important as aggregation centres for insect populations in this environment. "
	}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data

def plants_pollinators_Herrera1988(save_path="./data"):    
	"""Plant pollinators dataset of  `Herrara 1988 <https://www.jstor.org/stable/2260469>`_ .

	- Nodes: **205** (26 plants, 179 pollinators)
	- Edges: **412**
	- Bipartite: **True**
	- Components: **1**


	**Reference**
	
	Herrera, J. (1988) Pollination relatioships in southern spanish mediterranean shrublands. Journal of Ecology 76: 274-287.

	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	
	.. image:: /_static/assets/dataset/herrera1988.png 
		:align: center


	"""
	url = "http://www.web-of-life.es/networkjson.php?id=M_PL_016"
	data_type = "weboflife_json"
	data_name = "networkjson.php?id=M_PL_016"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "http://www.web-of-life.es/map.php?type=5",
		"source" : 'Herrera, J. (1988) Pollination relatioships in southern spanish mediterranean shrublands. Journal of Ecology 76: 274-287.',
		"abstract": "(1) Pollination relationships were investigated for fourteen months in a southern Spanish Mediterranean coastal scrub community, composed of thirty plant species, at Reserva Biologica de Donana, Donana National Park. (2) Flowering encompassed the whole year, as did insect visits to flowers. Distinct seasonal changes, however, in both the number and identity of insect taxa, and in the number of plant species in bloom were apparent: maximum plant and insect richness occurred in spring. (3) Insect visitors mainly included small beetles, honeybees, small halictid bees, syrphids and bombylids. The overall species richness of the pollinator array was very high (187 taxa). (4) Plant species with specialized pollination mechanisms were relatively infrequent. Most plants had non-restrictive or small flowers, or both. Species relying on pollen to attract pollinators outweighed those relying on nectar as the main reward. (5) Joint analysis of flower attributes, blooming phenology and pollination vectors demonstrated that species flowering at about the same time of year tend to have their flowers visited by the same insects, irrespective of floral features. (6) It is hypothesized that fruit set is more resource- than pollen-limited and that to achieve maximum fruit set most plants have unspecialized pollination relationships. The generalized nature of pollination systems may have been a major factor contributing to the survival and weedy behaviour of many Mediterranean scrub species."
	}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data


def plants_pollinators_Memmott1999(save_path="./data"):    
	"""Plant pollinators dataset of  `Memmott 1999 <https://onlinelibrary.wiley.com/doi/pdf/10.1046/j.1461-0248.1999.00087.x>`_ .

	- Nodes: **104** (23 plants, 79 pollinators)
	- Edges: **299**
	- Bipartite: **True**
	- Components: **1**


	**Reference**
	
	Memmott J. 1999. The structure of a plant-pollinator food web. Ecology Letters 2:276-280.

	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	
	.. image:: /_static/assets/dataset/memmott1999.png 
		:align: center


	"""
	url = "http://www.web-of-life.es/networkjson.php?id=M_PL_017"
	data_type = "weboflife_json"
	data_name = "networkjson.php?id=M_PL_017"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "http://www.web-of-life.es/map.php?type=5",
		"source" : 'Memmott J. 1999. The structure of a plant-pollinator food web. Ecology Letters 2:276-280.',
		"abstract": "The pollination biology literature is dominated by examples of specialization between plants and their pollinators. However, a recent review shows that it is generalization that prevails in the field, with most plants having a number of pollinators and most pollinators visiting a number of plants. Consequently, the vast majority of plant–pollinator interactions are embedded in a complex web of plant–pollinator interactions. These plant‐pollinator webs can be studied in the manner of conventional food webs and the aim of this paper is to illustrate how contemporary methods of web construction and analysis can be applied to plant‐pollinator communities."
	}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data



def plants_pollinators_OlesenUnpublished(save_path="./data"):    
	"""Plant pollinators dataset of Olesen Unpublished.

	- Nodes: **144** (39 plants, 105 pollinators)
	- Edges: **383**
	- Bipartite: **True**
	- Components: **1**


	**Reference**
	
	Unpublished

	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	
	.. image:: /_static/assets/dataset/olesenunpublished.png 
		:align: center


	"""
	url = "http://www.web-of-life.es/networkjson.php?id=M_PL_018"
	data_type = "weboflife_json"
	data_name = "networkjson.php?id=M_PL_018"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "http://www.web-of-life.es/map.php?type=5",
		"source" : 'Unpublished'
	}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data

def plants_pollinators_Inouye1988(save_path="./data"):    
	"""Plant pollinators dataset of  `Inouye 1988 <https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1442-9993.1988.tb00968.x>`_ .

	- Nodes: **125** (40 plants, 85 pollinators)
	- Edges: **264**
	- Bipartite: **True**
	- Components: **2**


	**Reference**
	
	Inouye, D. W., and G. H. Pyke. 1988. Pollination biology in the Snowy Mountains of Australia: comparisons with montane Colorado, USA. Australian Journal of Ecology 13:191-210.

	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	
	.. image:: /_static/assets/dataset/inouye1988.png 
		:align: center


	"""
	url = "http://www.web-of-life.es/networkjson.php?id=M_PL_019"
	data_type = "weboflife_json"
	data_name = "networkjson.php?id=M_PL_019"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "http://www.web-of-life.es/map.php?type=5",
		"source" : 'Inouye, D. W., and G. H. Pyke. 1988. Pollination biology in the Snowy Mountains of Australia: comparisons with montane Colorado, USA. Australian Journal of Ecology 13:191-210.',
		"abstract": "Various aspects of the pollination biology of the alpine flora of Kosciusko National Park, NSW, were examined from late December 1983 until the end of March 1984, including flowering phenology, corolla tube lengths, flower colour, ultraviolet reflectance patterns, visitation rates to the flowers and proboscis lengths of the flower‐visiting insects. An average of 5.3 species flowered in each of 13, 2 m×2 m montane plots and 5.6 species in the 13 alpine plots. The maximum number in flower simultaneously averaged 4.1 species in the montane and 3.3 in the alpine plots; flowering peaked in mid‐January, Corolla tube lengths of the flora averaged 1.73 mm. The most common floral colour was white or predominantly white (40 species), followed by yellow (14 species). Only six of the 38 species (16%) examined had some type of reflectance pattern; the remaining species all absobed ultraviolet. Flies appeared to be the major pollinators. The insects collected in the study area comprised 60 species of Diptera, 33 species of Hymenoptera, and several species each of Lepidoptera and Coleoptera. On average, 14.4 percents of flowers watched during 379 observation periods (10 min each) were visited. On average, each plant species was visited by 6.4 species of flies, 2.4 species of bees, wasps or sawflies, one species of butterfly or moth and 0.3 species of beetles. Visitation rates increased over the growing season, and were significantly affected by ambient temperature (positively), light levels (positively) and wind speed (negatively). The maximum proboscis length for the 25 most common species of bees was 2.76 mm, but 18 of 51 species of flies had proboscis lengths longer than this. The mean proboscis length for all 25 species of bees was 1.68 mm, and for 51 species of flies was 2.31 mm. Proboscis lengths for flies were positively correlated with the average corolla length for the plant species they visited. For bees, however, the range in proboscis lengths was relatively small and did not show this pattern. There appear to be significant differences between the plant‐pollinator community of alpine Australia and other alpine areas where bumblebees are common pollinators. These differences include shorter proboscis and corolla tube lengths, and perhaps an increased diversity and significance of flies as pollinators."
	}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data


def plants_pollinators_Kevan1970(save_path="./data"):    
	"""Plant pollinators dataset of  `Kevan 1970 <https://www.nceas.ucsb.edu/interactionweb/html/kevan_1970.html>`_ .

	- Nodes: **111** (20 plants, 91 pollinators)
	- Edges: **190**
	- Bipartite: **True**
	- Components: **2**


	**Reference**
	
	Kevan P. G. 1970. High Arctic insect-flower relations: The interrelationships of arthropods and flowers at Lake Hazen, Ellesmere Island, Northwest Territories, Canada. Ph.D. thesis, University of Alberta, Edmonton, 399 pp.

	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	
	.. image:: /_static/assets/dataset/kevan1970.png 
		:align: center


	"""
	url = "http://www.web-of-life.es/networkjson.php?id=M_PL_020"
	data_type = "weboflife_json"
	data_name = "networkjson.php?id=M_PL_020"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "http://www.web-of-life.es/map.php?type=5",
		"source" : 'Kevan P. G. 1970. High Arctic insect-flower relations: The interrelationships of arthropods and flowers at Lake Hazen, Ellesmere Island, Northwest Territories, Canada. Ph.D. thesis, University of Alberta, Edmonton, 399 pp.'
	}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data


def plants_pollinators_Kato1990(save_path="./data"):    
	"""Plant pollinators dataset of  `Kato 1990 <https://repository.kulib.kyoto-u.ac.jp/dspace/bitstream/2433/156101/1/cbl02704_309.pdf>`_ .

	- Nodes: **768** (91 plants, 677 pollinators)
	- Edges: **1193**
	- Bipartite: **True**
	- Components: **2**


	**Reference**
	
	Kato, M., Kakutani, T., Inoue, T. and Itino, T. (1990). Insect-flower relationship in the primary beech forest of Ashu, Kyoto: An overview of the flowering phenology and the seasonal pattern of insect visits. Contrib. Biol. Lab., Kyoto, Univ., 27, 309-375.

	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	
	.. image:: /_static/assets/dataset/kato1990.png 
		:align: center


	"""
	url = "http://www.web-of-life.es/networkjson.php?id=M_PL_021"
	data_type = "weboflife_json"
	data_name = "networkjson.php?id=M_PL_021"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "http://www.web-of-life.es/map.php?type=5",
		"source" : 'Kato, M., Kakutani, T., Inoue, T. and Itino, T. (1990). Insect-flower relationship in the primary beech forest of Ashu, Kyoto: An overview of the flowering phenology and the seasonal pattern of insect visits. Contrib. Biol. Lab., Kyoto, Univ., 27, 309-375.'
	}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data