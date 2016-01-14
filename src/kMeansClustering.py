"""
Cluster the speeches of presidential candidates.
@author - jverma
"""

import sys
import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import Normalizer
from sklearn.cluster import KMeans


class CandClusters:
	"""
	Implements the k-means clustering for the speeches of
	the presidential candidates.
	Each document will be represented by a vector in a very high dimensional
	vector space. The vectors have as entries the tf-idf scores of the n-grams.
	K-Means algorithm is employed to extract clusters of the documents.
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


	def cluster(self, min_df=2, k=19, max_iter=300, n_init=1):
		"""
		CLusters the candidate speeches using k-means algorithm.

		Parameters
		----------
		min_df: only terms with document frequency greater than
				min_df will be considered. Default is 2.

		k: The number of clusters to form as well as the number of centroids to generate

		max_iter: Maximum number of iterations of the k-means algorithm for a single run.
				Default is 300.

		n_init: Number of time the k-means algorithm will be run with different centroid seeds. 
				The final results will be the best output of n_init 
				consecutive runs in terms of inertia. Default is 1.

		Returns
		-------
		Cluster index for each of the input documents.
		"""
		vectorizer = TfidfVectorizer(min_df=min_df, stop_words='english')
		X = vectorizer.fit_transform(self.text)

		km = KMeans(n_clusters=k, init='k-means++', max_iter=max_iter, n_init=n_init)
		km.fit(X)
		clusters = km.labels_.tolist()
		#return km.inertia_
		#return km.labels_
		#return clusters, self.corpus
		zippy = []
		for x,y in zip(self.corpus, clusters):
			zippy.append((x,y))
		return zippy




