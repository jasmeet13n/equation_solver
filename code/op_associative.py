import eqparser
import copyTree

def asso(root):
	if root == None:
		return root;
	if root.leaf == '=':
		return 0
	newRoot = 0
# Root Plus
	if root.leaf == '+':
		if root.children[0].leaf == '+':
			newRoot = copyTree.createTreeCopy(root)
			a = newRoot.children[0].children[0]
			b = newRoot.children[0].children[1]
			c = newRoot.children[1]
			tmp = newRoot.children[0]
			tmp.children[0] = b
			tmp.children[1] = c
			newRoot.children[0] = a
			newRoot.children[1] = tmp
		elif root.children[1].leaf == '+':
			newRoot = copyTree.createTreeCopy(root)
			a = newRoot.children[0]
			b = newRoot.children[1].children[0]
			c = newRoot.children[1].children[1]
			tmp = newRoot.children[1]
			tmp.children[0] = a
			tmp.children[1] = b
			newRoot.children[1] = c
			newRoot.children[0] = tmp
		elif root.children[0].leaf == '-':
			newRoot = copyTree.createTreeCopy(root)
			a = newRoot.children[0].children[0]
			b = newRoot.children[0].children[1]
			c = newRoot.children[1]
			tmp = newRoot.children[0]
			tmp.children[0] = b
			tmp.children[1] = c
			newRoot.children[0] = a
			newRoot.children[1] = tmp
			newRoot.leaf = '-'
			tmp.leaf = '-'
		elif root.children[1].leaf == '-':
			newRoot = copyTree.createTreeCopy(root)
			a = newRoot.children[0]
			b = newRoot.children[1].children[0]
			c = newRoot.children[1].children[1]
			tmp = newRoot.children[1]
			tmp.children[0] = a
			tmp.children[1] = b
			newRoot.children[1] = c
			newRoot.children[0] = tmp
			newRoot.leaf = '-'
			tmp.leaf = '+'
		return newRoot
# Root Minus
	elif root.leaf == '-':
		if root.children[0].leaf == '+':
			newRoot = copyTree.createTreeCopy(root)
			a = newRoot.children[0].children[0]
			b = newRoot.children[0].children[1]
			c = newRoot.children[1]
			tmp = newRoot.children[0]
			tmp.children[0] = b
			tmp.children[1] = c
			newRoot.children[0] = a
			newRoot.children[1] = tmp
			newRoot.leaf = '+'
			tmp.leaf = '-'
		elif root.children[1].leaf == '+':
			newRoot = copyTree.createTreeCopy(root)
			a = newRoot.children[0]
			b = newRoot.children[1].children[0]
			c = newRoot.children[1].children[1]
			tmp = newRoot.children[1]
			tmp.children[0] = a
			tmp.children[1] = b
			newRoot.children[1] = c
			newRoot.children[0] = tmp
			tmp.leaf = '-'
		elif root.children[0].leaf == '-':
			newRoot = copyTree.createTreeCopy(root)
			a = newRoot.children[0].children[0]
			b = newRoot.children[0].children[1]
			c = newRoot.children[1]
			tmp = newRoot.children[0]
			tmp.children[0] = b
			tmp.children[1] = c
			newRoot.children[0] = a
			newRoot.children[1] = tmp
			newRoot.leaf = '-'
			tmp.leaf = '+'
		elif root.children[1].leaf == '-':
			newRoot = copyTree.createTreeCopy(root)
			a = newRoot.children[0]
			b = newRoot.children[1].children[0]
			c = newRoot.children[1].children[1]
			tmp = newRoot.children[1]
			tmp.children[0] = a
			tmp.children[1] = b
			newRoot.children[1] = c
			newRoot.children[0] = tmp
			newRoot.leaf = '+'
		return newRoot

