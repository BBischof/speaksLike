"""
Emperical computation of average IDF. 
"""
import os
import numpy as np 
import matplotlib.pyplot as plt




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



	def computeNumberOfWordsAndIDF(self):
		"""
		Computes the IDF scores of words and the number of words in documents.
		These results can be used for plotting.

		Returns
		-------
		A dictionary containing number of words in documents,  and average IDF of words.
		{"number_of_words": number of words, "idf": idf values}
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

		res_data = {"number_of_words": number_of_words, "idf": idf_vec}
		return res_data




	def computeAvergeNumberOfWordsAndIDF(self):
		"""
		Computes averge IDF and averge number of words in a document.
		This information will be used in computation of the DCM model.

		Returns
		-------
		[(Average number of words in a doc, variance), (Average IDF score of a word, variance)]
		"""
		out = self.computeNumberOfWordsAndIDF()
		number_of_words = out['number_of_words']
		idf_vec = out['idf']

		return [(np.mean(number_of_words), np.var(number_of_words)), (np.mean(idf_vec), np.var(idf_vec))]


# s = np.random.normal(0,0.1, 1000))
# count, bins, ignored = plt.hist(s, 30, normed=True)
# plt.plot(bins, 1/(0.1 * np.sqrt(2 * np.pi)) *
# 		np.exp( - (bins - 0)**2 / (2 * 0.1**2) ),
# 		linewidth=2, color='r')
# plt.show()








