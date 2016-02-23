# Principal Components Analysis (PCA)

## Philosophy

PCA is a statistical method for estimating the dimensionality of one's sample, as long as that dimension is less than or equal to the number of factors for which data has been recorded. So, often, it is described as a dimensionality reduction method. Colloquially, we group together factors which are highly correlated with one another into new variables which are uncorrelated and account for a monotonically decreasing proportion of variability in the data.

Caveat: new factors do not necessarily make sense, nor does PCA eliminate unuseful factors. More importantly, PCA should be done on data in which the measured factors have similar variability, otherwise the analysis will result in new factors in which the first principal component (the one accounting for the largest portion of variance in the data) will be dominated by the factors with highest variance. **This is likely going to be relevant to us**

## Method

There are two ways to perform a PCA which are essentially the same, modulo the starting point. We either start with the Variance-Covariance matrix of our data, or we start with the Correlation matrix. (These two methods correspond to the cases, respectively, where our factors are measured in similar units and generally have the same variability among samples, and the case where we have only one or neither of the previous.) 

After we have chosen the matrix on which to perform the PCA, we basically just find it's eigenvalues and eigenvectors. The eigenvector is used to define the new factor and calculate the 'principal component score' associated to that factor for each element of the sample, and the eigenvalue tells us how much of the variance in the sample this new factor accounts for. (we should be thinking of this as a change of basis, with the eigenvectors giving us the transition matrix)

## On our data

What do we forsee as problems applying this method to our data?