# Root Multiply
	if root.leaf == '*':
		if root.children[0].leaf == '*':
			newRoot = copyTree.createTreeCopy(root)
			a = newRoot.children[0].children[0]
			b = newRoot.children[0].children[1]
			c = newRoot.children[1]
			tmp = newRoot.children[0]
			tmp.children[0] = b
			tmp.children[1] = c
			newRoot.children[0] = a
			newRoot.children[1] = tmp
		elif root.children[1].leaf == '*':
			newRoot = copyTree.createTreeCopy(root)
			a = newRoot.children[0]
			b = newRoot.children[1].children[0]
			c = newRoot.children[1].children[1]
			tmp = newRoot.children[1]
			tmp.children[0] = a
			tmp.children[1] = b
			newRoot.children[1] = c
			newRoot.children[0] = tmp
		elif root.children[0].leaf == '/':
			newRoot = copyTree.createTreeCopy(root)
			a = newRoot.children[0].children[0]
			b = newRoot.children[0].children[1]
			c = newRoot.children[1]
			tmp = newRoot.children[0]
			tmp.children[0] = b
			tmp.children[1] = c
			newRoot.children[0] = a
			newRoot.children[1] = tmp
			newRoot.leaf = '/'
			tmp.leaf = '/'
		elif root.children[1].leaf == '/':
			newRoot = copyTree.createTreeCopy(root)
			a = newRoot.children[0]
			b = newRoot.children[1].children[0]
			c = newRoot.children[1].children[1]
			tmp = newRoot.children[1]
			tmp.children[0] = a
			tmp.children[1] = b
			newRoot.children[1] = c
			newRoot.children[0] = tmp
			newRoot.leaf = '/'
			tmp.leaf = '*'
		return newRoot
# Root Divide
	elif root.leaf == '/':
		if root.children[0].leaf == '/':
			newRoot = copyTree.createTreeCopy(root)
			a = newRoot.children[0].children[0]
			b = newRoot.children[0].children[1]
			c = newRoot.children[1]
			tmp = newRoot.children[0]
			tmp.children[0] = b
			tmp.children[1] = c
			newRoot.children[0] = a
			newRoot.children[1] = tmp
			newRoot.leaf = '/'
			tmp.leaf = '*'
		elif root.children[1].leaf == '/':
			newRoot = copyTree.createTreeCopy(root)
			a = newRoot.children[0]
			b = newRoot.children[1].children[0]
			c = newRoot.children[1].children[1]
			tmp = newRoot.children[1]
			tmp.children[0] = a
			tmp.children[1] = b
			newRoot.children[1] = c
			newRoot.children[0] = tmp
			newRoot.leaf = '*'
		elif root.children[0].leaf == '*':
			newRoot = copyTree.createTreeCopy(root)
			a = newRoot.children[0].children[0]
			b = newRoot.children[0].children[1]
			c = newRoot.children[1]
			tmp = newRoot.children[0]
			tmp.children[0] = b
			tmp.children[1] = c
			newRoot.children[0] = a
			newRoot.children[1] = tmp
			newRoot.leaf = '*'
			tmp.leaf = '/'
		elif root.children[1].leaf == '*':
			newRoot = copyTree.createTreeCopy(root)
			a = newRoot.children[0]
			b = newRoot.children[1].children[0]
			c = newRoot.children[1].children[1]
			tmp = newRoot.children[1]
			tmp.children[0] = a
			tmp.children[1] = b
			newRoot.children[1] = c
			newRoot.children[0] = tmp
			tmp.leaf = '/'
		return newRoot
	return 0
		
		
# Main Function ****************************************************************
if __name__ == "__main__":
	while 1:
		try:
			s = raw_input('eq > ')   # use input() on Python 3
		except EOFError:
			print
			break
		root = eqparser.parse(s)
		print "Old Tree = " + repr(root.children[0])
		print str(root.children[0])
		newRoot =  asso(root.children[0])	
		print "New Tree = " + repr(newRoot)
		print str(newRoot)
	
