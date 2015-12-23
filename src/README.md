Compare the GOP presidential candidate to other historical figures using a simple vector space model. 

**Input:**

- A text file containing the speeches for each candidate e.g. Trump.txt, Cruz.txt etc. All stored in a same directory. The path of the directory will be fed to the class as input argument.
- A text file containing the speeches of the person we want to compare to the candidates.
- We can also remove one from the list, and use that as query against others.

**Usage:**
```
from comparingSpeeches import GOPspeeches

results = GOPspeeches(input_directory)

print results.compare(query.txt)
```

**Requirements:**

- numpy
- scikit learn


**WARNING:** So far no tests have been performed. There may be some bugs in the code, let me know if something breaks.


