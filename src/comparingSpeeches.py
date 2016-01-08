"""
Compare the speeches of presidential candidates.
@author - jverma
"""

import sys
import os
import numpy as np 
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import Normalizer


class candSpeeches:
	"""
	Implements the vector space model for computing the similarities of
	the speeches of the presidential candidates. 
	Each document will be represented by a vector in a very
	high dimensional vector space. The vectors have as entries the 
	tf-idf scores of the n-grams.
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


	def compare(self, query, min_df=2, LSA=False, n_comp=None):
		"""
		Compare the candidates speeches with a query e.g. Hitler or Ford.

		Parameters
		----------
		query: path to the textual document. e.g. hitler.txt
		min_df: only terms with document frequency greater than
				min_df will be considered. Default is 2.
		LSA: If True, the vectors will be mapped to a lower
			dimensional 'concept' space using Latend Semantic Analysis.
		n_comp: Number of components for the LSA, dimension of the concept space.


		Returns
		-------
		Speeches (documents) ranked accoring to the similarity to the query. 
		"""
		vectorizer = TfidfVectorizer(min_df=min_df, stop_words='english')
		X = vectorizer.fit_transform(self.text)
		X = X.toarray()

		#print sum([y != 0 for y in X[0]])

		queryData = open(query).read()
		queryData = [queryData]
		queryVector = vectorizer.transform(queryData)
		queryVector = queryVector.toarray()

		#print sum([y != 0 for y in queryVector])

		if (LSA):
			if (n_comp != None):
				lsa = TruncatedSVD(n_components=n_comp)
				X = lsa.fit_transform(X)
				X = Normalizer(copy=False).fit_transform(X)
				queryVector = lsa.transform(queryVector)

		ranking = cosine_similarity(X, queryVector)
		doc_id = np.argsort(ranking, axis=0)
		#print doc_id
		doc_id = doc_id[::-1]
		#print doc_id
		ranked_docs = [self.corpus[doc_id[i][0]] for i in range(len(self.corpus))]

		return ranked_docs
