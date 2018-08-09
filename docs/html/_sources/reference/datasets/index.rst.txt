.. _datasets:


************************
Datasets
************************

.. automodule:: dynamicalab

Bipartite 
==================

.. autosummary::
   :toctree: generated/

   plants_pollinators_Ramirez1992
   plants_pollinators_McCullen1993



Usage
=================

.. code:: python 
	
	import dynamicalab as dlb

	data = dlb.plants_pollinators_McCullen1993(save_path="./datas")
	G = data.graph()