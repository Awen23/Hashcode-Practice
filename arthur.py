import heapq as hq
import math
f = open("a_example.in", "r")

rows, cols, numVehicles, numRides, bonus, numSteps = [*map(int, f.readline().split())]
vehicles = []
rides = []
output = [[] for i in range(numVehicles)]

for x in range(0, numRides):
	rides.append([*map(int, f.readline().split()), x])

rides2 = rides.copy()



def dist(x1,y1,x2,y2):
	return abs(x1-x2) + abs(y1 - y2)

def out():
	for o in output:
		print(len(o), *o)

while rides:
	#time, carX, carY, vehI = hq.heappop(vehicles)
	toConsider = []
	while newTime < firstTime+numSteps*0.001:
		toConsider.append(hq.heappop(vehicles))
	for i in range(len(rides)):
		ride = rides[i]
		a, b, x, y, s, f, rideI = ride
		potentialEnd = time + dist(a, b, carX, carY) + dist(a, b, x, y)
		if f > potentialEnd:
			endTime = potentialEnd
			endI = i
			break
	hq.heappush(vehicles, [endTime, x, y, vehI])
	rides.pop(endI) # remove from list
	output[vehI].append(rideI)

out()

def score():
	score = 0
	for ride in output:
		time = x1 = y1 = 0
		for i in range(ride[0]):
			x2 = rides2[ride[i+1]][0]
			y2 = rides2[ride[i+1]][1]
			time+= dist(x1,y1,x2,y2)
			x1 = x2
			y1 = y2
			if time == rides2[ride[i+1][4]]:
				score+=bonus
			x2 = rides2[ride[i+1]][2]
			y2 = rides2[ride[i+1]][3]
			time += dist(x1,y1,x2,y2)
			if time < rides2[ride[i+1][5]]:
				score+= dist(x1,y1,x2,y2)
			x1 = x2
			y1 = y2
	print(score)