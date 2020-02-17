f = open("dc.in", "r")

servers = [] # [[physicalsize, capacity],...]
serverCap = []

taken = [] # [[rownum, slotnum],...]

rows, slots, unavailable, pools, numServers = [*map(int, f.readline().split())]
rows_blocked = [[] for _ in range(16)] # list of blocks per row sorted
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

class serverconfig:
	def __init__(self, config, score):
		# constructor
		self.config = config
		self.score = score

	def othermethod(self):
		#method
		return 0

seed = None
#pla