files = ['a.in', 'b.in', 'c.in', 'd.in', 'e.in']
for fileName in files:
	f = open(fileName, "r")



def writeToOut(fileName):
	f = open(fileName+'.out', "w+")
	# f.write()

	f.close()
	