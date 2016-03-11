# Rough project steps

- I wget-ed all the articles from 2015 into a directory,
- use find | grep | awk to create a list of paths to files, save list to var
- loop over list of files and use cat | grep | sed to parse the files output to new files
- loop over new files use cat to concatenate files with parts into single transcripts

## Bash Commands Run
- (note, this command needs slight modification to run now, some of the directory structure on whatthefolly has changed)
```bash
for j in $(seq -f "%02g" 12); do for i in $(seq -f "%02g" 31); do echo "http://www.whatthefolly.com/2015/$j/$i/" ; done; done | wget -r -np -nc -k -i -
```
- (now depricated in favor of the below)
```bash
find . -name "*html" -type f -exec ls -l {} \; | awk '{print $9}' | grep -v "/feed" | grep -v "page" | awk -F "/" '{print $5}'
```
- (now depricated in favor of the below)
```bash 
cat index.html | grep "<p>" | grep -v "Copyright" | grep -v "Category:" | grep -v "Log in" | grep -v "News Editor" | grep -v "span id" | grep -v ">…<" |  sed -e :a -e 's/<[^>]*>//g;/</N;//ba'
```
I ended up combining two and three into one script

## Extracting and scrubbing the html to make individual files
```bash
find . -name "*html" -type f -exec ls -l {} \; | awk '{print $9}' | grep -v "/feed" | grep -v "page" | awk -F "/" '($5 != "index.html")' | grep "transcript" | while read filename; do 
	name=`echo "$filename" | awk -F "/" '{print $5}'`
	echo "$name"
	cat "$filename" | grep "<p>" | grep -v "Copyright" | grep -v "Category:" | grep -v "Log in" | grep -v "News Editor" | grep -v "span id" | grep -v ">…<" |  sed -e :a -e 's/<[^>]*>//g;/</N;//ba' > "transcripts/${name}.txt"
done

```
(Note that `{print $5}' may not work depending on you personal directory structure. This should be modified to accomidate what is returned from the previous script. I'm too lazy to make all these commands more cohesive and extendible, but the basics are all here if someone wants to recreate this. Also, you could just grab the data from this repo...)
## Concatenating files that were broken into parts

```bash
find . -name "*txt" -type f -exec ls -l {} \; | grep "part" | grep -v "tax-scams" | grep -v "sunshine" | grep -v "pacific" | grep -v "state-department" | grep -v "d-c.txt" | awk '{print $9}' | while read filename; do
 name=`echo "${filename:2}" | awk -F "-" '{for (i=1; i<(NF-2); i++) printf $i "-"; print $(NF-2)}'`
 cat "$filename" >> "${name}.txt"
done
```

I then just removed all files that were previously made of parts.

## Putting Candidates into their own folders
```bash
for cand in "donald-trump" "carly-fiorina" "jeb-bush" "ben-carson" "chris-christie" "ted-cruz" "jim-gilmore" "lindsey-graham" "mike-huckabee" "john-kasich" "george-pataki" "rand-paul" "marco-rubio" "rick-santorum" "bernie-sanders" "hillary-clinton" "martin-omalley"
do
	mkdir ../${cand}
	cp `ls | grep "transcript-${cand}s"` ../${cand}/
done
```

## Analysis

We begin by using tf-idf to create similarity vectors between each speech and a comparison text in the directory. We sort these similarity values--most similar to least--and return the list. 

Next we iterate over all documents in the directory and generate these rankings for each. We average these rankings and return a sorted list(ascending) by similarity to the comparison texts.

## Output

A list of text documents from different candidates ranked by average tf-idf distance to a set of text documents from a directory.
