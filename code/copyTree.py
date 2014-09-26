import eqparser

def createTreeCopy(root):
	if root == None:
		return None;
	newRoot = eqparser.Node(root.type,[],root.leaf)
	if isinstance(root.children,list) == False:
		root.children = [root.children];
	for i in range(len(root.children)):
		newRoot.children.append(createTreeCopy(root.children[i]))
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
		newRoot = createTreeCopy(root)
		newRoot.children[0].leaf = 'a'
		print "Old Tree = " + repr(root)
		print "New Tree = " + repr(newRoot)
	
