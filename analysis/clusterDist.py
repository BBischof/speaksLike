# Compares two clusterings and measures the distance between them as defined by the number of sibling points that no longer are siblings
import itertools
import math
C_1 = {1: [1,2,3], 2: [4]}
C_2 = {1: [1,2], 2: [3, 4]}
C_3 = {1: [1,2], 2: [3], 3: [4]}
Ugly = {1: ["apple","b"], 2: ["c"], 3: ["d"]}

# for dictionaries that may not be as trivial as our dictionary format, this removes the 
# names, and makes them simple integers
def makeClusteringLabelless(D):
	clusterDict = {}
	labelsDict = {}
	i = 1
	for k in D.keys():
		clusterDict[k] = []
		for item in D[k]:
			labelsDict[i] = item 
			clusterDict[k].append(i)
			i +=1
	return labelsDict, clusterDict


# Converts a partition of (1,...,n) indexed by a dictionary into an adjacency matrix
def buildClusterMatrix(D, size=-1):
	count = sum(len(v) for v in D.itervalues())
	A = []
	for i in range(count):
		A.append([0]*count)
	for k in D.keys():
		for p in list(itertools.combinations(D[k],2)):
			A[p[0]-1][p[1]-1]=1
			A[p[1]-1][p[0]-1]=1
	return A

#takes two adjacency matrices and computes the cluster distance between them
def clusterDist(x, y):
	if len(x) == len(y):
		diff = []
		for n in range(len(a)):
			diff.append(sum([math.fabs(i - j) for i, j in zip(x[n], y[n])]))
		return sum(diff)/2/len(x)
	else:
		return "mismatched size"

a = buildClusterMatrix(C_1) 
b = buildClusterMatrix(C_2)
c = buildClusterMatrix(C_3)

# print clusterDist(a,b)
# print clusterDist(a,c)
# print clusterDist(b,c)

print makeClusteringLabelless(Ugly)