import dynamicalab as dlb
import os

class Dataset(object):
	"""
	Base class to load networks datasets.
	
	Datasets hold the information about the data and can construct graphs.
	
	**Parameters**

	url : String
		Download url.

	save_path : String
		Save the data into this directory. If it already exists, it will try to get the data or download it and copy it there. If the directory does not exist, the script will create the directory. 

	data_type : String
		In which form the data should be read. Implemented format are : ``gml``, ``bipartite``, ``adjacency``. See ``data2graph`` for description.

	data_name : String
		Name of the file from the downloaded files that should be use to construct the network. 

	compress_type : String
		Tells the script what it downloads. Implemented format are : ``ZIP``, ``None``. If ``None``, then it suggests that the downloaded file is not compressed.

	infos : dictionary
		Information about the dataset. It is accessible through ``print(dataset)``.

	"""
	def __init__(self, url, save_path, data_type, data_name, compress_type, infos={}):
		"""Initialization of the dataset. Anything is done at this point. To download the dataset, you need to call the method ``dataset.graph()``.

		**Parameters**

		url : String
			Download url.

		save_path : String
			Save the data into this directory. If already existing, it will try to get the data or download it and copy it there. If the directory does not exist, the script will create it. 

		data_type : String
			In which form the data should be read. Implemented format are : ``gml``, ``bipartite``, ``adjacency``. See ``data2graph`` for description.

		data_name : String
			Name of the downloaded file that should be use to construct the network. 

		compress_type : String
			Tells the script what it downloads. Implemented format are : ``ZIP``, ``None``. If ``None``, then it suggests that the downloaded file is not compressed.

		infos : dictionary
			Information about the dataset. It is accessible through ``print(dataset)``.


		"""
		self.url = url
		self.save_path = save_path
		self.data_type = data_type
		self.data_name = data_name
		if self.is_valid_compression(compress_type):
			self.compress_type = compress_type
		self.infos = infos
		return

	def graph(self, custom_data2graph=None):
		"""Construct a networkx Graph of the dataset. 

		1. Check if the file is already downloaded in ``save_path``. If not, download it and copy it.
		
		2. Construct the graph from the data. The method ``self.data2graph`` already implements some construction methods. If the dataset requires a different treatment, it is recommended to
		pass your custom method ``custom_data2graph`` that will be called as ``G = custom_data2graph(data_path)``. If ``custom_data2graph!=None``, then the `data_name` is passed to this custom constructor. 

		.. note::
			
			The constructed graph is not holded in memory.

		**Parameters**

		custom_data2graph : method
			If ``None``, this method is called to construct the network. It receives as an argument the path to the data and is expected to return the graph.

		"""
		data_path = self.download_data()
		if custom_data2graph:
			return custom_data2graph(data_path)
		return self.data2graph(data_path)

	def is_valid_compression(self, compress_type):
		if compress_type not in ["ZIP", None]:
			raise dlb.DynamicaLabNotImplemented
		return True

	def is_downloaded(self):
	
		fname = os.path.join(self.save_path, self.data_name)
		return os.path.isfile(fname) 

	def download_data(self):

		# Download
		filename = self.url.rpartition('/')[2]
		filename_no_extension = filename.rpartition('.')[0]
		file_path = os.path.join("./", filename)

		if (self.is_downloaded()==False):
			from six.moves import urllib
			urllib.request.urlretrieve(self.url, file_path)
			self.uncompress_data(file_path, filename_no_extension)
			
		return self.save_path +"/"+self.data_name


	def uncompress_data(self, file_path, filename_no_extension):
		if self.compress_type == "ZIP":
			import zipfile
			with zipfile.ZipFile(file_path, 'r') as myzip:
				myzip.extractall(self.save_path+"/")
				os.unlink(file_path)

		elif self.compress_type == None:
			if os.path.isdir(self.save_path)==False:
				os.makedirs(self.save_path)
			os.rename(file_path, os.path.join(self.save_path,file_path))

		
	def data2graph(self, path, create_using=None):
		import networkx as nx
		import numpy as np

		if self.data_type == "gml":
			return nx.read_gml(path)

		elif self.data_type == "bipartite":

			A = np.loadtxt(path)
			G = nx.Graph()

			for i in range(A.shape[0]):
				for j in range(A.shape[1]):
					G.add_edge(i,j, weight=A[i,j])
			return G
		elif self.data_type == "edgelist":
			return nx.read_edgelist(path, comments="#")
			
		elif self.data_type == "adjacency":
			A = np.loadtxt(path)
			return nx.from_numpy_matrix(A)

		raise dlb.DynamicaLabNotImplemented

	def __str__(self):
		for key in self.infos:
			print(key)
			print("----------")
			print(self.infos[key])
			print("")
		return ""


