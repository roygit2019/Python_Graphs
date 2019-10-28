class Node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None
		self.parent=None

def BST_insert(k,x,y):
	while x!=None:
		y=x
		if k.data<x.data:
			x=x.left
		else:
			x=x.right
	k.parent=y
	if k.data<y.data:
		y.left=k
	else:
		y.right=k

def BST_search(k,x):
	if x==None:
		return -1
	elif x.data==k:
		return (x.parent,x.left,x.right)
	else:
		if k<x.data:
			return BST_search(k,x.left)
		else:
			return BST_search(k,x.right)
	
roote=int(input("Enter the root node\n"))
root=Node(roote)
while True:
	a=int(input("Enter the node to be inserted.Enter -1 to quit\n"))
	if a==-1:
		break
	obj=Node(a)
	BST_insert(obj,root,None)
while True:
	a=int(input("Enter the node to be searched.Enter -1 to quit\n"))
	if a==-1:
		break
	ret=BST_search(a,root)
	if ret==-1:
		print("Node not found\n")
	else:
		print("Node found! {}\n".format(a))
		if ret[0]==None:
			print("Parent Node: Nill")
		else:
			print("Parent Node: {}".format(ret[0].data))
		if ret[1]==None:
			print("Left Child Node: Nill")
		else:
			print("Left Child Node: {}".format(ret[1].data))
		if ret[2]==None:
			print("Right Child Node: Nill")
		else:
			print("Right Child Node: {}".format(ret[2].data))


	



