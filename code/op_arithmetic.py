import eqparser
import copyTree

def arith(root):
	if root == None:
		return root;
	if root.leaf == '=':
		return 0
#	print root.leaf
#	print root.children[0]
#	print root.children[1]
	if root.leaf == '+' or root.leaf == '-' or root.leaf == '*' or root.leaf == '/' or root.leaf == '^':
		flag = 0
		if root.children[0].leaf == 'undefined' or root.children[1].leaf == 'undefined':
			return eqparser.Node("SYMBOL",[],"undefined")
		
		if root.leaf == '/' and root.children[1].leaf == 0:
			return eqparser.Node("SYMBOL",[],"undefined")
			
		if (root.children[0].type == "INT" or root.children[0].type == "FLOAT") and (root.children[1].type == "INT" or root.children[1].type == "FLOAT"):
			flag = 1
		
		# addition subtraction with 0
		elif root.leaf == '+' and root.children[0].leaf==0 and root.children[1].leaf!=0:
			return copyTree.createTreeCopy(root.children[1])
		elif (root.leaf == '+' or root.leaf == '-') and root.children[0].leaf!=0 and root.children[1].leaf==0:
			return copyTree.createTreeCopy(root.children[0])

		# multiplication with 0
		elif root.leaf == '*' and root.children[0].leaf==0 and root.children[1].leaf!=0:
			return eqparser.Node("INT",[],0)
		elif root.leaf == '*' and root.children[0].leaf!=0 and root.children[1].leaf==0:
			return eqparser.Node("INT",[],0)
		#elif root.leaf == '*' and root.children[0].leaf=='undefined' and root.children[1].leaf==0:
		#	return eqparser.Node("INT",[],1)
			
		# multiplication with 1
		elif root.leaf == '*' and root.children[0].leaf==1 and root.children[1].leaf!=0:
			return copyTree.createTreeCopy(root.children[1])
		elif root.leaf == '*' and root.children[0].leaf!=0 and root.children[1].leaf==1:
			return copyTree.createTreeCopy(root.children[0])
		
		# division if numerator == 0 and division with 1
		elif root.leaf == '/' and root.children[0].leaf==0 and root.children[1].leaf!=0:
			return eqparser.Node("INT",[],0)
		elif root.leaf == '/' and root.children[0].leaf!=0 and root.children[1].leaf==1:
			return copyTree.createTreeCopy(root.children[0])
		
		# power of 1 and 0
		elif root.leaf == '^' and root.children[0].leaf==1:
			return eqparser.Node("INT",[],1)
		elif root.leaf == '^' and root.children[0].leaf==0:
			return eqparser.Node("INT",[],0)
		elif root.leaf == '^' and root.children[1].leaf==0:
			return eqparser.Node("INT",[],1)
		elif root.leaf == '^' and root.children[1].leaf==1:
			return copyTree.createTreeCopy(root.children[0])
		
		if len(root.children[0].children) == 0 and len(root.children[1].children) == 0:
			if root.children[0].leaf == root.children[1].leaf:
				if root.leaf == '+':
					newNode = eqparser.Node(root.type,[],'*')
					newNode.children.append(eqparser.Node("INT",[],2))
					newNode.children.append(eqparser.Node(root.children[0].type,[],root.children[0].leaf))
					return newNode
				if root.leaf == '-':
					return eqparser.Node("INT",[],0)
				if root.leaf == '/':
					return eqparser.Node("INT",[],1)

		if flag == 1:
			if root.leaf == '/' or (root.children[0].type == "FLOAT" or root.children[1].type == "FLOAT"):
				newNode = eqparser.Node("FLOAT",[],0)
			elif root.children[0].type == "INT" and root.children[0].type == "INT":
				newNode = eqparser.Node("INT",[],0)
			else:
				return 0
			if root.leaf == '+':
					newNode.leaf = root.children[0].leaf + root.children[1].leaf
			elif root.leaf == '-':
					newNode.leaf = root.children[0].leaf - root.children[1].leaf
			elif root.leaf == '*':
					newNode.leaf = root.children[0].leaf * root.children[1].leaf
			elif root.leaf == '/':
					newNode.leaf = (root.children[0].leaf*1.0) / root.children[1].leaf
			elif root.leaf == '^':
					newNode.leaf = (root.children[0].leaf) ** root.children[1].leaf
			return newNode
			
	elif root.leaf == "ln" or root.leaf == "log":
		if root.children[0].leaf == 'undefined':
			return eqparser.Node("SYMBOL",[],"undefined")
		# ln
		if root.leaf == "ln" and root.children[0].leaf == 1:
			return eqparser.Node("INT",[],0)
		elif root.leaf == "ln" and root.children[0].leaf == 'e':
			return eqparser.Node("INT",[],1)
		# log
		elif root.leaf == "log" and root.children[0].leaf == 1:
			return eqparser.Node("INT",[],0)
		elif root.leaf == "log" and root.children[0].leaf == 2:
			return eqparser.Node("INT",[],1)
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
		newRoot =  arith(root.children[0])	
		print "Old Tree = " + repr(root)
		print "New Tree = " + repr(newRoot)
		print str(newRoot)
	
