import heapq as hq
import math
f = open("c_no_hurry.in", "r")

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

percentage = 1
numCheck = math.ceil(percentage * len(rides))
while rides:
	#print("\n\nRides at start is ", rides)
	#print("Vehicles at start is ", vehicles)
	if len(vehicles) > 0:
		time, carX, carY, vehI = hq.heappop(vehicles)
	else:
		break

	if len(rides) < numCheck:
		numCheck = len(rides)
	
	minScore = [9999999999999, -1, -1, -1, -1, -1]
	minPotentialEnd = 99999999999999999
	for i in range(numCheck):
		ride = rides[i]
		a, b, x, y, s, f, rideI = ride
		
		potentialEnd = time + dist(a, b, carX, carY) + dist(a, b, x, y)
		#print("f is {}, potentialEnd is {}".format(f,potentialEnd))
		if potentialEnd < minPotentialEnd:
			minPotentialEnd = potentialEnd
		if f > potentialEnd:
			score = bonus + dist(a,b,x,y) - 2*(dist(a, b, carX, carY)) - (s - (dist(a,b,carX,carY) + time))
			if score < minScore[0]:
				minScore = [score, i, rideI, potentialEnd, x, y]
				#print("minScore is ", minScore)
		
	if(minScore[1] != -1):
		#print("Assigned ", minScore[2]);
		endTime = time + minScore[3]
		x = minScore[4]
		y = minScore[5]
		hq.heappush(vehicles, [endTime, x, y, vehI])
		rides.pop(minScore[1]) # remove from list
		output[vehI].append(minScore[2])
	else:
		if minPotentialEnd < numSteps:
			hq.heappush(vehicles, [minPotentialEnd, carX, carY, vehI])

	
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