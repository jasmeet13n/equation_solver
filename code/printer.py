import eqparser
from printingcolors import *

pretty_printing_colors = {
    'FLOAT'          : bcolors.CYAN,
    'INT'            : bcolors.BLUE,
    'VARIABLENAME'   : bcolors.YELLOW,
    'SYMBOL'         : bcolors.GREEN,
    'EQUALS'         : bcolors.WHITE,
    'BINARYOP'       : bcolors.WHITE,
    'UNARYOP'        : bcolors.RED,
    'UNARYFUNCTION'  : bcolors.MAGENTA,
    'BINARYFUNCTION'  : bcolors.MAGENTA,
    }

def printer(root):
	if root == None:
		return
	s = ""
	l = len(root.children)
	
	if l==2 and root.type =="BINARYFUNCTION":
		s+=""+ pretty_printing_colors[root.type] +str(root.leaf) + bcolors.ENDC + "("		
	if l==1:
		s+=""+ pretty_printing_colors[root.type] +str(root.leaf) + bcolors.ENDC + "("
	if l>0:
		flag = 1
		if len(root.children[0].children) == 0:
			flag = 0
		if flag == 1 and root.leaf!='=':
			s+="("
		s+=printer(root.children[0])
		if flag == 1 and root.leaf!='=':
			s+=")" 
	if l==1:
		s+=") "
	if l==0:
		s+= pretty_printing_colors[root.type] +str(root.leaf) + bcolors.ENDC		
	if l==2 and root.type =="BINARYFUNCTION":
		s+=" , "
	elif l==2:
		s+=" "+ pretty_printing_colors[root.type] +str(root.leaf)+" " + bcolors.ENDC
	if l>1:
		flag = 1
		if len(root.children[1].children) == 0:
			flag = 0
		if flag == 1 and root.leaf!='=':
			s+="("
		s+=printer(root.children[1])
		if flag == 1 and root.leaf!='=':
			s+=")" 
	if l==2 and root.type == "BINARYFUNCTION":
		s+=")"
	return s

