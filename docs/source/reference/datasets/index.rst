.. _datasets:


************************
Datasets
************************

.. automodule:: dynamicalab

Bipartites
==================

.. autosummary::
   :toctree: generated/

   plants_pollinators
   plants_pollinators_Ramirez1992
   plants_pollinators_McCullen1993
   plants_pollinators_Arroyo1992_I
   plants_pollinators_Arroyo1992_II
   plants_pollinators_Arroyo1992_III
   plants_pollinators_Barrett1987
   plants_pollinators_Robsertson1992


Connectomes
=================

.. autosummary::
	:toctree: generated/
	     
	connectomes
	connectomes_CElegansSNAP

Usage
=================

.. code:: python 
	
	import dynamicalab as dlb

	data = dlb.plants_pollinators_McCullen1993(save_path="./datas")
	G = data.graph()