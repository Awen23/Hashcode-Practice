 
f = open("dc.in", "r")

servers = []
serverCap = []
taken = []

rows, slots, unavailable, pools, numServers = [*map(int, f.readline().split())]

for x in range(0, unavailable):
	taken.append([*map(int, f.readline().split())])

for x in range(0, numServers):
	servers.append([*map(int, f.readline().split()), x])
	serverCap.append(servers[x][1])

servers.sort(key = lambda x:x[1], reverse = True)
servers.sort(key = lambda x:x[0])
servers2 = []

def score():
	sums = [0] * pools
	rows = [[0] * rows for x in range(pools)]


	for x in range(0, numServers):
		if len(servers2[x]) > 0:
			sums[servers2[x][1]] += serverCap[x]
			rows[servers2[x][1]][servers2[x][0]] += serverCap[x]


	gcList = []

	for x in range(0, pools):
		gcList.append(sums[x] - max(rows[x]))

	score = min(gcList)
	print(score)
