
# Heuristic Cost Function *****************************************************
def heuFunc1(root,v,h):
	if root == None:
		return 0
	val = 0
	x = root.leaf
	if x == v:
		val+=((h-1))
		val+=0
	else:
		val+=0
	for i in range(len(root.children)):
		val += heuFunc1(root.children[i],v,h+1)
	return val

def heuFunc2(root,v,h):
	if root == None:
		return 0
	val = 0
	x = root.leaf
	if x=='diff' or x=='integrate':
		val+=((h-1))+10
	elif x=='sin' or x=='cos':
		val+=2
	elif x == v:
		val+=((h-1))
		val+=1
	else:
		val+=2
	for i in range(len(root.children)):
		val += heuFunc2(root.children[i],v,h+1)
	return val
	
