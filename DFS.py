class Node:
 	def __init__(self,name):
 		self.name=name
 		self.colour="white"
 		self.p=None
u=Node("u")
v=Node("v")
w=Node("w")
x=Node("x")
y=Node("y")
z=Node("z")

graph={u:[v,x],v:[y],w:[y,z],x:[v],y:[x],z:[z]}

def dfs(node):
	node.colour="grey" #add search element check with appropriate distance attirbute in Node class, if required.
	for i in graph[node]:
		if i.colour=="white":
			i.p=node
			dfs(i)
	node.colour="black"
	print(node.name)
for x in graph:
	if x.colour=="white":
		dfs(x)


