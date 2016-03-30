
# Gap statistic and implementation
## [Reference](https://datasciencelab.wordpress.com/2013/12/27/finding-the-k-in-k-means-clustering/)
## Basics
 * The gap statistic compares the clustering on the sample data to the clustering on a collection of randomly generated samples from a distribution with no clusters (to average)
 * If the gap statistic for a certain k is positive, then the clustering produces a larger intra-cluster distance on the generated data than it does on the actual sample data. i.e. the clusters in your sample data are more tightly packed than in the random data.

## clusteringk.py implementation

The class is divided into three parts, essentially:
 0. initialization: *krange* = list of clusters you want to compare via gap statistics
 1. randomData
  obviously, the random samples are generated here. they are generated from a uniform distribution to produce samples that are the same size as the sample data.
 2. intraDist  
  we will say intraDist returns **W_k**
  requires:
   * labels: a tuple s.t. if k=lables[i] then the ith observation is in the kth cluster
   * k: number of clusters
   * centers: a list of points corresponding the center of each cluster
  for each cluster a list (*points*) is made containing the index of each observation in the cluster, and then the distance from each point in the cluster to that cluster's center is calculated. They're then all summed and sort of averaged and transformed into it's logrithmic value.

 3. gapstat
  mostly just applies the the previous two functions, but is the most confusing. 
  definitions:
   - ref_size is the number of random samples generated
   - Wkestrand is a list of averaged **W_k** values calculated on a clustering of the randomly generated data for each k in *krange*.
   - Wk is a list of **W_k** values calculated on a clustering of the sample data for each k in *krange*
   - sk is a list of (what are essentially) standard deviations for the randomly generated data

  the loops fill up the lists defined above, with the inner loop taking care of the randomly generated samples. note that for each k we must re-initialize the function KMeans from sklearn. 