from collections import defaultdict
def printAllDuplicates(str):
	dm = defaultdict(lambda:0)
	for i in range(0,len(str),1):
		dm[str[i]]+=1
	for s in dm:
		if dm[s]>1:
			print(s," = ",dm[s])
str = input()
printAllDuplicates(str)