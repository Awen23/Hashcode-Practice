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

i = 0
j = 0
poolnum = 0
for _ in range(num_servers_assigned):
	
	if i < len(servers_placed[j]):
		servers_placed[j][i][2] == poolnum
		i += 1
		poolnum += 1
	else:
		i == 0

	j += 1
	if j == rows:
		j == 0
	if poolnum == pools:
		poolnum == 0



print(servers_placed)