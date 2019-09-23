.. _datasets:


************************
Datasets
************************

.. automodule:: dynamicalab



Usage
=================


We have created a convenient dataset loader. The datasets are automatically downloaded in the `save_path`. 
If the data have already been downloaded, the dataset are automatically loaded from the local path. 

Each dataset has a graph generator method to convert the raw data to a `nx.Graph`.


Example
--------------

.. code:: python 
   
   import dynamicalab as dlb

   data = dlb.plants_pollinators_McCullen1993(save_path="./datas")
   G = data.graph()


Bipartites (24 datasets)
=========================

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
   plants_pollinators_Kaiser2010
   plants_pollinators_Petanidou1991
   plants_pollinators_Clements1923
   plants_pollinators_Dicks2002I
   plants_pollinators_Dicks2002II
   plants_pollinators_Dupont2003
   plants_pollinators_Elberling1999I
   plants_pollinators_Elberling1999II
   plants_pollinators_Olesen2002I
   plants_pollinators_Olerton2003
   plants_pollinators_Hocking1968
   plants_pollinators_Herrera1988
   plants_pollinators_Memmott1999
   plants_pollinators_OlesenUnpublished
   plants_pollinators_Inouye1988
   plants_pollinators_Kevan1970
   plants_pollinators_Kato1990


Connectomes (1 dataset)
=========================

.. autosummary::
	:toctree: generated/
	     
	connectomes
	connectomes_CElegansSNAP

Food webs (7 datasets)
=========================

.. autosummary::
   :toctree: generated/
        
   food_webs
   food_webs_Angelini2005
   food_webs_Angelini2011
   food_webs_Angelini2011b
   food_webs_Angelini2006
   food_webs_Torres2013
   food_webs_Cruz2007
   food_webs_Christian1999