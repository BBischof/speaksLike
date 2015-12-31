from comparingSpeeches import candSpeeches

results = candSpeeches("allTranscripts")

output = results.compare("hitler/mein-kampf.txt")
hil=0
hilCount=0
tru=0
truCount=0

for i, transcript in enumerate(output):
	if "hillary" in transcript:
		hil += i
		hilCount +=1
	elif "donald" in transcript:
		tru += i
		truCount += 1
	print transcript, i

#print "hillary", hil/hilCount
#print "trump", tru/truCount