
from dynamicalab import Dataset

def food_webs(save_path):
	"""Iterator through all food webs datasets.
	
	**Parameter**

	save_path : String
		Directory to which the data will be saved.
	
	**Example**

	.. code:: python

		for data in dlb.foodwebs("./data"):
			G = data.graph()

	.. note:: 

		It loads all methods of ``Dynamicalab`` for which the name contains ``foodwebs_``. 
		Therefore, the name convention must be enforced.

	"""
	import dynamicalab as dlb
	index = 0
	methods = dir(dlb)
	pp_methods = [getattr(dlb,method) for method in methods if ("food_webs_" in method)]
	datasets = [method(save_path) for method in pp_methods]

	while index < len(datasets):
		yield datasets[index]
		index += 1



def food_webs_Angelini2005(save_path="./data"):    
	"""Food webs of `Angelini 2005 <https://www.sciencedirect.com/science/article/pii/S0304380004003606>`_ .

	- Nodes: **40** 
	- Edges: **185**
	- Components: **1**


	**Reference**
	
	Angelini, R., Agostinho A. (2005) Food web model of the Upper Paran ́a River Floodplain: description and aggregation effects. Ecological Modelling 181: 109–121

	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	

	"""
	url = "http://www.web-of-life.es/networkjson.php?id=FW_001"
	data_type = "weboflife_foodwebs_json"
	data_name = "networkjson.php?id=FW_001"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "http://www.web-of-life.es/map.php?type=7",
		"source" : 'Angelini, R., Agostinho A. (2005) Food web model of the Upper Paran ́a River Floodplain: description and aggregation effects. Ecological Modelling 181: 109–121'
	}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data


def food_webs_Angelini2011(save_path="./data"):    
	"""Food webs of `Angelini 2011 <https://www.researchgate.net/publication/287728990_Mixed_food_web_control_and_stability_in_a_Cerrado_river_Brazil>`_ .

	- Nodes: **14** 
	- Edges: **38**
	- Components: **1**


	**Reference**
	
	Angelini, R., Aloisio, GR., Carvalho, AR. (2011) Mixed food web control and stability in a Cerrado river (Brazil). Pan-American Journal of Aquatic Sciences 5(3):421-431

	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	

	"""
	url = "http://www.web-of-life.es/networkjson.php?id=FW_002"
	data_type = "weboflife_foodwebs_json"
	data_name = "networkjson.php?id=FW_002"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "http://www.web-of-life.es/map.php?type=7",
		"source" : 'Angelini, R., Aloisio, GR., Carvalho, AR. (2011) Mixed food web control and stability in a Cerrado river (Brazil). Pan-American Journal of Aquatic Sciences 5(3):421-431'
	}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data

def food_webs_Angelini2011b(save_path="./data"):    
	"""Food webs of `Angelini 2011b <http://scientiamarina.revistas.csic.es/index.php/scientiamarina/article/view/1254>`_ .

	- Nodes: **28** 
	- Edges: **127**
	- Directed: **True**
	- Components: **1**
	- Note: **Canibalism has been found in 3 species or groups. Merluccius, Condrichtis, Macrobenthos**
	- Description: **Cell values indicate the relative frequency of prey species in the diet of each predator species.**



	**Reference**
	
	Angelini, R., Velho, VF. (2011) Ecosystem structure and trophic analysis of Angolan fishery landings. Scientia Marina 75(2)

	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	

	"""
	url = "http://www.web-of-life.es/networkjson.php?id=FW_003"
	data_type = "weboflife_foodwebs_json"
	data_name = "networkjson.php?id=FW_003"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "http://www.web-of-life.es/map.php?type=7",
		"source" : 'Angelini, R., Velho, VF. (2011) Ecosystem structure and trophic analysis of Angolan fishery landings. Scientia Marina 75(2)'
	}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data




def food_webs_Angelini2006(save_path="./data"):    
	"""Food webs of `Angelini 2006 <http://www.scielo.br/scielo.php?pid=S1679-62252006000200011&script=sci_abstract>`_ .

	- Nodes: **32** 
	- Edges: **140**
	- Directed: **True**
	- Components: **1**
	- Note: **Canibalism has been found in 4 species or groups. Hoplias malabaricus, Rhaphiodon vulpinus, Group 1, Group 2**
	- Description: **Cell values indicate the relative frequency of prey species in the diet of each predator species.**


	**Reference**
	
	Angelini, R,. Agostinho A,. Carlos LG. (2006) Modeling energy flow in a large Neotropical Reservoir: a tool do evaluate fishing and stability. Neotrop. Ichthyol., 4(2):253-260, 2006

	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	

	"""
	url = "http://www.web-of-life.es/networkjson.php?id=FW_004"
	data_type = "weboflife_foodwebs_json"
	data_name = "networkjson.php?id=FW_004"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "http://www.web-of-life.es/map.php?type=7",
		"source" : 'Angelini, R,. Agostinho A,. Carlos LG. (2006) Modeling energy flow in a large Neotropical Reservoir: a tool do evaluate fishing and stability. Neotrop. Ichthyol., 4(2):253-260, 2006'
	}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data

