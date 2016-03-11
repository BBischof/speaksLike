#Main control script
from comparingSpeeches import candSpeeches
import sys
import glob
import operator

#read from command line
if len(sys.argv) >= 2:
	args = sys.argv
	comparisonLocation = args[2]
	compareList = glob.glob(comparisonLocation + "*.txt")
	transcripts = args[1]

results = candSpeeches(transcripts)

#loop over comparison texts, compare to transcripts, append to list of rankings.
rankingsDict = {}
for text in compareList:
	output = results.compare(text)
	#i indicates ranking since transcripts are sorted by cosine similarity
	for i, transcript in enumerate(output):
		if transcript in rankingsDict.keys():
			rankingsDict[transcript].append(i+1)
		else:
			rankingsDict[transcript] = [i+1]

#print documents used for comparison
print "Texts compared to: "
for text in compareList:
	print text.split("/")[-1]
	

print "#######"
print "Ranked transcripts:"

#calculate average ratings
avgs = {}
for tran in rankingsDict.keys():
	avgs[tran] = float(sum(rankingsDict[tran]))/len(rankingsDict[tran])
#sort by avg rank and print
sorteda = sorted(avgs.items(), key=operator.itemgetter(1))
for x in sorteda:
	print "Doc: " + x[0][:-4] + ", AVG:" + str(x[1]) + ", List:" + str(rankingsDict[x[0]])

