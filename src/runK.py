#Main control script for K-means
from kMeansClustering import CandClusters
import sys
import glob
import operator
import json

#read from command line
if len(sys.argv) >= 2:
	args = sys.argv	
	transcripts = args[1]

results = CandClusters(transcripts)

output = results.cluster()

clusters = {}

#print output

for i in output:
	if i[1] in clusters.keys():
		clusters[i[1]][0] +=1
		clusters[i[1]][1].append(i[0])
	else:
		clusters[i[1]] = [1, [i[0]]]

#print clusters

print json.dumps(clusters, sort_keys=True, indent=4)