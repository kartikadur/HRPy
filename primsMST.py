# encoding : utf-8
from heapq import heappush, heappop

graph = {}
nodeList = []
edgeList = []

#input nodes and edges count
V,E = map(int, input().strip().split(" "))

#input edges in graph
for i in range(E):
    v1, v2, wt = map(int, input().strip().split(" "))
    #since the graph is undirected create mirror edges between all vertices
    if v1 in graph :
        graph[v1].append((wt, v2))
    else :
        graph[v1] = [(wt,v2)]
        
    if v2 in graph :
        graph[v2].append((wt, v1))
    else :
        graph[v2] = [(wt,v1)]

def prims(start):
    #print("start {}".format(start))
    nodeList = [i for i in range(1, V + 1)]
    sum = 0
    nodeList.remove(start)
    for i in graph[start]:
        heappush(edgeList, (i[0], start, i[1]))
    #processing all vertices
    while len(nodeList) > 0 :
        #print("edgeList {}".format(edgeList))
        wt, v1, v2 = heappop(edgeList)
        
        if v2 in nodeList :
            sum = sum + wt
            nodeList.remove(v2)
            for i in filter(lambda i: i[1] in nodeList, graph[v2]) :
                heappush(edgeList, (i[0], v2, i[1]))
        else :
            continue
    return sum

#get start node and run program
print(prims(int(input())))

'''
This program only calculates the minimum span of a given graph
It can be slightly modified to store edges to calculate path as well
Input 
5 6
1 2 3
1 3 4
4 2 6
5 2 2
2 3 5
3 5 7
1
Expected Output
15
'''
