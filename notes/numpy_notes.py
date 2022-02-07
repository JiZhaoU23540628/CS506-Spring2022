import numpy as np
dis_array = np.array(dis) # convert dis to array
dis_array.ravel() # convert an array of all demensions to one dimension
np.unravel_index(i , dis_array.shape)
"""
np.unravel_index(i, dis_array.shape) is aming
to return the original index of these elements in the originlal matrix (dis_array.shape)"""
