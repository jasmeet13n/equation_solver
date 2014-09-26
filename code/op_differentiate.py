import eqparser
import copyTree

def diff(r):
	if r == None:
		return r;
	if r.leaf == '=':
		return 0
	if r.leaf == "diff":
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
			
		if len(root.children[0].children) == 0:
			if (root.children[0].leaf == variable):
				return eqparser.Node("INT",[],1)
			else:
				return eqparser.Node("INT",[],0)
		
		elif (root.children[0].leaf == '^'):
			if isinstance(root.children[0].children[1].leaf,int) or isinstance(root.children[0].children[1].leaf,float):
				newDiff1 = eqparser.Node(root.type,[],root.leaf)
				newDiff2 = copyTree.createTreeCopy(root.children[0].children[0])
				newDiff3 = eqparser.Node("VARIABLENAME",[],variable)
				newDiff1.children.append(newDiff2)
				newDiff1.children.append(newDiff3)
				
				power = root.children[0].children[1].leaf
				root.children[0].children[1].leaf = power -1
				newNode1 = eqparser.Node("BINARYOP",[],'*')
				newNode2 = eqparser.Node("INT",[],power)
				newNode1.children.append(newNode2)
				newNode1.children.append(root.children[0])
				newMul1 = eqparser.Node("BINARYOP",[],'*')
				newMul1.children.append(newNode1)
				newMul1.children.append(newDiff1)
				return newMul1
		
		elif (root.children[0].leaf == '*'):
			if isinstance(root.children[0].children[0].leaf,int) or isinstance(root.children[0].children[0].leaf,float):
				newRoot = root.children[0]
				tmp = root.children[0].children[1]
				root.children[0].children[1] = root
				root.children[0] = tmp
				return newRoot
			elif isinstance(root.children[0].children[1].leaf,int) or isinstance(root.children[0].children[1].leaf,float):
				newRoot = root.children[0]
				tmp = root.children[0].children[0]
				root.children[0].children[0] = root
				root.children[0] = tmp
				return newRoot
			else:
				newDiff1 = eqparser.Node(root.type,[],root.leaf)
				newDiff2 = copyTree.createTreeCopy(root.children[0].children[0])
				newDiff3 = eqparser.Node("VARIABLENAME",[],variable)
				newDiff1.children.append(newDiff2)
				newDiff1.children.append(newDiff3)
				
				newDiff4 = eqparser.Node(root.type,[],root.leaf)
				newDiff5 = copyTree.createTreeCopy(root.children[0].children[1])
				newDiff6 = eqparser.Node("VARIABLENAME",[],variable)
				newDiff4.children.append(newDiff5)
				newDiff4.children.append(newDiff6)
				
				newMul1 = eqparser.Node("BINARYOP",[],'*')
				newMul2 = eqparser.Node("BINARYOP",[],'*')
				
				newMul1.children.append(root.children[0].children[0])
				newMul1.children.append(newDiff4)
				
				newMul2.children.append(root.children[0].children[1])
				newMul2.children.append(newDiff1)
				
				newAdd = eqparser.Node("BINARYOP",[],'+')				
				newAdd.children.append(newMul1)
				newAdd.children.append(newMul2)
				return newAdd
				
		elif root.children[0].leaf == 'sin':
			newDiff1 = eqparser.Node(root.type,[],root.leaf) 
			newDiff2 = eqparser.Node("VARIABLENAME",[],variable)
			treeCopy = copyTree.createTreeCopy(root.children[0].children[0])
			newDiff1.children.append(treeCopy)
			newDiff1.children.append(treeCopy)
			
			newNode1 = eqparser.Node("BINARYOP",[],'*')
			root.children[0].leaf = 'cos'
			newNode1.children.append(root.children[0])
			newNode1.children.append(newDiff1)
			return newNode1
			
		elif root.children[0].leaf == 'cos':
			newDiff1 = eqparser.Node(root.type,[],root.leaf) 
			newDiff2 = eqparser.Node("VARIABLENAME",[],variable)
			treeCopy = copyTree.createTreeCopy(root.children[0].children[0])
			newDiff1.children.append(treeCopy)
			newDiff1.children.append(treeCopy)
			
			newNode1 = eqparser.Node("BINARYOP",[],'*')
			root.children[0].leaf = 'sin'

			newSub1 = eqparser.Node("BINARYOP",[],'-')
			newSub2 = eqparser.Node("INT",[],0)
			newSub1.children.append(newSub2)
			newSub1.children.append(root.children[0])
			
			newNode1.children.append(newSub1)
			newNode1.children.append(newDiff1)
			return newNode1
	return 0

if __name__ == "__main__":
	while 1:
		try:
			s = "diff(x*cos(x),x) = 0"   # use input() on Python 3
		except EOFError:
			print
			break
		root = eqparser.parse(s)
		newRoot =  diff(root.children[0])	
		print "Old Tree = " + repr(root)
		print str(root)
		print "New Tree = " + repr(newRoot)
		print str(newRoot)
		break
