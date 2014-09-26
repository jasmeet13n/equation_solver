import eqparser
import copyTree
import equalTree

def dist(root):
	if root == None:
		return root
	if root.leaf == '=':
		return 0
	if root.leaf == '*':
		if root.children[0].leaf == '+' or root.children[0].leaf == '-':		
			if root.children[0].children[0].leaf !=0 and root.children[0].children[1].leaf!=0:
				newTree = copyTree.createTreeCopy(root)
				newNode1 = eqparser.Node(root.children[0].type,[],root.children[0].leaf)
				newNode2 = copyTree.createTreeCopy(root.children[1])
				tmp1 = newTree.children[0]
				tmp1.leaf = '*'
				tmp2 = tmp1.children[1]
				tmp1.children[1] = newNode2
				newNode1.children.append(tmp1)
				newTree.children[0] = tmp2
				newNode1.children.append(newTree)
				return newNode1
		elif root.children[1].leaf == '+' or root.children[1].leaf == '-':
			if root.children[1].children[0].leaf !=0 and root.children[1].children[1].leaf!=0:		
				newTree = copyTree.createTreeCopy(root)
				newNode1 = eqparser.Node(root.children[1].type,[],root.children[1].leaf)
				newNode2 = copyTree.createTreeCopy(root.children[0])
				tmp1 = newTree.children[1]
				tmp1.leaf = '*'
				tmp2 = tmp1.children[0]
				tmp1.children[0] = newNode2
				newTree.children[1] = tmp2
				newNode1.children.append(newTree)
				newNode1.children.append(tmp1)
				return newNode1
	elif root.leaf == '/' and root.children[1].leaf !=0:
		if root.children[0].leaf == '+' or root.children[0].leaf == '-':		
			newTree = copyTree.createTreeCopy(root)
			newNode1 = eqparser.Node(root.children[0].type,[],root.children[0].leaf)
			newNode2 = copyTree.createTreeCopy(root.children[1])
			tmp1 = newTree.children[0]
			tmp1.leaf = '/'
			tmp2 = tmp1.children[1]
			tmp1.children[1] = newNode2
			newNode1.children.append(tmp1)
			newTree.children[0] = tmp2
			newNode1.children.append(newTree)
			return newNode1
	return 0
	
def invDist(r):
	if r == None:
		return root;
	if r.leaf == '=':
		return 0
	#print "here"
	if r.leaf == '+' or r.leaf == '-':
		if (r.children[0].leaf == '*' or r.children[0].leaf == '/') and (r.children[1].leaf == '*' or r.children[1].leaf == '/'):			
			root = copyTree.createTreeCopy(r)
			a = root.children[0]
			b = root.children[1]
			numA = len(a.children)
			numB = len(b.children)
			if numA == 0:
				if a.leaf == b.children[0].leaf:
					newNode1 = eqparser.Node("BINARYOP",[],'*')
					newNode2 = eqparser.Node(a.type,[],a.leaf)
					newNode1.children.append(newNode2)
					newNode1.children.append(root)
					root.children[0] = eqparser.Node("INT",[],1)
					root.children[1].children[0] = eqparser.Node("INT",[],1)
					return newNode1
				elif numB==2 and a.leaf == b.children[1].leaf and b.leaf!='/':
					newNode1 = eqparser.Node("BINARYOP",[],'*')
					newNode2 = eqparser.Node(a.type,[],a.leaf)
					newNode1.children.append(newNode2)
					newNode1.children.append(root)
					root.children[0] = eqparser.Node("INT",[],1)
					root.children[1].children[1] = eqparser.Node("INT",[],1)
					return newNode1
			elif numB == 0:
				if a.children[0].leaf == b.leaf:
					newNode1 = eqparser.Node("BINARYOP",[],'*')
					newNode2 = eqparser.Node(b.type,[],b.leaf)
					newNode1.children.append(root)
					newNode1.children.append(newNode2)
					root.children[0].children[0] = eqparser.Node("INT",[],1)
					root.children[1] = eqparser.Node("INT",[],1)
					return newNode1
				elif numA == 2 and a.children[1].leaf == b.leaf and a.leaf!='/':
					newNode1 = eqparser.Node("BINARYOP",[],'*')
					newNode2 = eqparser.Node(b.type,[],b.leaf)
					newNode1.children.append(root)
					newNode1.children.append(newNode2)
					root.children[0].children[1] = eqparser.Node("INT",[],1)
					root.children[1] = eqparser.Node("INT",[],1)
					return newNode1
			elif numA == 2 and numB == 2:
				if (a.leaf == '*' or a.leaf == '/') and (b.leaf == '*' or b.leaf == '/'):			
					if equalTree.checkEqual(a.children[0],b.children[0]):
						newCopy = copyTree.createTreeCopy(a.children[0])
						newNode1 = eqparser.Node("BINARYOP",[],'*')
						newNode1.children.append(newCopy)
						newNode1.children.append(root)
						root.children[0].children[0] = eqparser.Node("INT",[],1)
						root.children[1].children[0] = eqparser.Node("INT",[],1)
						return newNode1
					elif a.leaf =='*' and equalTree.checkEqual(a.children[1],b.children[0]):
						newCopy = copyTree.createTreeCopy(a.children[1])
						newNode1 = eqparser.Node("BINARYOP",[],'*')
						newNode1.children.append(newCopy)
						newNode1.children.append(root)
						root.children[0].children[1] = eqparser.Node("INT",[],1)
						root.children[1].children[0] = eqparser.Node("INT",[],1)
						return newNode1
					elif b.leaf =='*' and equalTree.checkEqual(a.children[0],b.children[1]):
						newCopy = copyTree.createTreeCopy(a.children[0])
						newNode1 = eqparser.Node("BINARYOP",[],'*')
						newNode1.children.append(newCopy)
						newNode1.children.append(root)
						root.children[0].children[0] = eqparser.Node("INT",[],1)
						root.children[1].children[1] = eqparser.Node("INT",[],1)
						return newNode1
					elif a.leaf == '*' and b.leaf == '*' and equalTree.checkEqual(a.children[1],b.children[1]):
						newCopy = copyTree.createTreeCopy(a.children[1])
						newNode1 = eqparser.Node("BINARYOP",[],'*')
						newNode1.children.append(newCopy)
						newNode1.children.append(root)
						root.children[0].children[1] = eqparser.Node("INT",[],1)
						root.children[1].children[1] = eqparser.Node("INT",[],1)
						return newNode1
					elif a.leaf == '/' and b.leaf == '/' and equalTree.checkEqual(a.children[1],b.children[1]):
						newCopy = copyTree.createTreeCopy(a.children[1])
						
						newDiv1 = eqparser.Node("BINARYOP",[],'/')
						newDiv2 = eqparser.Node("INT",[],1)
						newDiv1.children.append(newDiv2)
						newDiv1.children.append(newCopy)
						
						newNode1 = eqparser.Node("BINARYOP",[],'*')
						newNode1.children.append(newDiv1)
						newNode1.children.append(root)
						root.children[0] = root.children[0].children[0]
						root.children[1] = root.children[1].children[0]
						return newNode1
		return 0
	
		
		
# Main Function ****************************************************************
if __name__ == "__main__":
	while 1:
		try:
			s = "(1/(x+y)) - (2/(x+y)) = 0"   # use input() on Python 3
		except EOFError:
			print
			break
		root = eqparser.parse(s)
		newRoot =  invDist(root.children[0])	
		print "Old Tree = " + repr(root.children[0])
		print str(root.children[0])
		print "New Tree = " + repr(newRoot)
		print str(newRoot)
		break
	
