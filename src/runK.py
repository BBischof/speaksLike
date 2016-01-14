#Main control script for K-means
from kMeansClustering import CandClusters
import sys
import glob
import operator

#read from command line
if len(sys.argv) >= 2:
	args = sys.argv	
	transcripts = args[1]

results = CandClusters(transcripts)

output = results.cluster()

clusters = {}

print output

for i in output:
	if i in clusters.keys():
		clusters[i] +=1
	else:
		clusters[i] = 1

print clusters