from .base import BaseDynamics
import numpy as np

class BernoulliDynamics(BaseDynamics):
    """Random binary dynamics with probability ``p`` of being active."""

    def __init__(self, p=None):
        """
        **Params**

        p : float : (default=None)
            Probability of being active (x=1). If None, then ``p``
            is choosen randomly between 0 and 1.

        """
        super(BernoulliDynamics, self).__init__()

        if p is None:
            self.p = np.random.rand()
        else:
            self.p = p
            
    def __call__(self, G, T, x0=None):

        num_time_steps = len(T)
        _x = np.random.rand(num_time_steps, len(G))

        X = np.zeros([num_time_steps, len(G)])
        X[_x < self.p] = 1

        return  X

