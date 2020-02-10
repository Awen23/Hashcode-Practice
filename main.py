import heapq as hq
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

while rides:
	time, carX, carY, vehI = hq.heappop(vehicles)
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
	for ride in output:
		time = x = y = 0
		for i in range(ride[0]):
			dist = dist(x,y,rides2[ride[i]][2],rides2[ride[i]][3])
			