def food_webs_Torres2013(save_path="./data"):    
	"""Food webs of `Torres 2013 <https://www.sciencedirect.com/science/article/pii/S0304380013002822>`_ .

	- Nodes: **44** 
	- Edges: **413**
	- Directed: **True**
	- Components: **1**
	- Note: **Canibalism has been found in 14 species or groups. Seabirds, Sharks, Demersal piscivores, Adult hake, Juvenile hake, Benthic cephalopods, Benthopelagic cephalopods, Small benthopelagic fishes, Flatfishes, Small demersal fishes, Crabs, Shrimps, Gelatinous zooplankton, Benthic invertebrates C**
	- Description: **Cell values indicate the relative frequency of prey species in the diet of each predator species.**


	**Reference**
	
	Torres MA., Coll M., Heymans JJ., Christensen V,. Sobrino I. (2013) Food-web structure of and fishing impacts on the Gulf of Cadiz ecosystem (South-western Spain). Ecological Modelling 265 (2013) 26–44

	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	

	"""
	url = "http://www.web-of-life.es/networkjson.php?id=FW_005"
	data_type = "weboflife_foodwebs_json"
	data_name = "networkjson.php?id=FW_005"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "http://www.web-of-life.es/map.php?type=7",
		"source" : 'Torres MA., Coll M., Heymans JJ., Christensen V,. Sobrino I. (2013) Food-web structure of and fishing impacts on the Gulf of Cadiz ecosystem (South-western Spain). Ecological Modelling 265 (2013) 26–44'
	}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data


def food_webs_Cruz2007(save_path="./data"):    
	"""Food webs of `Cruz 2007 <https://www.sciencedirect.com/science/article/pii/S0272771406005002>`_ .

	- Nodes: **30** 
	- Edges: **229**
	- Directed: **True**
	- Components: **1**
	- Note: **Canibalism has been found in 10 species or groups. Zooplankton, Polychaetes, Rays, Catfish, Herrings, Mollies, Swimming crabs, Shrimp, Infauna, Gastropods**
	- Description: **Cell values indicate the relative frequency of prey species in the diet of each predator species.**

	**Reference**
	
	Cruz-Escalona, V.H., Arrequin-Sanchez, F., Zetina-Rejon, M. (2007) Analysis of the ecosystem structure of Laguna Alvarado, western Gulf of Mexico, by means of a mass balance model. Estuarine, Coastal and Shelf Science 72 (155-167)

	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	

	"""
	url = "http://www.web-of-life.es/networkjson.php?id=FW_006"
	data_type = "weboflife_foodwebs_json"
	data_name = "networkjson.php?id=FW_006"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "http://www.web-of-life.es/map.php?type=7",
		"source" : 'Cruz-Escalona, V.H., Arrequin-Sanchez, F., Zetina-Rejon, M. (2007) Analysis of the ecosystem structure of Laguna Alvarado, western Gulf of Mexico, by means of a mass balance model. Estuarine, Coastal and Shelf Science 72 (155-167)'
	}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data




def food_webs_Christian1999(save_path="./data"):    
	"""Food webs of `Christian 1999 <https://www.sciencedirect.com/science/article/pii/S0304380099000228>`_ .

	- Nodes: **48** 
	- Edges: **221**
	- Directed: **True**
	- Components: **1**
	- Note: **Canibalism has been found in 3 species or groups. Microfauna, Meiofauna, Microprotozoa**
	- Description: **Cell values indicate the relative frequency of prey species in the diet of each predator species.**

	**Reference**
	
	Christian, RR., Luczkovich JJ. (1999) Organizing and understanding a winter’s seagrass foodweb network through effective trophic levels

	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	

	"""
	url = "http://www.web-of-life.es/networkjson.php?id=FW_007"
	data_type = "weboflife_foodwebs_json"
	data_name = "networkjson.php?id=FW_007"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "http://www.web-of-life.es/map.php?type=7",
		"source" : 'Christian, RR., Luczkovich JJ. (1999) Organizing and understanding a winter’s seagrass foodweb network through effective trophic levels'
	}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data

