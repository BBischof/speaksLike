"""
Dirichlet compound multinomial model for textual documents.

Created on - 03/31/2016
@author - jverma
"""
import numpy as np



def generateSample(alpha_val, n, avg_words_in_a_doc, avg_idf):
	"""
	Generates a sample from DCM model.

	Parameters
	----------
	alpha : Parameter of Dirichlet distribution. 
	n : Size of the vector to be generated. 
	avg_words_in_a_doc : Averge number of words in a document.
	avg_idf : The average value of IDF computed emperically for proper normalization.
	"""
	# create the alpha vector for Dirichlet dist.
	alpha = np.zeros(n)
	alpha.fill(alpha_val)

	# compute theta, a sample from Dirichlet dist.
	theta = np.random.dirichlet(alpha)

	# generate a sample from mult with theta as param.
	x = np.random.multinomial(avg_words_in_a_doc, theta)

	# normalize by the maximum value.
	max_freq = np.max(x)
	norm_tf = x/float(max_freq)

	# sample for tf-idf, multiply by the average IDF.
	tf_idf = norm_tf * float(avg_idf)
	return tf_idf 


print generateSample(0.1, 13000, 200, 0.01)


