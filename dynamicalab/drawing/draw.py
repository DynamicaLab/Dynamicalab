import numpy as np
import matplotlib.patches as mpatches
import networkx as nx
from matplotlib.patches import FancyArrowPatch as ArrowPath
from matplotlib.font_manager import FontProperties



def draw_curved_edges(edges, pos, ax, mu=0.05, edge_color="black", edge_width=1.0, alpha=1.0, arrow_scale=20.0, loopsize=0):
	"""This function plot the edges of a graph with a certain curvature. It can also plot arrows for direction. For self-loop, it is possible
		to plot an edge that does a circle passing throught the node. The size of the circle is controlled by the parameter ``loopsize``. 
		

		**Parameters**
		
	
		edges : list
			A list of edges succh taht edges are tuple of node ids, ``(nodeA, nodeB)``.
		
		pos : dictionnary
			A dictionnary of nodes position.

		ax : Matplotlib Axes object
			Draw the edges in the specified Matplotlib axes.

		mu : float : (default=0.05)
			Level of curvature. Should always be positive. If zero, then edges are straight.  

		edge_color :  str or list : (default="black")
			If a list, then each entry is the color of the edge when iterated through edges. If a string, then each edge will have the same color.
		
		alpha : float : (default=1)
			Edges opacity

		arrow_scale : float : (default=20)
			Control the size of the arrows. If equal to zero, then the arrows become invisible.

		loopsize : float : (default=0)
			If ``edges`` contains self-loops, i.e. ``edge==(nodeA, nodeA)``, then it draw a self-loop which is composed of a simple circle. The radius of the circle is controlled by ``loopsize``

		
		**Example**
		

		.. code:: python

			import networkx as nx
			import dynamicalab.drawing as draw
			import matplotlib.pyplot as plt

			G = nx.erdos_renyi_graph(20,0.1)
			pos = nx.spring_layout(G)
			edges = G.edges()

			fig = plt.figure()
			ax = plt.gca()

			draw.draw_curved_edges(edges, pos, ax, mu=5)

			plt.show()
		

		.. seealso::
			
			draw_networks


	"""

	for v,edge in enumerate(edges):
		
		x1,y1 = pos[edge[0]]
		x2,y2 = pos[edge[1]]
		
		#If self loop
		if edge[0]==edge[1]:
			dv = 0.0
			theta = np.linspace(0.0,2.0*np.pi, 100)
			X = np.cos(theta)*loopsize+x1-loopsize
			Y = np.sin(theta)*loopsize+y1
		
			
		else:
			dv = mu
			if x1>x2:
				x1,y1 = pos[edge[1]]
				x2,y2 = pos[edge[0]]
				dv = -mu

			dx = x2
			dy = y2

			# Center to origin
			x1 -= dx
			x2 -= dx
			y1 -= dy
			y2 -= dy

			r = ((y2-y1)**2.0 + (x2-x1)**2.0)**(0.5)

			theta = np.arctan2(y1, x1)
			c, s = np.cos(theta), np.sin(theta)
			R = np.matrix('{} {}; {} {}'.format(c, -s, s, c))

			# Rotate
			x1 = x2 - r
			y1 = y2

			# Find parabola
			h = (x2+x1)/2.0
			k = y2+dv*r
			a = (y2-k)/((x2-h)**2.0)
			X = np.linspace(x1,x2,100)
			Y = a*(X-h)**2.0+k

			# Rotate the parabola and translate
			theta = np.pi+theta
			c, s = np.cos(theta), np.sin(theta)
			R = np.matrix('{} {}; {} {}'.format(c, -s, s, c))
			for u in range(len(X)):
				C1 = np.array([X[u], Y[u]])
				C1 = np.dot(R, C1)
				X[u], Y[u] = C1[0,0]+dx , C1[0,1]+dy
		
		color = edge_color
		if type(edge_color)==list:
			color = edge_color[v]

		edgewidth = edge_width
		if type(edge_width)==list:
			edgewidth = edge_width[v]
		
		middle_index = int(len(X)/2)
		posA = (X[middle_index-5], Y[middle_index-5])
		posB = (X[middle_index+5], Y[middle_index+5])
		if dv<0.0:
			u = posA
			posA = posB
			posB = u
		
		try:
			arrow = ArrowPath(posA=posA, posB=posB, mutation_scale=arrow_scale,color=color)
			ax.add_patch(arrow)
		except:
			True


		ax.plot(X,Y, "-", linewidth=edgewidth, color=color, zorder=0, alpha=alpha)
		

