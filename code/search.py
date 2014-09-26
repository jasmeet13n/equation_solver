import eqparser
import copyTree
import heuristic
import printer
import op_inverse as inve
import op_arithmetic as arith
import op_commutative as comm
import op_associative as asso
import op_distributive as dist
import op_trigonometry as trig
import op_differentiate as diff
import op_integrate as integ

que = []
visited = {}
var = 'x'
simplify = 0

def search(root,v):
	global que
	global visited
	global var
	global simplify
	que = []
	visited = {}
	var = v
	simplify = 0
	distance = 0
	insertSorted(root,distance)
	visited[repr(root)] = True
	minTup = que[0]
	count = 0
	while count<5000:
		if len(que) == 0:
			break
		newTup = que.pop()
		distance = newTup[1]
		if(newTup[0] < minTup[0]):
			minTup = newTup
		if(minTup[0] == 0):
			break
		newRoot = newTup[3]
		recApplyOperators(newRoot,newRoot,newRoot,distance)
		count+=1
	print "Correct Solution    : ",printer.printer(minTup[3])
	#print "States Visited before Search Solution = ",count
	print "Simplifying ..."
	# Simplification Starts Here
	que = []
	visited = {}
	var = v
	simplify = 1
	distance = 0

	insertSorted(minTup[3],distance)
	visited[repr(minTup[3])] = True
	simTup = que[0]
	count = 0
	minCount = 1000;
	since = 0
	if integ.containsDiffInteg(minTup[3]):
		sinceMax = 5000
	else:
		sinceMax = 5000
	while count<5000:
		if len(que) == 0:
			break
		newTup = que.pop()
		distance = newTup[1]
		if(newTup[0] < simTup[0]):
			simTup = newTup
			minCount = count
			since = 0
		if(simTup[0] == 3):
			break
		if(since == sinceMax):
			#print "Simplified Solution : ", printer.printer(simTup[3])
			since = 0
			#break
		newRoot = newTup[3]
		recApplyOperators(newRoot,newRoot,newRoot,distance)
		count+=1
		since+=1
	
	print "Simplified Solution : ", printer.printer(simTup[3])
	#print "States visited before Simplified State = ",minCount
	return

def insertSorted(root,distance):
	heuVal = 0
	if simplify == 0:
		heuVal = heuristic.heuFunc1(root,var,0)
	else:
		heuVal = heuristic.heuFunc2(root,var,0)
	tup = [heuVal,distance,distance+heuVal,root]
	#print tup
	index = 0
	i=0
	l = len(que)
	for i in range(l+1):
		if i==l:
			break
		if simplify == 0:
			if que[i][2] <= tup[2]:
				break
		elif simplify == 1:
			if que[i][2] <= tup[2]:
				break
	index = i
	que.insert(index,tup)
	return
	

def enqu(root,parent,absRoot,newRoot,distance):
	if newRoot == None or newRoot == 0 or newRoot==root:
		return
	if root == parent:
		newStr = repr(newRoot)
		if newStr in visited:
			return
		else:
			insertSorted(newRoot,distance)
			visited[newStr] = True
	else:
		flag = 1
		if parent.children[0] == root:
			flag = 0
		parent.children[flag] = newRoot
		newStr = repr(absRoot)
		if newStr in visited:
			parent.children[flag] = root
			return
		else:
			copy = copyTree.createTreeCopy(absRoot)
			insertSorted(copy,distance)
			#print "Parent = ",repr(absRoot)
			visited[newStr] = True
			parent.children[flag] = root
		return
			
			
def applyAllOperators(root, parent, absRoot,distance):
	newRoot = arith.arith(root)
	enqu(root, parent, absRoot, newRoot,distance)

	newRoot = trig.trig(root)
	enqu(root, parent, absRoot, newRoot,distance)

	newRoot = diff.diff(root)
	enqu(root, parent, absRoot, newRoot,distance)

	newRoot = integ.integrate(root)
	enqu(root, parent, absRoot, newRoot,distance)

	if simplify == 0:
		newRoot = inve.lrFlip(root)
		enqu(root, parent, absRoot, newRoot,distance)
		
		newRoot = inve.rlFlip(root)
		enqu(root, parent, absRoot, newRoot,distance)

	newRoot = comm.comm(root)
	enqu(root, parent, absRoot, newRoot,distance)

	newRoot = asso.asso(root)
	enqu(root, parent, absRoot, newRoot,distance)

	newRoot = dist.dist(root)
	enqu(root, parent, absRoot, newRoot,distance)
	
	newRoot = dist.invDist(root)
	enqu(root, parent, absRoot, newRoot,distance)
	
	return

def recApplyOperators(root, parent, absRoot,distance):
	#print "reached again",repr(absRoot)
	if root == None:
		return
	applyAllOperators(root, parent, absRoot,distance+1)
	for i in range(len(root.children)):
		recApplyOperators(root.children[i], root, absRoot,distance)
	return


	
