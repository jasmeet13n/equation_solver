import eqparser
import copyTree

def comm(root):
	if root == None:
		return root;
	if root.leaf == '=':
		return 0
	if root.leaf == '+' or root.leaf == '*':
		newRoot = copyTree.createTreeCopy(root)
		tmp = newRoot.children[0]
		newRoot.children[0] = newRoot.children[1]
		newRoot.children[1] = tmp
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
		print "Old Tree = " + repr(root)
		print str(root)
		newRoot =  comm(root.children[0])	
		print "New Tree = " + repr(newRoot)
		print str(newRoot)
	
