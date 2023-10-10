import numpy as np
import pywt as pywt
from timeflux.core.node import Node


class Dwt(Node):
    
 def __init__(self, func= 'db2'):
     
     self._func = 'db2'
     
def update(self):
    # Make sure we have a non-empty dataframe
    if self.i.ready():

        self.o.data = pywt.dwt(self.i, self._func)

