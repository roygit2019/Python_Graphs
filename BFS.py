class Node:
	def __init__(self,name):
		self.n=name
		self.d=0
		self.p=None
r=Node("r")
v=Node("v")
s=Node("s")
w=Node("w")
t=Node("t")
x=Node("x")
u=Node("u")
y=Node("y")

gg={r:[v,s],v:[],s:[r,w],w:[s,t,x],t:[w,x,u],x:[w,t,u,y],u:[t,x,y,],y:[u,x]}
se=input("Enter the node to be searched\n")
Queue=list()
Visited=list()
d=0
Queue.append(s)
found=False

while len(Queue)!=0:
	cur=Queue.pop()
	if cur not in Visited:
		Visited.append(cur)
	for x in gg[cur]:
		if x not in Visited:
			x.p=cur
			x.d=cur.d+1
			if x.n==se:
				print("Node found in {} steps".format(x.d))
				found=True
				break
			Queue.append(x)
	if found==True:
		break
if found==False:
	print("Node not found")
	print("path of BFS:")
	for y in Visited:
		print(y.n)


