from clusteringk import findk

# path="/home/lee/Data/allTranscripts"
path="allTranscripts"
r=range(5,25)

test=findk(path,r)
ks = test.gapstat()

print ks