# Text Comparison:

A comparison of speeches by the 2016 presidential candidates to other historical figures using a simple vector space model. 

## A Short Primer to TF-IDF

TF-IDF is a method for weighting words in a corpus of documents based on frequency in one document vs infrequency in the entire corpus. As a simple example, one can imagine a corpus of two documents, such that "alpha" appears only in the first document, and "beta" appears only in the second. Then, one would expect alpha to be reflective of the content of the first document and distinguishing from the second. However, as the size of document grows, and the number of appearances of alpha becomes relatively insubstantial in document one, we become less convinced that alpha is reflective of the content of document one. 

Define a function
```
TF(document, word) := (number of appearance of word in document)
```

and similarly
```
IDF(corpus, word) := (number of documents in corpus)/(number of documents in corpus containing word)
```

it's customary to use a logarithmic scale for IDF to normalize the length of these vectors, whence
```
IDF_n:=log_2(IDF).
```

The output of the above calculation, are vectors. To rank by similarity, we use cosine similarity between a comparison text and each of the vectors produced above. The transcripts are then ranked based on this cosine similarity to provide an ordered list of the most to least similar documents to the comparison text.

## K-means clustering

Simply ranking the documents by TF-IDF cosine similarity is fairly primitive. It says nothing about the aggregate similarity of a candidate's rhetoric to the archive of comparison texts. To look at them simultaneously, one can use K-means clustering. One can think of this as asking "can we group documents by how similar they all are to one another?" One would expect that each candidate would have their own cluster, and so would the archive of comparison texts(corresponding to the person being compared to.) Additionally, one would expect the distance between clusters to indicate the similarity of candidates rhetoric. Again, we rely on TF-IDF to provide us with a distance function.

To determine K we rely on two statistics and a comparison between them:
- Gap Statistic 
- Pham Et. Al. [Ref](https://datasciencelab.wordpress.com/2014/01/21/selection-of-k-in-k-means-clustering-reloaded/)

The purpose of these statistics is to provide a guide for selecting the number of clusters for our analysis. In this case, the clusters will be the groupings of speeches. One might expect that given 19 speakers, we would want k=19. While this makes intuitive sense, it is a bit naive. To provide any real assessment of the candidate's "similarity to Hitler" we would expect that as the number of clusters decreases, one--or a few--candidates speeches overwhelmingly cluster together with Hitler's.

## Principle Component Analysis

Because of the high dimensionality of our representations(TF-IDF is extremely high dimensional), we have interest in dimensional reduction. One strategy for this is PCA. By utilizing PCA, we can project our high dimensional vectors onto a plane(2-dimensional subspace) which most accurately represents the variability in the data set. 

With the lower dimensional representations, we have two advantages:
- ability to visualize
- potential for more concentrated datapoints

High dimensional data is notorious for providing misleading clustering results(cf. curse of dimensionality), so we may see more defined clusters by utilizing K-means after PCA. Additionally, by projecting to two or three dimensions, we can plot the data points so that we can attempt to manually inspect the relationships.

## Input:

```
input_directory
```
- A directory containing text files of a given candidate

```
benchmark.txt
```
- A text file containing a single corpus of words to which we compare the files contained in the input_directory.


Note that we can also remove a document from input_directory and pass that as our benchmark.txt argument for purpose of self-similarity measurement.

## Output:

A sorted list of speeches and their rankings in tf-idf distance to the set of comparison texts.

Output format is a list of texts included as comparison texts, followed by a list of lines where each line corresponds to an article, it's average ranking of comparison to the comparison texts, and the individual rankings to each comparison text.

## Usage:
Usage of run.py:
```
python run.py name-of-directory-containing-speeches name-of-directory-containing-comparison-texts
```

Usage of comparingSpeeches:
```
from comparingSpeeches import candSpeeches

results = candSpeeches("input_directory")

print results.compare("benchmark.txt")
```

## Requirements:

The following python packages are required:

- numpy
- scikit learn


## WARNING: 

This code is in development, and thus, not fully functioning yet. This disclaimer will be removed when this code is considered to be functional, with unit testing.


