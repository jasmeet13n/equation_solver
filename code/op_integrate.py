import eqparser
import copyTree

def containsDiffInteg(root):
	#print root.leaf
	l = len(root.children)
	if l == 0:
		if root.leaf == 'diff' or root.leaf == 'integrate':
			return True
	if root.leaf == 'diff' or root.leaf == 'integrate':
		return True
	left = False
	if l>0:
		left = containsDiffInteg(root.children[0])
	right = False
	if l==2:
		right = containsDiffInteg(root.children[1])
	return left or right


def integrate(r):
	if r == None:
		return r;
	if r.leaf == '=':
		return 0
	if r.leaf == "integrate":
		#print repr(r)
		root = copyTree.createTreeCopy(r)
		variable = root.children[1].leaf
		if(root.children[0].leaf == '+' or root.children[0].leaf == '-'):
			newRoot = root.children[0]
			newNode1 = eqparser.Node(root.type,[],root.leaf)
			newNode2 = eqparser.Node("VARIABLENAME",[],variable)
			newNode1.children.append(root.children[0].children[1])
			newNode1.children.append(newNode2)
			tmp = root
			root.children[0] = tmp.children[0].children[0]
			newRoot.children[0] = root
			newRoot.children[1] = newNode1
			return newRoot
			
		elif len(root.children[0].children) == 0:
			if (root.children[0].leaf == variable):
				newNode1 = eqparser.Node("BINARYOP",[],'/')
				newNode2 = eqparser.Node("INT",[],2)
				
				newPow1 = eqparser.Node("BINARYOP",[],'^')
				newPow2 = eqparser.Node("INT",[],2)
				newPow1.children.append(root.children[0])
				newPow1.children.append(newPow2)
				
				newNode1.children.append(newPow1)
				newNode1.children.append(newNode2)
				return newNode1			
			elif root.children[0].leaf == 0:
				return eqparser.Node("INT",[],0)	
			else:
				newNode1 = eqparser.Node("BINARYOP",[],'*')
				newNode2 = eqparser.Node("VARIABLENAME",[],variable)
				newNode1.children.append(root.children[0])
				newNode1.children.append(newNode2)
				return newNode1
		
		elif (root.children[0].leaf == '^'):
			if (isinstance(root.children[0].children[1].leaf,int) or isinstance(root.children[0].children[1].leaf,float)) and root.children[0].children[0].leaf == variable:
				power = root.children[0].children[1].leaf
				newNode1 = eqparser.Node("BINARYOP",[],'/')
				newNode2 = eqparser.Node("INT",[],power+1)
				root.children[0].children[1].leaf = power+1
				newNode1.children.append(root.children[0])
				newNode1.children.append(newNode2)
				return newNode1
		
		elif (root.children[0].leaf == '*'):
			if root.children[0].children[0].leaf == 0:
				return eqparser.Node("INT",[],0)
			if root.children[0].children[0].leaf == 'diff' or root.children[0].children[0].leaf == 'integrage' or root.children[0].children[1].leaf == 'diff' or root.children[0].children[1].leaf == 'integrage':
				return 0
			if(containsDiffInteg(root.children[0]) == True):
				return 0
			if(containsDiffInteg(root.children[1]) == True):
				return 0
			newInteg1 = eqparser.Node(root.type,[],root.leaf)
			newInteg2 = copyTree.createTreeCopy(root.children[0].children[1])
			newInteg3 = eqparser.Node("VARIABLENAME",[],variable)
			newInteg1.children.append(newInteg2)
			newInteg1.children.append(newInteg3)
			
			newInteg1Copy = copyTree.createTreeCopy(newInteg1)
			
			newMul1 = eqparser.Node("BINARYOP",[],'*')
			newMul2 = eqparser.Node("BINARYOP",[],'*')
			
			newDiff1 = eqparser.Node("BINARYFUNCTION",[],'diff')
			newFirstCopy = copyTree.createTreeCopy(root.children[0].children[0])
			newDiff1.children.append(newFirstCopy)
			newDiff2 = eqparser.Node("VARIABLENAME",[],variable)
			newDiff1.children.append(newDiff2)
			
			newMul1.children.append(root.children[0].children[0])
			newMul1.children.append(newInteg1)
			
			newMul2.children.append(newDiff1)
			newMul2.children.append(newInteg1Copy)
			
			newInteg4 = eqparser.Node(root.type,[],root.leaf)
			newInteg6 = eqparser.Node("VARIABLENAME",[],variable)
			newInteg4.children.append(newMul2)
			newInteg4.children.append(newInteg6)
			
			newSub = eqparser.Node("BINARYOP",[],'-')				
			newSub.children.append(newMul1)
			newSub.children.append(newInteg4)
			return newSub
		elif root.children[0].leaf == '/':
			if isinstance(root.children[0].children[1].leaf,int) or isinstance(root.children[0].children[1].leaf,float):
				newRoot = root.children[0]
				tmp = root.children[0].children[0]
				root.children[0].children[0] = root
				root.children[0] = tmp
				return newRoot
				
		elif root.children[0].leaf == 'cos':
			if root.children[0].children[0].leaf == variable:			
				root.children[0].leaf = 'sin'
				return root.children[0]
			
		elif root.children[0].leaf == 'sin':
			if root.children[0].children[0].leaf == variable:			
				root.children[0].leaf = 'cos'

				newSub1 = eqparser.Node("BINARYOP",[],'-')
				newSub2 = eqparser.Node("INT",[],0)
				newSub1.children.append(newSub2)
				newSub1.children.append(root.children[0])		
				return newSub1
	return 0

if __name__ == "__main__":
	while 1:
		try:
			s = "(x+y)+(z*(z*sin(z)))*integrate(a,b) = 0"   # use input() on Python 3
		except EOFError:
			print
			break
		root = eqparser.parse(s)
		print containsDiffInteg(root)
		newRoot =  integrate(root.children[0])	
		print "Old Tree = " + repr(root)
		print str(root)
		print "New Tree = " + repr(newRoot)
		print str(newRoot)
		break

