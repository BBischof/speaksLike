"""
Emperical computation of average IDF. 
"""
import os
import numpy as np 




class InverseDocFreq:
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



	def computeAverageIDF(self):
		"""
		Computes the averge IDF and the average number of words in a document.

		Returns
		-------
		[Average number of words, average IDF]
		"""
		vectorizer = TfidfVectorizer(min_df=min_df, stop_words='english')
		X = vectorizer.fit_transform(self.text)
		X = X.toarray()

		n,m = X.shape()
		idf_vec = []
		for i in range(m-1):
			colmn = X[:,i:i+1]
			df = np.count_nonzero(colmn)
			idf = (n/float(df)) + 1.0
			idf = np.log2(idf)
			idf_vec.append(idf)

		number_of_words = []
		for j in range(n):
			rw = X[i]
			words_in_rw = np.count_nonzero(rw)
			number_of_words.append(words_in_rw)

		return [np.mean(number_of_words), np.mean(idf_vec)]









