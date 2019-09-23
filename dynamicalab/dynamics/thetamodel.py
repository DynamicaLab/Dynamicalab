
import networkx as nx
import numpy as np
from scipy.integrate import odeint

from .base import BaseDynamics


class ThetaModelDynamics(BaseDynamics):
	"""Theta model, or Ermentrout–Kopell canonical model, is
	a biological neuron model.


	.. math::
		\dfrac{dx_i}{dt} = 1-\cos(x_i) + [1+\cos(x_i)]\eta_j

		\eta_j = \Big[I + \dfrac{\sigma}{N}\sum_{j=1}^N w_{ij}(1-\cos(x_j))\Big]


	Since the activity is interpreted as an angle, it is typical to take the
	cosinus of the activity.

	"""
	def __init__(self, sigma=0.1, input_intensity=0.5, cos_transform=True):
		"""

		**Parameters**

		sigma : Float : (default=0.1)

		input_intensity : Float : (default=0.5)
			Input intensity to each node.

		cos_transform : Bool : (default=True)
			If true, take the cosinus of the activity as output.

		"""
		super(ThetaModelDynamics, self).__init__()
		self.sigma = sigma
		self.I = input_intensity
		self.cos_transform = cos_transform
		return
	
	def best_x0(self, G):
		"""Random numbers between 0 and ``2*np.pi``
		"""
		return np.random.uniform(0,2*np.pi, size=(G.number_of_nodes(),))
	
	def __call__(self, G, T, x0=None):

		if x0 is None:
			x0 = self.best_x0(G)
		
		W = nx.to_numpy_array(G)
		N = G.number_of_nodes()

		dt = T[1]-T[0]

		def ode(x, T, W):

			net = self.I + self.sigma/N * (W @ (1-np.cos(x)))
			dydt = (1-np.cos(x)) + (1+np.cos(x))*net
			return dydt
		
		X = odeint(ode, x0, T, args=(W.copy(), ))

		if self.cos_transform:
			return np.cos(X)

		return X
		
	