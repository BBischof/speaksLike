from comparingSpeeches import candSpeeches
import sys
import glob
import operator
#print sys.argv
if len(sys.argv) >= 2:
	args = sys.argv
	#print args[1]
	comparisonLocation = args[2]
	compareList = glob.glob(comparisonLocation + "*.txt")
	transcripts = args[1]

results = candSpeeches(transcripts)

rankingsDict = {}

#print comparisonLocation
for text in compareList:
	#print text
	output = results.compare(text)

	# hil=0
	# hilCount=0
	# tru=0
	# truCount=0

	for i, transcript in enumerate(output):
		if transcript in rankingsDict.keys():
			rankingsDict[transcript].append(i+1)
		else:
			rankingsDict[transcript] = [i+1]
	# 	if "hillary" in transcript:
	# 		hil += i
	# 		hilCount +=1
	# 	elif "donald" in transcript:
	# 		tru += i
	# 		truCount += 1
	#	print transcript, i
	#print rankingsDict

	#print "########################"

avgs = {}
for tran in rankingsDict.keys():
	avgs[tran] = float(sum(rankingsDict[tran]))/len(rankingsDict[tran])
sorteda = sorted(avgs.items(), key=operator.itemgetter(1))
for x in sorteda:
	print "Doc:" + x[0][:-4] + ", AVG:" + str(x[1]) + ", List:" + str(rankingsDict[x[0]])


#####
# write a loop to go over all the transcripts of hitler and avg rankings 
# maybe make it take a dir?
# also do fords 
# file name is wrong above. 

#print "hillary", hil/hilCount
#print "trump", tru/truCount