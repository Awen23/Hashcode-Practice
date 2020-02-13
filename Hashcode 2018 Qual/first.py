import heapq as hq
import math
f = open("b_should_be_easy.in", "r")

rows, cols, numVehicles, numRides, bonus, numSteps = [*map(int, f.readline().split())]
vehicles = []
rides = []
output = [[] for i in range(numVehicles)]

for x in range(0, numRides):
	rides.append([*map(int, f.readline().split()), x])

rides2 = rides.copy()

rides.sort(key = lambda x : x[4])
vehicles = [[0, 0, 0, i] for i in range(numVehicles)]

def dist(x1,y1,x2,y2):
	return abs(x1-x2) + abs(y1 - y2)

def out():
	for o in output:
		print(len(o), *o)

while rides and vehicles:
	time, carX, carY, vehI = hq.heappop(vehicles)
	for i in range(len(rides)):
		endI = -1
		ride = rides[i]
		a, b, x, y, s, f, rideI = ride
		potentialEnd = time + dist(a, b, carX, carY) + dist(a, b, x, y)
		if potentialEnd < f:
			endTime = potentialEnd
			endI = i
			break
	if endI != -1:
    
		hq.heappush(vehicles, [endTime, x, y, vehI])
		output[vehI].append(rideI)
		rides.pop(endI) # remove from list


def score():
	score = 0
	for ride in output:
		#print(ride)
		time = x1 = y1 = 0
		for i in range(len(ride)):
			x2 = rides2[ride[i]][0]
			y2 = rides2[ride[i]][1]
			time+= dist(x1,y1,x2,y2)
			x1 = x2
			y1 = y2
			if time <= rides2[ride[i]][4]:
				score+=bonus
				#print(score)
			x2 = rides2[ride[i]][2]
			y2 = rides2[ride[i]][3]
			time += dist(x1,y1,x2,y2)
			time = max(time,rides2[ride[i]][4]+dist(x1,y1,x2,y2))
			if time < rides2[ride[i]][5]:
				score += dist(x1,y1,x2,y2)
				#print(score)
			x1 = x2
			y1 = y2
	print(score)

out()
#output = [[0],[2,1]]
score()
