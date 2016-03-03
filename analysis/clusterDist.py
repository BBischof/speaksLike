# Compares two clusterings and measures the distance between them as defined by the number of sibling points that no longer are siblings
import itertools
import math
C_1 = {1: [1,2,3], 2: [4]}
C_2 = {1: [1,2], 2: [3, 4]}
C_3 = {1: [1,2], 2: [3], 3: [4]}

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

print clusterDist(a,b)
print clusterDist(a,c)
print clusterDist(b,c)