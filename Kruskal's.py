class Node:
	def __init__(self,nameofnode):
		self.name=nameofnode

a=Node("a")
b=Node("b")
c=Node("c")
d=Node("d")
e=Node("e")
f=Node("f")
g=Node("g")
h=Node("h")
i=Node("i")
edges=dict()
#given graph 
listofsets=list()
graph={a:[(b,4),(h,8)],b:[(h,11),(c,8)],c:[(i,2),(f,4),(d,7)],d:[(f,14),(e,9)],e:[(f,10)],f:[(g,2)],g:[(i,6),(h,1)],h:[(i,7)],i:[]}
for x in graph: #for forming the edges
	a=set()
	a.add(x)
	listofsets.append(a)
	neighbours=graph[x];
	for y in neighbours:
		edges[(x,y[0])]=y[1]
'''
for x in edges: #for displaying the edges
	v=edges[x]
	print(x[0].name+" "+x[1].name+" "+str(v))
'''
sortededges=sorted(edges.items(),key=lambda x:x[1])
print("============================")
cost=0
for y in sortededges: #For displaying the sorted edges
	p1=y[0]
	u=p1[0]
	v=p1[1]
	p2=y[1]	
	for i in range(len(listofsets)):
		if u in listofsets[i]:
			ii=i
			break
	for i in range(len(listofsets)):
		if v in listofsets[i]:
			jj=i
			break
	if ii==jj:
		continue
	else:
		listofsets[ii]=listofsets[ii]|listofsets[jj]
		listofsets[jj]=listofsets[ii]|listofsets[jj]
		cost+=p2
		print(u.name,v.name)
print("Minimum cost of the spanning tree: "+str(cost))







