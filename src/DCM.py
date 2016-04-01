"""
Dirichlet compound multinomial model for textual documents.

Created on - 03/31/2016
@author - jverma
"""
import numpy as np



def generateSample(alpha_val, n):
	"""
	Generates a sample from DCM model.

	Parameters
	----------
	alpha : Parameter of Dirichlet distribution. 
	n : Size of the vector to be generated. 
	"""
	# create the alpha vector for Dirichlet dist.
	alpha = np.zeros(n)
	alpha.fill(alpha_val)

	# compute theta, a sample from Dirichlet dist.
	theta = np.random.dirichlet(alpha)

	# generate a sample from mult with theta as param.
	x = np.random.multinomial(100, theta)
	max_freq = np.max(x)
	return x/float(max_freq)


print generateSample(0.1, 100)


