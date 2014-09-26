def checkEqual(r1,r2):
	if r1 == None and r2!=None:
		return False
	elif r1!=None and r2==None:
		return False
	elif r1 == None and r2 == None:
		return True
	l1 = len(r1.children)
	l2 = len(r2.children)
	if(l1 != l2):
		return False
	if r1.leaf != r2.leaf:
		return False
	if l1==0 and l2==0:
		return True
	if checkEqual(r1.children[0],r2.children[0]) == False:
		return False
	if l1 == 1 and l2 == 1:
		return True
	if checkEqual(r1.children[1],r2.children[1]) == False:
		return False
	return True
