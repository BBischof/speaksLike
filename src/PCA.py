"""
Dimensional Reduction of tf-idf vectors for candidate speeches.
@author - jverma
"""

import sys
import os
import numpy as np 
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import TruncatedSVD



class DimensionalReduction:
	"""
	Implements reduction models for candidate speeches.
	Uses Singular Valude Decompostion to perform PCA.
	"""
	def __init__(self, data):
		"""
		Parameters
		----------
		data: A directory containing the text of the speeches.
		e.g. a directory which has files as trump.txt, rubio.txt, cruz.txt etc.
		"""
		self.corpus = os.listdir(data)
		self.text = []
		for f in self.corpus:
			f = os.path.join(data, f)
			with open(f) as doc:
				contents = doc.read()
				self.text.append(contents)


	def principalComponentAnalysis(self, nComp=2):
		"""
		Computes the principal components for the vectors.

		Parameters
		----------
		nComp: Number of projection vectors. Dimension of the reduced space.
				Defualt is 2.

		Returns
		-------
		A numpy array of shape (n, nComp)
		"""
		model = decomposition.TruncatedSVD(n_components=nComp)
		return model.fit_transform(self.text)


