# Text Comparison:

A comparison of speeches by the 2016 presidential candidates to other historical figures using a simple vector space model. 

## A Short Primer

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

The output of the above calculation, are vectors

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

## Usage:
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