def draw_networks(G, pos, ax, mu=0.08, 
					edge_color="black", 
					edge_width=1.0, 
					edge_alpha=1.0,
					use_edge_weigth=True,
					node_width=1.0,
					node_size=80.0,
					node_border_color="#404040",
					node_color="#EDEDED",
					node_alpha=1.0, 
					arrow_scale=20.0, 
					loop_radius=0.0, 
					letter="",
					letter_fontsize=13,
					letter_pos=[0.87, 0.02],
					letter_color="black"):
	"""This function draws networks. 
		

		**Parameters**
		
	
		G : Networkx Graph
			A Networkx ``Graph`` or ``DiGraph``.
		
		pos : dictionnary
			A dictionnary of nodes position.

		ax : Matplotlib Axes object
			Draw the network in the specified Matplotlib axes.
	
		mu : float : (default=0.05)
			Level of curvature. Should always be positive. If zero, then edges are straight.  

		edge_color :  str or list : (default="black")
			If a list, then each entry is the color of the edge when iterated through edges. If a string, then each edge will have the same color.
		
		edge_width : float or list : (default=1.0)
			Use this if ``use_edge_weigth==False`` for edge widths. If a list, each element must be in the same order as ``G.edges()``

		edge_alpha : float : (default=1)
			Edges opacity.
	
		use_edge_weigth : Bool : (default=True)
			Use the key ``weight`` of the edges attributes to choose the thickness of the edges.

		node_width : Float : (default=1.0)
			Node border width

		node_size : Float : (default=80)
			Controls the node size (proportional to radius).

		node_border_color : String : (default="#404040")
			Node border color.

		node_color : String or list : (default="#EDEDED")
			Node background color.

		node_alpha : float : (default=1.0)
			Node opacity.

		arrow_scale : float : (default=20)
			Control the size of the arrows. If equal to zero, then the arrows become invisible.

		loop_radius : float : (default=0)
			If ``edges`` contains self-loops, i.e. ``edge==(nodeA, nodeA)``, then it draw a self-loop which is composed of a simple circle. The radius of the circle is controlled by ``loop_radius``

		letter : string : (default="")
			Text that can be postionioned in the figure.

		letter_fontsize : float : (default=13)
			Font size of the text 

		letter_pos : List : (default=[0.87,0.02])
			Position of the text given in relative size of the plot. The first element is ``x``, the second is ``y``. 

		letter_color : String : (default="black")
			Color of the text
		
		**Example**
		

		.. code:: python

			import networkx as nx
			import dynamicalab.drawing as draw
			import matplotlib.pyplot as plt
			import seaborn as sns
			import numpy as np


			G = nx.erdos_renyi_graph(20,0.5)
			pos = nx.spring_layout(G)
			edges = G.edges()

			sns.set(style="ticks")
			fig = plt.figure()
			ax = plt.gca()

			node_colors = np.random.choice(['#b2182b','#d6604d','#f4a582','#fddbc7','#f7f7f7','#d1e5f0','#92c5de','#4393c3','#2166ac'],  20, replace=True)

			draw.draw_networks(G, pos, ax,
						mu=0.08, 
						edge_color="gray", 
						edge_width=1.5, 
						edge_alpha=0.6,
						use_edge_weigth=False,
						node_width=1.5,
						node_size=100.0,
						node_border_color="#404040",
						node_color=node_colors,
						node_alpha=1.0, 
						arrow_scale=0.0, 
						loop_radius=0, 
						letter="Example for Dynamicalab",
						letter_fontsize=16,
						letter_pos=[0.3, -0.05],
						letter_color="black")
		

		.. image:: /_static/assets/draw_example.png
			:align: center


	"""

	# Edges
	weights = [0]*len(G.edges())
	for i,edge in enumerate(G.edges()):
		if use_edge_weigth:
			weights[i] = G[edge[0]][edge[1]]['weight']
		else:
			if type(edge_width)==list:
				weights[i] = edge_width[i]
			else:
				weights[i] = edge_width
		
	draw_curved_edges(G.edges(), pos, ax, 
					mu=mu, 
					edge_color=edge_color, 
					alpha = edge_alpha,
					arrow_scale=arrow_scale,
					loopsize=loop_radius,
					edge_width=weights)

	# Nodes
	nodes = nx.draw_networkx_nodes(G, pos, 
		ax=ax, 
		node_size=node_size, 
		node_color=node_color, 
		linewidths=node_width)
	nodes.set_edgecolor(node_border_color)
	
	# Letter
	font = FontProperties()
	font.set_weight('bold')
	ax.text(letter_pos[0], letter_pos[1], letter, 
			verticalalignment='bottom', 
			horizontalalignment='left', 
			transform=ax.transAxes, 
			fontproperties=font,
			color=letter_color, 
			fontsize=letter_fontsize)

	# Axis
	ax.axis('off')
	return
