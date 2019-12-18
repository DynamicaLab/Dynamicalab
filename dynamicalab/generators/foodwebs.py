
from dynamicalab import Dataset

def food_webs(save_path):
	"""Iterator through all food webs datasets.
	
	**Parameter**

	save_path : String
		Directory to which the data will be saved.
	
	**Example**

	.. code:: python

		for data in dlb.food_webs("./data"):
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


def food_webs_Angelini_Agostinho_2005(save_path='./data'):    
    """Food webs of Angelini, R., Agostinho A. .
    
    - Nodes: **40** 
    - Edges: **185**
    - Directed: **True**
    - Components: **1**
    - Note: *Canibalism has been found in 4 species or groups. Hoplias malabaricus, Rhaphiodon vulpinus, Serrasalmus marginatus, Other piscivores*
    - Description: *Cell values indicate the relative frequency of prey species in the diet of each predator species.*

    **Reference**
    
    Angelini, R., Agostinho A. (2005) Food web model of the Upper Paran ́a River Floodplain: description and aggregation effects. Ecological Modelling 181: 109–121
    
    **Parameters**

    save_path : String : (default='./data')
        Directory to which the data will be saved.

    **Returns**

    Dataset 
        Object dataset. Use ``dataset.graph()`` to download the graph.
    
    
    """
    url = 'http://www.web-of-life.es/networkjson.php?id=FW_001'
    data_type = 'weboflife_foodwebs_json'
    data_name = 'networkjson.php?id=FW_001'
    compress_type = None
    infos = {
         'type': data_type,
         'download_url' : url,
        'info_url': 'http://www.web-of-life.es/map.php?type=7',
        'source' :  'Angelini, R., Agostinho A. (2005) Food web model of the Upper Paran ́a River Floodplain: description and aggregation effects. Ecological Modelling 181: 109–121'
    }

    data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
    return data
    

def food_webs_Angelini_et_all_1011(save_path='./data'):    
    """Food webs of Angelini, R., Aloisio, GR., Carvalho, AR. .
    
    - Nodes: **14** 
    - Edges: **38**
    - Directed: **True**
    - Components: **1**
    - Note: *Canibalism has been found in 1 species or groups. Hoplias malabaricus*
    - Description: *Cell values indicate the relative frequency of prey species in the diet of each predator species..*

    **Reference**
    
    Angelini, R., Aloisio, GR., Carvalho, AR. (2011) Mixed food web control and stability in a Cerrado river (Brazil). Pan-American Journal of Aquatic Sciences 5(3):421-431
    
    **Parameters**

    save_path : String : (default='./data')
        Directory to which the data will be saved.

    **Returns**

    Dataset 
        Object dataset. Use ``dataset.graph()`` to download the graph.
    
    
    """
    url = 'http://www.web-of-life.es/networkjson.php?id=FW_002'
    data_type = 'weboflife_foodwebs_json'
    data_name = 'networkjson.php?id=FW_002'
    compress_type = None
    infos = {
         'type': data_type,
         'download_url' : url,
        'info_url': 'http://www.web-of-life.es/map.php?type=7',
        'source' :  'Angelini, R., Aloisio, GR., Carvalho, AR. (2011) Mixed food web control and stability in a Cerrado river (Brazil). Pan-American Journal of Aquatic Sciences 5(3):421-431'
    }

    data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
    return data
    

def food_webs_Angelini_Velho_2011(save_path='./data'):    
    """Food webs of Angelini, R., Velho, VF. .
    
    - Nodes: **28** 
    - Edges: **127**
    - Directed: **True**
    - Components: **1**
    - Note: *Canibalism has been found in 3 species or groups. Merluccius, Condrichtis, Macrobenthos*
    - Description: *Cell values indicate the relative frequency of prey species in the diet of each predator species. .*

    **Reference**
    
    Angelini, R., Velho, VF. (2011) Ecosystem structure and trophic analysis of Angolan fishery landings. Scientia Marina 75(2)
    
    **Parameters**

    save_path : String : (default='./data')
        Directory to which the data will be saved.

    **Returns**

    Dataset 
        Object dataset. Use ``dataset.graph()`` to download the graph.
    
    
    """
    url = 'http://www.web-of-life.es/networkjson.php?id=FW_003'
    data_type = 'weboflife_foodwebs_json'
    data_name = 'networkjson.php?id=FW_003'
    compress_type = None
    infos = {
         'type': data_type,
         'download_url' : url,
        'info_url': 'http://www.web-of-life.es/map.php?type=7',
        'source' :  'Angelini, R., Velho, VF. (2011) Ecosystem structure and trophic analysis of Angolan fishery landings. Scientia Marina 75(2)'
    }

    data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
    return data
    

def food_webs_Angelini_et_all_2006(save_path='./data'):    
    """Food webs of Angelini, R,. Agostinho A,. Carlos LG. .
    
    - Nodes: **32** 
    - Edges: **140**
    - Directed: **True**
    - Components: **1**
    - Note: *Canibalism has been found in 4 species or groups. Hoplias malabaricus, Rhaphiodon vulpinus, Group 1, Group 2*
    - Description: *Cell values indicate the relative frequency of prey species in the diet of each predator species.*

    **Reference**
    
    Angelini, R,. Agostinho A,. Carlos LG. (2006) Modeling energy flow in a large Neotropical Reservoir: a tool do evaluate fishing and stability. Neotrop. Ichthyol., 4(2):253-260, 2006
    
    **Parameters**

    save_path : String : (default='./data')
        Directory to which the data will be saved.

    **Returns**

    Dataset 
        Object dataset. Use ``dataset.graph()`` to download the graph.
    
    
    """
    url = 'http://www.web-of-life.es/networkjson.php?id=FW_004'
    data_type = 'weboflife_foodwebs_json'
    data_name = 'networkjson.php?id=FW_004'
    compress_type = None
    infos = {
         'type': data_type,
         'download_url' : url,
        'info_url': 'http://www.web-of-life.es/map.php?type=7',
        'source' :  'Angelini, R,. Agostinho A,. Carlos LG. (2006) Modeling energy flow in a large Neotropical Reservoir: a tool do evaluate fishing and stability. Neotrop. Ichthyol., 4(2):253-260, 2006'
    }

    data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
    return data
    

def food_webs_Torres_et_all_2013(save_path='./data'):    
    """Food webs of Torres MA., Coll M., Heymans JJ., Christensen V,. Sobrino I. .
    
    - Nodes: **44** 
    - Edges: **413**
    - Directed: **True**
    - Components: **1**
    - Note: *Canibalism has been found in 14 species or groups. Seabirds, Sharks, Demersal piscivores, Adult hake, Juvenile hake, Benthic cephalopods, Benthopelagic cephalopods, Small benthopelagic fishes, Flatfishes, Small demersal fishes, Crabs, Shrimps, Gelatinous zooplankton, Benthic invertebrates C*
    - Description: *Cell values indicate the relative frequency of prey species/group in the diet of each predator species/group.*

    **Reference**
    
    Torres MA., Coll M., Heymans JJ., Christensen V,. Sobrino I. (2013) Food-web structure of and fishing impacts on the Gulf of Cadiz ecosystem (South-western Spain). Ecological Modelling 265 (2013) 26–44
    
    **Parameters**

    save_path : String : (default='./data')
        Directory to which the data will be saved.

    **Returns**

    Dataset 
        Object dataset. Use ``dataset.graph()`` to download the graph.
    
    
    """
    url = 'http://www.web-of-life.es/networkjson.php?id=FW_005'
    data_type = 'weboflife_foodwebs_json'
    data_name = 'networkjson.php?id=FW_005'
    compress_type = None
    infos = {
         'type': data_type,
         'download_url' : url,
        'info_url': 'http://www.web-of-life.es/map.php?type=7',
        'source' :  'Torres MA., Coll M., Heymans JJ., Christensen V,. Sobrino I. (2013) Food-web structure of and fishing impacts on the Gulf of Cadiz ecosystem (South-western Spain). Ecological Modelling 265 (2013) 26–44'
    }

    data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
    return data
    

def food_webs_Escalona_et_all_2007(save_path='./data'):    
    """Food webs of Cruz-Escalona, V.H., Arrequin-Sanchez, F., Zetina-Rejon, M. .
    
    - Nodes: **30** 
    - Edges: **229**
    - Directed: **True**
    - Components: **1**
    - Note: *Canibalism has been found in 10 species or groups. Zooplankton, Polychaetes, Rays, Catfish, Herrings, Mollies, Swimming crabs, Shrimp, Infauna, Gastropods*
    - Description: *Cell values indicate the relative frequency of prey species/group in the diet of each predator species/group.*

    **Reference**
    
    Cruz-Escalona, V.H., Arrequin-Sanchez, F., Zetina-Rejon, M. (2007)  Analysis of the ecosystem structure of Laguna Alvarado, western Gulf of Mexico, by means of a mass balance model. Estuarine, Coastal and Shelf Science 72 (155-167)
    
    **Parameters**

    save_path : String : (default='./data')
        Directory to which the data will be saved.

    **Returns**

    Dataset 
        Object dataset. Use ``dataset.graph()`` to download the graph.
    
    
    """
    url = 'http://www.web-of-life.es/networkjson.php?id=FW_006'
    data_type = 'weboflife_foodwebs_json'
    data_name = 'networkjson.php?id=FW_006'
    compress_type = None
    infos = {
         'type': data_type,
         'download_url' : url,
        'info_url': 'http://www.web-of-life.es/map.php?type=7',
        'source' :  'Cruz-Escalona, V.H., Arrequin-Sanchez, F., Zetina-Rejon, M. (2007)  Analysis of the ecosystem structure of Laguna Alvarado, western Gulf of Mexico, by means of a mass balance model. Estuarine, Coastal and Shelf Science 72 (155-167)'
    }

    data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
    return data
    

def food_webs_Christian_Luczkovich_1999(save_path='./data'):    
    """Food webs of Christian, RR., Luczkovich JJ. .
    
    - Nodes: **48** 
    - Edges: **221**
    - Directed: **True**
    - Components: **1**
    - Note: *Canibalism has been found in 3 species or groups. Microfauna, Meiofauna, Microprotozoa*
    - Description: *Cell values indicate the relative frequency of prey species/group in the diet of each predator species/group.*

    **Reference**
    
    Christian, RR., Luczkovich JJ. (1999) Organizing and understanding a winter’s seagrass foodweb network through effective trophic levels
    
    **Parameters**

    save_path : String : (default='./data')
        Directory to which the data will be saved.

    **Returns**

    Dataset 
        Object dataset. Use ``dataset.graph()`` to download the graph.
    
    
    """
    url = 'http://www.web-of-life.es/networkjson.php?id=FW_007'
    data_type = 'weboflife_foodwebs_json'
    data_name = 'networkjson.php?id=FW_007'
    compress_type = None
    infos = {
         'type': data_type,
         'download_url' : url,
        'info_url': 'http://www.web-of-life.es/map.php?type=7',
        'source' :  'Christian, RR., Luczkovich JJ. (1999) Organizing and understanding a winter’s seagrass foodweb network through effective trophic levels'
    }

    data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
    return data
    

def food_webs_Bascompte_et_all_2005(save_path='./data'):    
    """Food webs of J. Bascompte, C. J. Melián and E. Sala .
    
    - Nodes: **249** 
    - Edges: **3313**
    - Directed: **True**
    - Components: **1**
    - Note: *Canibalism has been found in 11 species or groups. Crabs, Shrimps, Polychaetes, Gastropods, Squids, Octopuses, Asteroids, Echinoids, Mycteroperca venenosa, Scomberomorus cavalla, Tylosurus acus*
    - Description: *Cell values indicate the relative frequency of prey species/group in the diet of each predator species/group.*

    **Reference**
    
    J. Bascompte, C. J. Melián and E. Sala (2005). Interaction strength combinations and the overfishing of a marine food web. Proceedings of the National Academy of Sciences USA, 102: 5443-5447. 
    
    **Parameters**

    save_path : String : (default='./data')
        Directory to which the data will be saved.

    **Returns**

    Dataset 
        Object dataset. Use ``dataset.graph()`` to download the graph.
    
    
    """
    url = 'http://www.web-of-life.es/networkjson.php?id=FW_008'
    data_type = 'weboflife_foodwebs_json'
    data_name = 'networkjson.php?id=FW_008'
    compress_type = None
    infos = {
         'type': data_type,
         'download_url' : url,
        'info_url': 'http://www.web-of-life.es/map.php?type=7',
        'source' :  'J. Bascompte, C. J. Melián and E. Sala (2005). Interaction strength combinations and the overfishing of a marine food web. Proceedings of the National Academy of Sciences USA, 102: 5443-5447. '
    }

    data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
    return data
    

def food_webs_Angelini_et_all_2013(save_path='./data'):    
    """Food webs of Angelini, R., Morais, R., Catella AC., Resende KE., Libralato, S. .
    
    - Nodes: **40** 
    - Edges: **241**
    - Directed: **True**
    - Components: **1**
    - Note: **
    - Description: *Cell values indicate the relative frequency of prey species/group in the diet of each predator species/group.*

    **Reference**
    
    Angelini, R., Morais, R., Catella AC., Resende KE., Libralato, S. (2013) Aquatic food webs of the oxbow lakes in the Pantanal: A new site for fisheries guaranteed by alternated control? Ecological Modelling 253 (82– 96)
    
    **Parameters**

    save_path : String : (default='./data')
        Directory to which the data will be saved.

    **Returns**

    Dataset 
        Object dataset. Use ``dataset.graph()`` to download the graph.
    
    
    """
    url = 'http://www.web-of-life.es/networkjson.php?id=FW_009'
    data_type = 'weboflife_foodwebs_json'
    data_name = 'networkjson.php?id=FW_009'
    compress_type = None
    infos = {
         'type': data_type,
         'download_url' : url,
        'info_url': 'http://www.web-of-life.es/map.php?type=7',
        'source' :  'Angelini, R., Morais, R., Catella AC., Resende KE., Libralato, S. (2013) Aquatic food webs of the oxbow lakes in the Pantanal: A new site for fisheries guaranteed by alternated control? Ecological Modelling 253 (82– 96)'
    }

    data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
    return data
    

def food_webs_Angelini_et_all_2013(save_path='./data'):    
    """Food webs of Angelini, R., Morais, R., Catella AC., Resende KE., Libralato, S. .
    
    - Nodes: **39** 
    - Edges: **248**
    - Directed: **True**
    - Components: **1**
    - Note: **
    - Description: *Cell values indicate the relative frequency of prey species/group in the diet of each predator species/group.*

    **Reference**
    
    Angelini, R., Morais, R., Catella AC., Resende KE., Libralato, S. (2013) Aquatic food webs of the oxbow lakes in the Pantanal: A new site for fisheries guaranteed by alternated control? Ecological Modelling 253 (82– 96)
    
    **Parameters**

    save_path : String : (default='./data')
        Directory to which the data will be saved.

    **Returns**

    Dataset 
        Object dataset. Use ``dataset.graph()`` to download the graph.
    
    
    """
    url = 'http://www.web-of-life.es/networkjson.php?id=FW_010'
    data_type = 'weboflife_foodwebs_json'
    data_name = 'networkjson.php?id=FW_010'
    compress_type = None
    infos = {
         'type': data_type,
         'download_url' : url,
        'info_url': 'http://www.web-of-life.es/map.php?type=7',
        'source' :  'Angelini, R., Morais, R., Catella AC., Resende KE., Libralato, S. (2013) Aquatic food webs of the oxbow lakes in the Pantanal: A new site for fisheries guaranteed by alternated control? Ecological Modelling 253 (82– 96)'
    }

    data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
    return data
    

def food_webs_Thompson_and_Townsend_2003(save_path='./data'):    
    """Food webs of Thompson, R., Townsend, C. .
    
    - Nodes: **105** 
    - Edges: **343**
    - Directed: **True**
    - Components: **1**
    - Note: **
    - Description: **

    **Reference**
    
    Thompson, R., Townsend, C. (2003) IMPACTS ON STREAM FOOD WEBS OF NATIVE AND EXOTIC FOREST: AN INTERCONTINENTAL COMPARISON. Ecology, 84(1), pp. 145–161
    
    **Parameters**

    save_path : String : (default='./data')
        Directory to which the data will be saved.

    **Returns**

    Dataset 
        Object dataset. Use ``dataset.graph()`` to download the graph.
    
    
    """
    url = 'http://www.web-of-life.es/networkjson.php?id=FW_011'
    data_type = 'weboflife_foodwebs_json'
    data_name = 'networkjson.php?id=FW_011'
    compress_type = None
    infos = {
         'type': data_type,
         'download_url' : url,
        'info_url': 'http://www.web-of-life.es/map.php?type=7',
        'source' :  'Thompson, R., Townsend, C. (2003) IMPACTS ON STREAM FOOD WEBS OF NATIVE AND EXOTIC FOREST: AN INTERCONTINENTAL COMPARISON. Ecology, 84(1), pp. 145–161'
    }

    data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
    return data
    

def food_webs_Thompson_and_Townsend_2003_01(save_path='./data'):    
    """Food webs of Thompson, R., Townsend, C. .
    
    - Nodes: **58** 
    - Edges: **126**
    - Directed: **True**
    - Components: **1**
    - Note: **
    - Description: **

    **Reference**
    
    Thompson, R., Townsend, C. (2003) IMPACTS ON STREAM FOOD WEBS OF NATIVE AND EXOTIC FOREST: AN INTERCONTINENTAL COMPARISON. Ecology, 84(1), pp. 145–161
    
    **Parameters**

    save_path : String : (default='./data')
        Directory to which the data will be saved.

    **Returns**

    Dataset 
        Object dataset. Use ``dataset.graph()`` to download the graph.
    
    
    """
    url = 'http://www.web-of-life.es/networkjson.php?id=FW_012_01'
    data_type = 'weboflife_foodwebs_json'
    data_name = 'networkjson.php?id=FW_012_01'
    compress_type = None
    infos = {
         'type': data_type,
         'download_url' : url,
        'info_url': 'http://www.web-of-life.es/map.php?type=7',
        'source' :  'Thompson, R., Townsend, C. (2003) IMPACTS ON STREAM FOOD WEBS OF NATIVE AND EXOTIC FOREST: AN INTERCONTINENTAL COMPARISON. Ecology, 84(1), pp. 145–161'
    }

    data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
    return data
    

def food_webs_Thompson_and_Townsend_2003_02(save_path='./data'):    
    """Food webs of Thompson, R., Townsend, C. .
    
    - Nodes: **71** 
    - Edges: **148**
    - Directed: **True**
    - Components: **1**
    - Note: **
    - Description: **

    **Reference**
    
    Thompson, R., Townsend, C. (2003) IMPACTS ON STREAM FOOD WEBS OF NATIVE AND EXOTIC FOREST: AN INTERCONTINENTAL COMPARISON. Ecology, 84(1), pp. 145–161
    
    **Parameters**

    save_path : String : (default='./data')
        Directory to which the data will be saved.

    **Returns**

    Dataset 
        Object dataset. Use ``dataset.graph()`` to download the graph.
    
    
    """
    url = 'http://www.web-of-life.es/networkjson.php?id=FW_012_02'
    data_type = 'weboflife_foodwebs_json'
    data_name = 'networkjson.php?id=FW_012_02'
    compress_type = None
    infos = {
         'type': data_type,
         'download_url' : url,
        'info_url': 'http://www.web-of-life.es/map.php?type=7',
        'source' :  'Thompson, R., Townsend, C. (2003) IMPACTS ON STREAM FOOD WEBS OF NATIVE AND EXOTIC FOREST: AN INTERCONTINENTAL COMPARISON. Ecology, 84(1), pp. 145–161'
    }

    data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
    return data
    

def food_webs_Thompson_and_Townsend_2003_04(save_path='./data'):    
    """Food webs of Thompson, R., Townsend, C. .
    
    - Nodes: **77** 
    - Edges: **240**
    - Directed: **True**
    - Components: **1**
    - Note: **
    - Description: **

    **Reference**
    
    Thompson, R., Townsend, C. (2003) IMPACTS ON STREAM FOOD WEBS OF NATIVE AND EXOTIC FOREST: AN INTERCONTINENTAL COMPARISON. Ecology, 84(1), pp. 145–161
    
    **Parameters**

    save_path : String : (default='./data')
        Directory to which the data will be saved.

    **Returns**

    Dataset 
        Object dataset. Use ``dataset.graph()`` to download the graph.
    
    
    """
    url = 'http://www.web-of-life.es/networkjson.php?id=FW_013_02'
    data_type = 'weboflife_foodwebs_json'
    data_name = 'networkjson.php?id=FW_013_02'
    compress_type = None
    infos = {
         'type': data_type,
         'download_url' : url,
        'info_url': 'http://www.web-of-life.es/map.php?type=7',
        'source' :  'Thompson, R., Townsend, C. (2003) IMPACTS ON STREAM FOOD WEBS OF NATIVE AND EXOTIC FOREST: AN INTERCONTINENTAL COMPARISON. Ecology, 84(1), pp. 145–161'
    }

    data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
    return data
    

def food_webs_Thompson_and_Townsend_2003_05(save_path='./data'):    
    """Food webs of Thompson, R., Townsend, C. .
    
    - Nodes: **78** 
    - Edges: **241**
    - Directed: **True**
    - Components: **1**
    - Note: **
    - Description: **

    **Reference**
    
    Thompson, R., Townsend, C. (2003) IMPACTS ON STREAM FOOD WEBS OF NATIVE AND EXOTIC FOREST: AN INTERCONTINENTAL COMPARISON. Ecology, 84(1), pp. 145–161
    
    **Parameters**

    save_path : String : (default='./data')
        Directory to which the data will be saved.

    **Returns**

    Dataset 
        Object dataset. Use ``dataset.graph()`` to download the graph.
    
    
    """
    url = 'http://www.web-of-life.es/networkjson.php?id=FW_013_03'
    data_type = 'weboflife_foodwebs_json'
    data_name = 'networkjson.php?id=FW_013_03'
    compress_type = None
    infos = {
         'type': data_type,
         'download_url' : url,
        'info_url': 'http://www.web-of-life.es/map.php?type=7',
        'source' :  'Thompson, R., Townsend, C. (2003) IMPACTS ON STREAM FOOD WEBS OF NATIVE AND EXOTIC FOREST: AN INTERCONTINENTAL COMPARISON. Ecology, 84(1), pp. 145–161'
    }

    data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
    return data
    

def food_webs_Thompson_and_Townsend_2003_06(save_path='./data'):    
    """Food webs of Thompson, R., Townsend, C. .
    
    - Nodes: **78** 
    - Edges: **268**
    - Directed: **True**
    - Components: **1**
    - Note: **
    - Description: **

    **Reference**
    
    Thompson, R., Townsend, C. (2003) IMPACTS ON STREAM FOOD WEBS OF NATIVE AND EXOTIC FOREST: AN INTERCONTINENTAL COMPARISON. Ecology, 84(1), pp. 145–161
    
    **Parameters**

    save_path : String : (default='./data')
        Directory to which the data will be saved.

    **Returns**

    Dataset 
        Object dataset. Use ``dataset.graph()`` to download the graph.
    
    
    """
    url = 'http://www.web-of-life.es/networkjson.php?id=FW_013_04'
    data_type = 'weboflife_foodwebs_json'
    data_name = 'networkjson.php?id=FW_013_04'
    compress_type = None
    infos = {
         'type': data_type,
         'download_url' : url,
        'info_url': 'http://www.web-of-life.es/map.php?type=7',
        'source' :  'Thompson, R., Townsend, C. (2003) IMPACTS ON STREAM FOOD WEBS OF NATIVE AND EXOTIC FOREST: AN INTERCONTINENTAL COMPARISON. Ecology, 84(1), pp. 145–161'
    }

    data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
    return data
    

def food_webs_Thompson_and_Townsend_2003_07(save_path='./data'):    
    """Food webs of Thompson, R., Townsend, C. .
    
    - Nodes: **98** 
    - Edges: **629**
    - Directed: **True**
    - Components: **1**
    - Note: **
    - Description: **

    **Reference**
    
    Thompson, R., Townsend, C. (2003) IMPACTS ON STREAM FOOD WEBS OF NATIVE AND EXOTIC FOREST: AN INTERCONTINENTAL COMPARISON. Ecology, 84(1), pp. 145–161
    
    **Parameters**

    save_path : String : (default='./data')
        Directory to which the data will be saved.

    **Returns**

    Dataset 
        Object dataset. Use ``dataset.graph()`` to download the graph.
    
    
    """
    url = 'http://www.web-of-life.es/networkjson.php?id=FW_013_05'
    data_type = 'weboflife_foodwebs_json'
    data_name = 'networkjson.php?id=FW_013_05'
    compress_type = None
    infos = {
         'type': data_type,
         'download_url' : url,
        'info_url': 'http://www.web-of-life.es/map.php?type=7',
        'source' :  'Thompson, R., Townsend, C. (2003) IMPACTS ON STREAM FOOD WEBS OF NATIVE AND EXOTIC FOREST: AN INTERCONTINENTAL COMPARISON. Ecology, 84(1), pp. 145–161'
    }

    data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
    return data
    

def food_webs_Townsend_et_all_1998_01(save_path='./data'):    
    """Food webs of Townsend, R. Colin., Thompson, M. Ross., McInstosh, R. Angus., Kilroy, Cathy., Edwards, Eric., Scarsbrook, R. Mike. .
    
    - Nodes: **86** 
    - Edges: **375**
    - Directed: **True**
    - Components: **1**
    - Note: **
    - Description: **

    **Reference**
    
    Townsend, R. Colin., Thompson, M. Ross., McInstosh, R. Angus., Kilroy, Cathy., Edwards, Eric., Scarsbrook, R. Mike. (1998) Disturbance, resource supply, and food-web architecture in streams. Ecology Letters 1: 200-109 
    
    **Parameters**

    save_path : String : (default='./data')
        Directory to which the data will be saved.

    **Returns**

    Dataset 
        Object dataset. Use ``dataset.graph()`` to download the graph.
    
    
    """
    url = 'http://www.web-of-life.es/networkjson.php?id=FW_014_01'
    data_type = 'weboflife_foodwebs_json'
    data_name = 'networkjson.php?id=FW_014_01'
    compress_type = None
    infos = {
         'type': data_type,
         'download_url' : url,
        'info_url': 'http://www.web-of-life.es/map.php?type=7',
        'source' :  'Townsend, R. Colin., Thompson, M. Ross., McInstosh, R. Angus., Kilroy, Cathy., Edwards, Eric., Scarsbrook, R. Mike. (1998) Disturbance, resource supply, and food-web architecture in streams. Ecology Letters 1: 200-109 '
    }

    data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
    return data
    

def food_webs_Townsend_et_all_1998_02(save_path='./data'):    
    """Food webs of Townsend, R. Colin., Thompson, M. Ross., McInstosh, R. Angus., Kilroy, Cathy., Edwards, Eric., Scarsbrook, R. Mike. .
    
    - Nodes: **94** 
    - Edges: **565**
    - Directed: **True**
    - Components: **1**
    - Note: *Canibalism has been found in 1 species or groups. Hydrobiosid sp1 FW_014_02*
    - Description: **

    **Reference**
    
    Townsend, R. Colin., Thompson, M. Ross., McInstosh, R. Angus., Kilroy, Cathy., Edwards, Eric., Scarsbrook, R. Mike. (1998) Disturbance, resource supply, and food-web architecture in streams. Ecology Letters 1: 200-109 
    
    **Parameters**

    save_path : String : (default='./data')
        Directory to which the data will be saved.

    **Returns**

    Dataset 
        Object dataset. Use ``dataset.graph()`` to download the graph.
    
    
    """
    url = 'http://www.web-of-life.es/networkjson.php?id=FW_014_02'
    data_type = 'weboflife_foodwebs_json'
    data_name = 'networkjson.php?id=FW_014_02'
    compress_type = None
    infos = {
         'type': data_type,
         'download_url' : url,
        'info_url': 'http://www.web-of-life.es/map.php?type=7',
        'source' :  'Townsend, R. Colin., Thompson, M. Ross., McInstosh, R. Angus., Kilroy, Cathy., Edwards, Eric., Scarsbrook, R. Mike. (1998) Disturbance, resource supply, and food-web architecture in streams. Ecology Letters 1: 200-109 '
    }

    data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
    return data
    

def food_webs_Townsend_et_all_1998_03(save_path='./data'):    
    """Food webs of Townsend, R. Colin., Thompson, M. Ross., McInstosh, R. Angus., Kilroy, Cathy., Edwards, Eric., Scarsbrook, R. Mike. .
    
    - Nodes: **108** 
    - Edges: **708**
    - Directed: **True**
    - Components: **1**
    - Note: *Canibalism has been found in 1 species or groups. Paranephrops zealandicus*
    - Description: **

    **Reference**
    
    Townsend, R. Colin., Thompson, M. Ross., McInstosh, R. Angus., Kilroy, Cathy., Edwards, Eric., Scarsbrook, R. Mike. (1998) Disturbance, resource supply, and food-web architecture in streams. Ecology Letters 1: 200-109 
    
    **Parameters**

    save_path : String : (default='./data')
        Directory to which the data will be saved.

    **Returns**

    Dataset 
        Object dataset. Use ``dataset.graph()`` to download the graph.
    
    
    """
    url = 'http://www.web-of-life.es/networkjson.php?id=FW_014_03'
    data_type = 'weboflife_foodwebs_json'
    data_name = 'networkjson.php?id=FW_014_03'
    compress_type = None
    infos = {
         'type': data_type,
         'download_url' : url,
        'info_url': 'http://www.web-of-life.es/map.php?type=7',
        'source' :  'Townsend, R. Colin., Thompson, M. Ross., McInstosh, R. Angus., Kilroy, Cathy., Edwards, Eric., Scarsbrook, R. Mike. (1998) Disturbance, resource supply, and food-web architecture in streams. Ecology Letters 1: 200-109 '
    }

    data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
    return data
    

def food_webs_Townsend_et_all_1998_04(save_path='./data'):    
    """Food webs of Townsend, R. Colin., Thompson, M. Ross., McInstosh, R. Angus., Kilroy, Cathy., Edwards, Eric., Scarsbrook, R. Mike. .
    
    - Nodes: **112** 
    - Edges: **832**
    - Directed: **True**
    - Components: **1**
    - Note: *Canibalism has been found in 2 species or groups. Stenoperla prasinia, Psilochorema bidens*
    - Description: **

    **Reference**
    
    Townsend, R. Colin., Thompson, M. Ross., McInstosh, R. Angus., Kilroy, Cathy., Edwards, Eric., Scarsbrook, R. Mike. (1998) Disturbance, resource supply, and food-web architecture in streams. Ecology Letters 1: 200-109 
    
    **Parameters**

    save_path : String : (default='./data')
        Directory to which the data will be saved.

    **Returns**

    Dataset 
        Object dataset. Use ``dataset.graph()`` to download the graph.
    
    
    """
    url = 'http://www.web-of-life.es/networkjson.php?id=FW_014_04'
    data_type = 'weboflife_foodwebs_json'
    data_name = 'networkjson.php?id=FW_014_04'
    compress_type = None
    infos = {
         'type': data_type,
         'download_url' : url,
        'info_url': 'http://www.web-of-life.es/map.php?type=7',
        'source' :  'Townsend, R. Colin., Thompson, M. Ross., McInstosh, R. Angus., Kilroy, Cathy., Edwards, Eric., Scarsbrook, R. Mike. (1998) Disturbance, resource supply, and food-web architecture in streams. Ecology Letters 1: 200-109 '
    }

    data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
    return data
    

def food_webs_Thompson_and_Townsend_2000_01(save_path='./data'):    
    """Food webs of Thompson, R., Townsend, C. .
    
    - Nodes: **96** 
    - Edges: **634**
    - Directed: **True**
    - Components: **1**
    - Note: **
    - Description: **

    **Reference**
    
    Thompson, R., Townsend, C. (2000) Is resolution the solution?: the effect of taxonomic resolution on the calculated properties of three stream food webs. Freshwater Biology  44, 413-422
    
    **Parameters**

    save_path : String : (default='./data')
        Directory to which the data will be saved.

    **Returns**

    Dataset 
        Object dataset. Use ``dataset.graph()`` to download the graph.
    
    
    """
    url = 'http://www.web-of-life.es/networkjson.php?id=FW_015_01'
    data_type = 'weboflife_foodwebs_json'
    data_name = 'networkjson.php?id=FW_015_01'
    compress_type = None
    infos = {
         'type': data_type,
         'download_url' : url,
        'info_url': 'http://www.web-of-life.es/map.php?type=7',
        'source' :  'Thompson, R., Townsend, C. (2000) Is resolution the solution?: the effect of taxonomic resolution on the calculated properties of three stream food webs. Freshwater Biology  44, 413-422'
    }

    data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
    return data
    

def food_webs_Thompson_and_Townsend_2000_02(save_path='./data'):    
    """Food webs of Thompson, R., Townsend, C. .
    
    - Nodes: **83** 
    - Edges: **415**
    - Directed: **True**
    - Components: **1**
    - Note: *Canibalism has been found in 1 species or groups. Stenoperla prasinia*
    - Description: **

    **Reference**
    
    Thompson, R., Townsend, C. (2000) Is resolution the solution?: the effect of taxonomic resolution on the calculated properties of three stream food webs. Freshwater Biology  44, 413-422
    
    **Parameters**

    save_path : String : (default='./data')
        Directory to which the data will be saved.

    **Returns**

    Dataset 
        Object dataset. Use ``dataset.graph()`` to download the graph.
    
    
    """
    url = 'http://www.web-of-life.es/networkjson.php?id=FW_015_02'
    data_type = 'weboflife_foodwebs_json'
    data_name = 'networkjson.php?id=FW_015_02'
    compress_type = None
    infos = {
         'type': data_type,
         'download_url' : url,
        'info_url': 'http://www.web-of-life.es/map.php?type=7',
        'source' :  'Thompson, R., Townsend, C. (2000) Is resolution the solution?: the effect of taxonomic resolution on the calculated properties of three stream food webs. Freshwater Biology  44, 413-422'
    }

    data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
    return data
    

def food_webs_Thompson_and_Townsend_2000_03(save_path='./data'):    
    """Food webs of Thompson, R., Townsend, C. .
    
    - Nodes: **93** 
    - Edges: **538**
    - Directed: **True**
    - Components: **1**
    - Note: **
    - Description: **

    **Reference**
    
    Thompson, R., Townsend, C. (2000) Is resolution the solution?: the effect of taxonomic resolution on the calculated properties of three stream food webs. Freshwater Biology  44, 413-422
    
    **Parameters**

    save_path : String : (default='./data')
        Directory to which the data will be saved.

    **Returns**

    Dataset 
        Object dataset. Use ``dataset.graph()`` to download the graph.
    
    
    """
    url = 'http://www.web-of-life.es/networkjson.php?id=FW_015_03'
    data_type = 'weboflife_foodwebs_json'
    data_name = 'networkjson.php?id=FW_015_03'
    compress_type = None
    infos = {
         'type': data_type,
         'download_url' : url,
        'info_url': 'http://www.web-of-life.es/map.php?type=7',
        'source' :  'Thompson, R., Townsend, C. (2000) Is resolution the solution?: the effect of taxonomic resolution on the calculated properties of three stream food webs. Freshwater Biology  44, 413-422'
    }

    data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
    return data
    

def food_webs_Thompson_and_Townsend_2000_04(save_path='./data'):    
    """Food webs of Thompson, R., Townsend, C. .
    
    - Nodes: **107** 
    - Edges: **966**
    - Directed: **True**
    - Components: **1**
    - Note: *Canibalism has been found in 1 species or groups. Megaleptoperla sp1 FW_015_04*
    - Description: **

    **Reference**
    
    Thompson, R., Townsend, C. (2000) Is resolution the solution?: the effect of taxonomic resolution on the calculated properties of three stream food webs. Freshwater Biology  44, 413-422
    
    **Parameters**

    save_path : String : (default='./data')
        Directory to which the data will be saved.

    **Returns**

    Dataset 
        Object dataset. Use ``dataset.graph()`` to download the graph.
    
    
    """
    url = 'http://www.web-of-life.es/networkjson.php?id=FW_015_04'
    data_type = 'weboflife_foodwebs_json'
    data_name = 'networkjson.php?id=FW_015_04'
    compress_type = None
    infos = {
         'type': data_type,
         'download_url' : url,
        'info_url': 'http://www.web-of-life.es/map.php?type=7',
        'source' :  'Thompson, R., Townsend, C. (2000) Is resolution the solution?: the effect of taxonomic resolution on the calculated properties of three stream food webs. Freshwater Biology  44, 413-422'
    }

    data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
    return data
    

def food_webs_Baeta_et_all_2011_01(save_path='./data'):    
    """Food webs of Baeta, A. , Niquil, A., Marques, J. C., Patrício, J. .
    
    - Nodes: **37** 
    - Edges: **242**
    - Directed: **True**
    - Components: **1**
    - Note: *Canibalism has been found in 6 species or groups. Zooplankton, Carcinus maenas, Crangon crangon, Glycera tridactyla, Nephthys sp1 FW_016_01, Nemertini*
    - Description: *Cell values indicate the relative frequency of prey species/group in the diet of each predator species/group.*

    **Reference**
    
    Baeta, A. , Niquil, A., Marques, J. C., Patrício, J. (2011) Modelling the effects of eutrophication, mitigation measures and an extreme flood event on estuarine benthic food webs. Ecological Modelling 222, 1209–1221
    
    **Parameters**

    save_path : String : (default='./data')
        Directory to which the data will be saved.

    **Returns**

    Dataset 
        Object dataset. Use ``dataset.graph()`` to download the graph.
    
    
    """
    url = 'http://www.web-of-life.es/networkjson.php?id=FW_016_01'
    data_type = 'weboflife_foodwebs_json'
    data_name = 'networkjson.php?id=FW_016_01'
    compress_type = None
    infos = {
         'type': data_type,
         'download_url' : url,
        'info_url': 'http://www.web-of-life.es/map.php?type=7',
        'source' :  'Baeta, A. , Niquil, A., Marques, J. C., Patrício, J. (2011) Modelling the effects of eutrophication, mitigation measures and an extreme flood event on estuarine benthic food webs. Ecological Modelling 222, 1209–1221'
    }

    data = Dataset(url, save_path, data_type, data_name, compress_type, infos)
    return data
    


