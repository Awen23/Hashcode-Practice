import heapq as hq
import math

f = open(input(), "r")

rows, cols, numVehicles, numRides, bonus, numSteps = [*map(int, f.readline().split())]
vehicles = []
rides = []
output = [[] for i in range(numVehicles)]
rides.sort(key = lambda x : x[4])
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

while rides:
	#time, carX, carY, vehI = hq.heappop(vehicles)
	toConsider = []
	vehi = hq.heappop(vehicles)
	firstTime = vehi[0]
	newTime = firstTime
	pushBack = True
	while newTime < firstTime+numSteps*0.001:
		toConsider.append(vehi)
		if len(vehicles) > 0:
			vehi = hq.heappop(vehicles)
			newTime = vehi[0]
		else:
			pushBack = False
			break
	if pushBack:
		hq.heappush(vehicles, vehi)
	ride = rides[0]
	a, b, x, y, s, f, rideI = ride
	carI = -1
	#endTime = 0
	# need to add some sort of wasted time counter thing
	lowesttimewasted = -1
	for car in toConsider:
		time, carX, carY, vehI = car
		# print("looking at car ", vehI)
		ridestarttime = time + dist(a, b, carX, carY)
		timewasted = s - ridestarttime
		if s == ridestarttime:
			endTime = ridestarttime + dist(a, b, x, y) #need to check
			carI = vehI
			break
		elif s >= ridestarttime and (timewasted < lowesttimewasted or lowesttimewasted == -1):
			endTime = ridestarttime + dist(a, b, x, y) #need to check
			carI = vehI
			lowesttimewasted = timewasted
	if carI == -1:
		for car in toConsider:
			time, carX, carY, vehI = car
			rideendtime = time + dist(a, b, carX, carY) + dist(a, b, x, y)
			if f > rideendtime:
				endTime = ridestarttime#need to check
				carI = vehI
				break
	rides.pop(0) # remove from list
	if carI != -1:
		hq.heappush(vehicles, [endTime, x, y, carI])
		
		output[carI].append(rideI)
		for car in toConsider:
			time, carX, carY, vehI = car
			if vehI != carI:
				hq.heappush(vehicles, [time, carX, carY, vehI])
				# print("hi2")
	else:
		for car in toConsider:
			time, carX, carY, vehI = car
			hq.heappush(vehicles, [time, carX, carY, vehI])
			# print("hi")
	# print(len(vehicles))


out()

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



#output = [[0],[2,1]]
score()