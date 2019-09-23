.. _classes:


************************
Dynamics 
************************

.. automodule:: dynamicalab.dynamics

Base class
----------
.. autoclass:: dynamicalab.dynamics.BaseDynamics
	:members: __call__

Available dynamics
------------------

All of the following dynamics inherit from ``BaseDynamics`` and have the
same general usage as above.

.. autosummary::
	:toctree: generated/
  	:nosignatures:

	SISDynamics
	ThetaModelDynamics
	BernoulliDynamics