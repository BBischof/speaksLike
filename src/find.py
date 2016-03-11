from clusteringk3 import findk

path="/home/lee/Data/allTranscripts"
r=range(10,25)

test=findk(path,r)
ks = test.gapstat()

print ks