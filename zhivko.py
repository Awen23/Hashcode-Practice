import heapq, random
maxSc = 0
while True:
	f = open("dc.in", "r")

	servers = []
	serverCap = []

	taken = []

	rows, slots, unavailable, pools, numServers = [*map(int, f.readline().split())]
	rows_blocked = [[] for _ in range(16)]
	for x in range(0, unavailable):
		val = [*map(int, f.readline().split())]
		taken.append(val)
		r, c = val
		rows_blocked[r].append(c)
	for thingy in rows_blocked:
		thingy.sort()
	for x in range(0, numServers):
		servers.append([*map(int, f.readline().split()), x])
		serverCap.append(servers[x][1])


	servers.sort(key = lambda x:x[1], reverse = True)
	servers.sort(key = lambda x:x[0])

	servers_placed = [[] for _ in range(16)]
	# [server, posInRow, pool]

	row_info = [0]*16 # first slot available
	row = 0
	to_break = False
	ps = [0]*16
	num_servers_assigned = 0
	for server in servers:
		size, capacity, i = server
		count_without_assign = 0
		if ps[row] < len(rows_blocked[row]):
			next_blocked = row_info[ps[row]]
		else:
			next_blocked = float('inf')
		while row_info[row]+size > next_blocked:
			row_info[row] = next_blocked+1
			ps[row] += 1
			if ps[row] < len(rows_blocked[row]):
				next_blocked = row_info[ps[row]]
			else:
				next_blocked = float('inf')
		while row_info[row]+size >= slots:
			row = (row+1)%16
			count_without_assign += 1
			if count_without_assign > 16:
				to_break = True
				break
			if ps[row] < len(rows_blocked[row]):
				next_blocked = row_info[ps[row]]
			else:
				next_blocked = float('inf')
			while row_info[row]+size > next_blocked:
				row_info[row] = next_blocked+1
				ps[row] += 1
				if ps[row] < len(rows_blocked[row]):
					next_blocked = row_info[ps[row]]
				else:
					next_blocked = float('inf')
		if to_break:
			break
		servers_placed[row].append([i, row_info[row], None])
		row_info[row] = row_info[row]+size
		row = (row+1)%16
		num_servers_assigned += 1

	def score():

		sums = [0] * pools
		rows2 = [[0] * rows for x in range(pools)]


		for x in range(0, numServers):
			if len(servers2[x]) > 0:
				sums[servers2[x][1]] += serverCap[x]
				rows2[servers2[x][1]][servers2[x][0]] += serverCap[x]

		gcList = []

		for x in range(0, pools):
			gcList.append(sums[x] - max(rows2[x]))

		score = min(gcList)
		
		# print(score)
		return score




	# NEW CODE FROM HERE
	def get_lowest(array):
		minn = 9999999
		j = 0
		for i in range(len(array)):
			if minn > array[i] and servers_assign[i]:
				minn = array[i]
				j = i
		return j

	servers_assign = servers_placed.copy()
	pools_assign = []
	servers2 = [[] for _ in range(numServers)]

	for i in range(pools):
		pools_assign.append([0,[0]*rows,0, i])

	#print("done")												

	while num_servers_assigned > 0:
		curr = heapq.heappop(pools_assign)
		low = get_lowest(curr[1])
		#print(num_servers_assigned)
		
		#???first not random
		
		rand = random.randrange(0,len(servers_assign[low]))

		server = servers_assign[low][rand][0]
		new = curr[1][low] + serverCap[server]
		curr[1][low] = new
		
		servers2[server] = [low, curr[3]]
		
		if new > curr[1][curr[2]]:
			curr[0] -= curr[1][curr[2]]
			curr[0] += new
			curr[2] = low
		else:
			curr[0] += serverCap[server]
			
		servers_assign[low].pop(rand)
		num_servers_assigned-=1
		heapq.heappush(pools_assign,curr)
		
		#print(servers2)
	sc = score()
	if sc > maxSc:
		maxSc = sc
	print(sc, maxSc)