#!/usr/bin/python
import eqparser 
import heuristic
import search

# Input Checker Function *******************************************************
def inputCheck(root):
	d = 0
	if root.type != "EQUALS":
		print "Expression entered is not a valid equation " + str(root)
		d=1
	if d == 1:
		return False
	else:
		return True

# Main Function ****************************************************************
if __name__ == "__main__":
	while 1:
		try:
			#s = "e^x = sin(8 + ((3/2)*z) - ((1/2)*z) + y)^2 + cos(8+y+z)^2"
			s = raw_input('eq > ')   # use input() on Python 3
			v = raw_input('vr > ')
		except EOFError:
			print
			break
		root = eqparser.parse(s)
		if inputCheck(root) == True:
			search.search(root,v)

