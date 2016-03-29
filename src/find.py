from clusteringk import findk

path="/home/lee/Data/allTranscripts"
r=range(10,11)

test=findk(path,r)
ks = test.gapstat()

print ks