#import sys
import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import Normalizer
from sklearn.cluster import KMeans

class findk:
	def __init__(self, data, krange):
		"krange is the range of values for K you'd like to check"
		#self.data = "/home/lee/Data/allTranscripts"
		self.corpus = os.listdir(data)
		self.text = []
		for f in self.corpus:
			f = os.path.join(data, f)
			with open(f) as doc:
				contents = doc.read()
				self.text.append(contents)

		self.range = krange
		self.range.append(krange[len(krange)-1]+1)
		vectorizer = TfidfVectorizer(min_df=2, stop_words='english')
		self.X = vectorizer.fit_transform(self.text)
		
		


	def randomData(self, ref_size=10):
		
		sample=[]
		#the points live in [0,1]^n where n=number of columns, so we will find several random samples from that unit hypercube
		for g in range(ref_size):
			Xb = []
			for i in range(self.X.shape[0]):
				Xb.append([])
				for j in range(self.X.shape[1]):
					Xb[i].append(np.random.uniform(0,1))
			Xb = np.array(Xb)
			sample.append(Xb)
		
		return np.array(sample)


	def intraDist(self, labels, sample, k, centers):
		"labels is the output from KMeans.labels, sample is list of vectors with distance to ith cluster center for on each observation"
		"I think this actually just gives the inertia of the clustering..."
		"""Dk = np.zeros(k)
		#N = []
		for i in range(k):
			
			points = [c for c, j in enumerate(labels) if j==i]  
			#N.append(len(points))
			for pt in points:
				Dk[i] += sample[pt,i]**2

		return np.log(sum(Dk))"""

		Dk = np.zeros(k)
		for i in range(k):			
			points = [c for c,j in enumerate(labels) if j==i]
			Dk[i]= sum([np.linalg.norm(centers[i]-pt)**2/(2*len(points)) for pt in points])
		return np.log(sum(Dk))





	def gapstat(self, ref_size=10, max_iter=300, n_init=3):


		Wkestrand = np.zeros(len(self.range))
		Wk = np.zeros(len(self.range))
		sk = np.zeros(len(self.range))
		
		sample = self.randomData(ref_size)
		
		

		for indk, k in enumerate(self.range):
			km = KMeans(n_clusters=k, init='k-means++', max_iter=max_iter, n_init=n_init)
			Wkrand = []
			for i in range(ref_size):
				#Wkrand = []
				km.fit(sample[i])
				SS = km.transform(sample[i])
				Wkrand.append((self.intraDist(km.labels_.tolist(), sample[i], k, km.cluster_centers_)))

			Wkestrand[indk] = (1/ref_size)*sum(Wkrand)

			km.fit(self.X)
			XX = km.transform(self.X)
			clusters = km.labels_.tolist()
			Wk[indk] = self.intraDist(clusters, self.X, k, km.cluster_centers_)
			sk[indk] = np.sqrt((1/ref_size)*sum([(Wkrand[i]-Wkestrand[indk])**2 for i in range(ref_size)]))

		sk *= np.sqrt(1+1/ref_size)

		Gapk = [(1/ref_size)*Wkestrand[i]-Wk[i] for i in range(len(self.range))]


		#return min([k for k, j in enumerate([Gapk[g]-Gapk[g+1]+sk[g+1] for g in self.range[:,-1]]) if j>0 ])
		return [(k, Gapk[j], Gapk[j]-Gapk[j+1]+sk[j+1])for j, k in enumerate(self.range[:-1])]

