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

vehicles = [[0,0,0,i] for i in range(numVehicles)]

rides.sort(key=lambda x : x[4])

def dist(x1,y1,x2,y2):
	return abs(x1-x2) + abs(y1 - y2)

def out():
	for o in output:
		print(len(o), *o)

percentage = 0.5
numCheck = 0.5 * len(rides)
while rides:
	time, carX, carY, vehI = hq.heappop(vehicles)

	if len(rides) < numCheck:
		numCheck = len(rides)
	
	scores = []
	for i in range(numCheck):
		ride = rides[i]
		a, b, x, y, s, f, rideI = ride
		
		potentialEnd = time + dist(a, b, carX, carY) + dist(a, b, x, y)
		if f > potentialEnd:
			score = bonus + dist(a,b,x,y) - 2(dist(a, b, carX, carY)) - (s - (dist(a,b,x,y) + time))
			scores.append([score, i])
	hq.heappush(vehicles, [endTime, x, y, vehI])
	rides.pop(endI) # remove from list
	output[vehI].append(rideI)

out()

