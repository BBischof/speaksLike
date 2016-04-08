"""
Dirichlet compound multinomial model for textual documents.

Created on - 03/31/2016
@author - jverma
"""
import numpy as np



def generateSample(alpha_val, n, avg_words_in_a_doc, var_words_in_a_doc, avg_idf, var_idf):
	"""
	Generates a sample from DCM model.

	Parameters
	----------
	alpha : Parameter of Dirichlet distribution. 
	n : Size of the vector to be generated. 
	avg_words_in_a_doc : Averge number of words in a document.
	var_words_in_a_doc : Variance of number of words in a document.
	avg_idf : The average value of IDF computed emperically for proper normalization.
	var_idf : Variance of the idf scores. 
	"""
	# create the alpha vector for Dirichlet dist.
	alpha = np.zeros(n)
	alpha.fill(alpha_val)

	# compute theta, a sample from Dirichlet dist.
	theta = np.random.dirichlet(alpha)

	# generate a sample from mult with theta as param.
	num_trials = int(np.random.normal(avg_words_in_a_doc, var_words_in_a_doc))
	x = np.random.multinomial(num_trials, theta)

	# normalize by the maximum value.
	max_freq = np.max(x)
	norm_tf = x/float(max_freq)

	# sample for tf-idf, multiply by the average IDF.
	idf_score = np.random.normal(avg_idf, var_idf)
	tf_idf = norm_tf * float(idf_score)
	return tf_idf 


print generateSample(0.1, 13000, 200, 50, 0.1, 0.001)


