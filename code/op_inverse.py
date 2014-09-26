import eqparser
import copyTree

def lrFlip(r):
	if r == None:
		return r;
	if r.leaf != '=':
		return 0
	root = copyTree.createTreeCopy(r) 
	if(root.children[0].leaf == '+'):
		newNode = eqparser.Node("BINARYOP",[],'-')
		newNode.children.append(root.children[1])
		newNode.children.append(root.children[0].children[1])
		root.children[0] = root.children[0].children[0]
		root.children[1] = newNode
		return root
	elif(root.children[0].leaf == '-'):
		newNode = eqparser.Node("BINARYOP",[],'+')
		newNode.children.append(root.children[1])
		newNode.children.append(root.children[0].children[1])
		root.children[0] = root.children[0].children[0]
		root.children[1] = newNode
		return root
	elif(root.children[0].leaf == '*'):
		newNode = eqparser.Node("BINARYOP",[],'/')
		newNode.children.append(root.children[1])
		newNode.children.append(root.children[0].children[1])
		root.children[0] = root.children[0].children[0]
		root.children[1] = newNode
		return root
	elif(root.children[0].leaf == '/'):
		newNode = eqparser.Node("BINARYOP",[],'*')
		newNode.children.append(root.children[1])
		newNode.children.append(root.children[0].children[1])
		root.children[0] = root.children[0].children[0]
		root.children[1] = newNode
		return root
	elif(root.children[0].leaf == 'sqrt'):
		newNode = eqparser.Node("BINARYOP",[],'^')
		newNode.children.append(root.children[1])
		newNode2 = eqparser.Node("INT",[],2)	
		newNode.children.append(newNode2)
		root.children[0] = root.children[0].children[0]
		root.children[1] = newNode
		return root
	elif(root.children[0].leaf == '^'):
		if(root.children[0].children[0].leaf == 'e'):
			newNode = eqparser.Node("UNARYFUNCTION",[],'ln')
			newNode.children.append(root.children[1])
			root.children[1] = newNode
			root.children[0] = root.children[0].children[1]
			return root
		elif(root.children[0].children[0].leaf == 2):
			newNode = eqparser.Node("UNARYFUNCTION",[],'log')
			newNode.children.append(root.children[1])
			root.children[1] = newNode
			root.children[0] = root.children[0].children[1]
			return root
		elif(root.children[0].children[1].leaf == 2):
			newNode = eqparser.Node("UNARYFUNCTION",[],'sqrt')
			newNode.children.append(root.children[1])
			root.children[1] = newNode
			root.children[0] = root.children[0].children[0]
			return root
		else:
			newNode = eqparser.Node("BINARYOP",[],'^')
			newNode2 = eqparser.Node("INT",[],1)	
			newNode3 = eqparser.Node("BINARYOP",[],'/')
			newNode3.children.append(newNode2)
			newNode3.children.append(root.children[0].children[1])
			newNode.children.append(root.children[1])
			newNode.children.append(newNode3)
			root.children[0] = root.children[0].children[0]
			root.children[1] = newNode
			return root
	return 0

def rlFlip(r):
	if r == None:
		return r;
	if r.leaf != '=':
		return 0
	root = copyTree.createTreeCopy(r)
	tmp = root.children[0]
	root.children[0] = root.children[1]
	root.children[1] = tmp
	newRoot = lrFlip(root)
	if newRoot == None or newRoot == 0 or newRoot == root:
		return 0
	tmp = newRoot.children[0]
	newRoot.children[0] = newRoot.children[1]
	newRoot.children[1] = tmp
	return newRoot
	
		

# Main Function ****************************************************************
if __name__ == "__main__":
	while 1:
		try:
			s = raw_input('eq > ')   # use input() on Python 3
		except EOFError:
			print
			break
		root = eqparser.parse(s)
		newRoot =  rlFlip(root)	
		print "Old Tree = " + repr(root)
		print str(root)
		print "New Tree = " + repr(newRoot)
		print str(newRoot)
	
