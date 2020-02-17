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
	servers.append([*map(int, f.readline().split())])
	serverCap.append(servers[1])


servers.sort(key = lambda x:x[1], reverse = True)
servers.sort(key = lambda x:x[0])

servers_placed = [[] for _ in range(16)]
# [server, posInRow, pool]
row_info = [0]*16 # first slot available
row = 0
to_break = False
ps = [0]*16
for server in servers:
	size, capacity, i = server
	count_without_assign = 0
	if ps[row] < len(rows_blocked[row]):
		next_blocked = row_info[ps[row]]
	if row_info[row]+size > next_blocked
	while :
		count_without_assign += 1
		if count_without_assign > 16:
			to_break = True
			break
	if to_break:
		break
	row = (row+1)%16

i = 0
j = 0
poolnum = 0
for i in range(numServers-count_without_assign):
	
	if i < len(servers_placed):
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

def get_lowest(array: List[int]):
	minn = 9999999
	j = 0
	for i in range(len(array)):
		if minn > array[i]:
			minn = array[i]
			j = i
	return j

pools_assign = []
for i in range(pools):
	pools_assign.append([0,[0]*rows,0, i])

while num_servers_assigned > 0:
	curr = pools_assign.heappop()
	low = get_lowest(curr[1])
