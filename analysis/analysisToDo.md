# Next steps for analysis in SpeaksLike

An overview of the analyses that need doing.

## K-means

Janu implemented a `K`-means script. And we have basic output with specific `K`'s. But no analysis of `K` and what these results mean.

### Cluster metrics

The primary metric for evaluating clusters
```
inter-cluster distance/intra-cluster diameter
```

### Naive Clustering (Speaker-Clustering)

This is the clustering defined by the candidates, i.e. any speech is in a cluster with another speech iff both speeches are by the same candidate. We would like to define a "distance" from our clustering to this clustering as a measure of success.

#### Auxilary Naive Clustering (RD-Clustering)

Clustering into `2` groups based on party.

### Elbow

(Lee)

Determine the ideal `K`. [example](https://datasciencelab.wordpress.com/2013/12/27/finding-the-k-in-k-means-clustering/)

### Analysis of clusters

We want to compare the clustering that we find to the naive clustering. We need to define a metric for this comparison. 

Given `s_i` a speech, and `C_j` a cluster then `s_i\in C_j` if `s_i` is a member of the cluster `C_j`, so for two speeches `s_a` and `s_b` should be 

```
D(s_a, s_b)=\delta_ij for s_a\in C_i, s_b\in C_j
```
then for two clusterings, `Cl_1` and `Cl_2`:
```
D(Cl_1, Cl_2)=(\sum_{a,b}^{I} |D^1(s_a, s_b)-D^2(s_a,s_b)|)/|I|
```

This is the percentage of the relationships that have changed.

#### Proof/Explanation

Notice that one can consider a clustering as a partition of the set of `n` data points. If we think of it this way, define the `adjacency matrix of a cluster` as the `nxn` binary matrix with ones in the `i,j`'th entry iff `i` and `j` are in the same partition component(for `i!=j`). For `C` a clustering call its adjacency matrix `A(C)`.

Then 

```
D(Cl_1, Cl_2)=|A(Cl_1)-A(Cl_2)|/2n
```

#### Write a py function to compute
(Done)

We naively represent partitions as dictionaries of lists, the `i`th partition component has key `i` and value equal to a list of contained points.

e.g.
```
C_1 = {1: [1,2,3], 2: [4]}
```

Then our functions to convert a clustering into a matrix.

```
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
```

and to compute the distance:

```
def clusterDist(x, y):
	if len(x) == len(y):
		diff = []
		for n in range(len(a)):
			diff.append(sum([math.fabs(i - j) for i, j in zip(x[n], y[n])]))
		return sum(diff)/2/len(x)
	else:
		return "mismatched size"
```

#### Changing number of clusters

This metric can handle mismatched number of clusters in our clusterings. One can think of the contribution to the distance of adding a point to a cluster as `x*y` where `x` is the number of points in the cluster it is leaving, `y` is the number of points in the cluster it is joining. So, a point breaking into it's own cluster is `x`. 

#### Examples of the distance
E.g.

```
Cl_1={1,2,3}, Cl_2={1,2,3}, such that 1_1={a,b}, 1_2={a}, 2_1={}, 2_2={b}, 3_1={c}, 3_2={c} 
```
then 

```
D(Cl_1, Cl_2)=1/3=.33
```

E.g. 2
```
Cl_1={1,2,3}, Cl_2={1,2}, such that 1_1={a,b}, 1_2={a,c}, 2_1={}, 2_2={b}, 3_1={c}
```
then 

```
D^1(a, b)=0, D^1(a, c)=1, D^1(c, b)=1, D^2(a, b)=1, D^2(a, c)=0, D^3(c, b)=1
```

```
D(Cl_1, Cl_2)=3/3=1
```

### Visualization

Fix dendro-gram. Find a better simple demonstration of the clusters. Maybe just draw the graph(janu will make this, also draw the trivial clusterings defined above). Maybe a sunburst(bryan has an idea)

## PCA

### Dimension reduction

(Janu)

The current dimensions in the vectors correspond to words in the speech. Even after PCA, the speeches are preserved, and the vectors live in new vector spaces. Clusters mean that speeches are similar. 

Ideally, points that are close, get much closer. Tend to reduce the inner-cluster diameter. 

The change from word-space to concept-space. Instead of looking strictly at word commonality, we are able to include the meaning of the words. Latent-semantic analysis is the name for PCA in NLP.

### PCA for vis of full dim K-means

(Afer Janu is done, bryan will make this)

Make the scatterplot with colors given by clusters.


### K-means + PCA

(after elbow method is written by Lee, apply that on Janu's PCA output)

`K`-means clustering after we run PCA.

We want to compare clustering before PCA and after. E.g. look at what speeches change clustering after PCA, and how that compares to naive clustering. Also want to compare ideal `K`.

### Visualization

(Bryan's code from above)

`2`-dimensional projection of the data after PCA, to see spatial comparison of speeches/cluster. 

## t-SNE

(Bryan will understand and try, Janu will post codes.)

### Dimension reduction

### K-means + t-SNE

### Visualization

## Sentiment analysis

(Bryan will run this as well)

### Sentiment as a filter

Once we have a clustering, we can look at the sentiment scores of each speech in that cluster, and we can "color" the point based on its sentiment. 

### Analysis on clusters

Determine the sentiment of a cluster as an average of the sentiments in that cluster. 

### Sentiment as a scalar

Instead of starting our entire analysis with speech vectors given by tf-idf values in each word dimensions, `v_w` the value of the vector at word `w` could be scaled by the sentiment score of `w`.

Let `sent_w` be the absolute value of the sentiment of the word `w`, and then scaled to the interval `[0,1]`. 

Currently:
```
s=I looked angry at Uncle Sam
v=<tf_idf_I, tf_idf_looked, tf_idf_angry, tf_idf_at, tf_idf_Uncle, tf_idf_Sam>
v^*= <sent_I * tf_idf_I, sent_looked * tf_idf_looked, sent_angry * tf_idf_angry, sent_at * tf_idf_at, sent_Uncle * tf_idf_Uncle, sent_Sam * tf_idf_Sam>
```

## Write up

(Bryan & Help)

Go viral! 