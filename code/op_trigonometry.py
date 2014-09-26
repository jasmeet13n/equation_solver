import eqparser
import copyTree
import equalTree

def trig(r):
	if r == None:
		return r;
	if r.leaf == '=':
		return 0
	root = r
	if root.leaf == '+':
		if root.children[0].leaf == '^' and root.children[1].leaf == '^':
			if root.children[0].children[0].leaf == 'sin' and root.children[0].children[1].leaf == 2 and root.children[1].children[0].leaf == 'cos' and root.children[1].children[1].leaf == 2:
				if equalTree.checkEqual(root.children[0].children[0].children[0],root.children[1].children[0].children[0]):
					newNode = eqparser.Node("INT",[],1)
					return newNode
			elif root.children[0].children[0].leaf == 'cos' and root.children[0].children[1].leaf == 2 and root.children[1].children[0].leaf == 'sin' and root.children[1].children[1].leaf == 2:
				if equalTree.checkEqual(root.children[0].children[0].children[0],root.children[1].children[0].children[0]):
					newNode = eqparser.Node("INT",[],1)
					return newNode
	return 0

if __name__ == "__main__":
	while 1:
		try:
			s = "sin(x+y+z)^2 + cos(x+y+x)^2 = x"   # use input() on Python 3
		except EOFError:
			print
			break
		root = eqparser.parse(s)
		newRoot =  trig(root.children[0])	
		print "Old Tree = " + repr(root)
		print str(root)
		print "New Tree = " + repr(newRoot)
		print str(newRoot)
		if newRoot!=0:
			print equalTree.checkEqual(root,newRoot)
		break
	
