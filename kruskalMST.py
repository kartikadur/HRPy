parent = {}
rank = {}

edges = []
nodes = []

sumWt = 0
numSets = 0

# Disjoint set code, setup for Kruskal's algo
def make(v):
	parent[v] = v
	rank[v] = 0

def find(v):
	if parent[v] != v:
		parent[v] = find(parent[v])
	return parent[v]

def union(v1, v2):
	root1 = find(v1)
	root2 = find(v2)

	# root1 == root : do nothing
	
	# root1 != root2
	if root1 != root2:
		# root1.rank > root2.rank : root2.parent = root1
		if rank[root1] < rank[root2]:
			parent[root1] = root2
		# root2.rank > root1.rank : root1.parent = root2
		else :
			parent[root2] = root1
			# root1.rank == root2.rank : root1.rank = root2.rank + 1	
			if rank[root1] == rank[root2]:
				rank[root1] = rank[root2] + 1
		return True
	return False
	


# get input
V, E = map(int, input().strip().split(" "))

for node in range(1, V + 1):
	make(node)
numSets = V

for edge in range(E):
	v1, v2, wt = map(int, input().strip().split(" "))
	edges.append((wt, v1, v2))

	edges.sort()

# Kruskal's code
for wt, v1, v2 in edges:
	if union(v1, v2) and numSets > 1 :
		sumWt += wt
		numSets -= 1

print(sumWt)

'''
Input
4 6
1 2 5
1 3 3
4 1 6
2 4 7
3 2 4
3 4 5
1

Output
12
'''