def food_webs_Bascompte2005(save_path="./data"):    
	"""Food webs of `Bascompte 2005 <http://www.pnas.org/content/102/15/5443>`_ .

	- Nodes: **249** 
	- Edges: **3313**
	- Directed: **True**
	- Components: **1**
	- Note: **Canibalism has been found in 11 species or groups. Crabs, Shrimps, Polychaetes, Gastropods, Squids, Octopuses, Asteroids, Echinoids, Mycteroperca venenosa, Scomberomorus cavalla, Tylosurus acus**
	- Description: **Cell values indicate the relative frequency of prey species in the diet of each predator species.**

	**Reference**
	
	J. Bascompte, C. J. Melián and E. Sala (2005). Interaction strength combinations and the overfishing of a marine food web. Proceedings of the National Academy of Sciences USA, 102: 5443-5447.
	
	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	

	"""
	url = "http://www.web-of-life.es/networkjson.php?id=FW_008"
	data_type = "weboflife_foodwebs_json"
	data_name = "networkjson.php?id=FW_008"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "http://www.web-of-life.es/map.php?type=7",
		"source" : 'J. Bascompte, C. J. Melián and E. Sala (2005). Interaction strength combinations and the overfishing of a marine food web. Proceedings of the National Academy of Sciences USA, 102: 5443-5447.'
	}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data

def food_webs_Angelini2013(save_path="./data"):    
	"""Food webs of `Angelini 2013 <https://www.sciencedirect.com/science/article/pii/S030438001300015X>`_ .

	- Nodes: **40** 
	- Edges: **241**
	- Directed: **True**
	- Components: **1**
	- Description: **Cell values indicate the relative frequency of prey species in the diet of each predator species.**

	**Reference**
	
	Angelini, R., Morais, R., Catella AC., Resende KE., Libralato, S. (2013) Aquatic food webs of the oxbow lakes in the Pantanal: A new site for fisheries guaranteed by alternated control? Ecological Modelling 253 (82– 96)

	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	

	"""
	url = "http://www.web-of-life.es/networkjson.php?id=FW_009"
	data_type = "weboflife_foodwebs_json"
	data_name = "networkjson.php?id=FW_009"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "http://www.web-of-life.es/map.php?type=7",
		"source" : 'Angelini, R., Morais, R., Catella AC., Resende KE., Libralato, S. (2013) Aquatic food webs of the oxbow lakes in the Pantanal: A new site for fisheries guaranteed by alternated control? Ecological Modelling 253 (82– 96)'
	}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data

def food_webs_Angelini2013B(save_path="./data"):    
	"""Food webs of `Angelini 2013B <https://www.sciencedirect.com/science/article/pii/S030438001300015X>`_ .

	- Nodes: **39** 
	- Edges: **248**
	- Directed: **True**
	- Components: **1**
	- Description: **Cell values indicate the relative frequency of prey species in the diet of each predator species.**

	**Reference**
	
	Angelini, R., Morais, R., Catella AC., Resende KE., Libralato, S. (2013) Aquatic food webs of the oxbow lakes in the Pantanal: A new site for fisheries guaranteed by alternated control? Ecological Modelling 253 (82– 96)

	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	

	"""
	url = "http://www.web-of-life.es/networkjson.php?id=FW_010"
	data_type = "weboflife_foodwebs_json"
	data_name = "networkjson.php?id=FW_010"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "http://www.web-of-life.es/map.php?type=7",
		"source" : 'Angelini, R., Morais, R., Catella AC., Resende KE., Libralato, S. (2013) Aquatic food webs of the oxbow lakes in the Pantanal: A new site for fisheries guaranteed by alternated control? Ecological Modelling 253 (82– 96)'
	}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data

def food_webs_Thompson2003(save_path="./data"):    

	
	"""Food webs of `Thompson 2003 <https://esajournals.onlinelibrary.wiley.com/doi/abs/10.1890/0012-9658(2003)084%5B0145:IOSFWO%5D2.0.CO;2>`_ .

	- Nodes: **105** 
	- Edges: **343**
	- Directed: **True**
	- Components: **1**
	- Description: **Cell values indicate the relative frequency of prey species in the diet of each predator species.**

	**Reference**
	
	Thompson, R., Townsend, C. (2003) IMPACTS ON STREAM FOOD WEBS OF NATIVE AND EXOTIC FOREST: AN INTERCONTINENTAL COMPARISON. Ecology, 84(1), pp. 145–161

	**Parameters**

	save_path : String : (default="./data")
		Directory to which the data will be saved.

	**Returns**

	Dataset 
		Object dataset. Use ``dataset.graph()`` to download the graph.
	

	"""
	url = "http://www.web-of-life.es/networkjson.php?id=FW_011"
	data_type = "weboflife_foodwebs_json"
	data_name = "networkjson.php?id=FW_011"
	compress_type = None
	infos = {
		"type" : data_type,
		"download_url" : url,
		"info_url": "http://www.web-of-life.es/map.php?type=7",
		"source" : 'Thompson, R., Townsend, C. (2003) IMPACTS ON STREAM FOOD WEBS OF NATIVE AND EXOTIC FOREST: AN INTERCONTINENTAL COMPARISON. Ecology, 84(1), pp. 145–161'
	}

	data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
	return data

	