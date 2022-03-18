def checkStateA(n):
	
	# check length of n
	# is 0 then print
	# string accepted
	if(len(n)== 0):
		print("string accepted")
		
	# if 1 is found call function
	# checkStateA otherwise if 0
	# is found call function stateB
	else:
		if(n[0]=='1'):
			checkStateA(n[1:])
		else:
			stateB(n[1:])


def stateB(n):
	
	# check length of n
	# is 0 then print
	# string not accepted
	if(len(n)== 0):
		print("string not accepted")
		
	# if 1 is found call function
	# stateB otherwise if 0
	# is found call function stateC
	else:
		if(n[0]=='1'):
			stateB(n[1:])
		else:
			stateC(n[1:])
		
		
def stateC(n):
	
	# check length of n
	# is 0 then print
	# string not accepted
	if(len(n)== 0):
		print("string not accepted")
		
	# if 1 is found call function
	# stateC otherwise if 0
	# is found call function checkStateA
	else:
		if(n[0]=='1'):
			stateC(n[1:])
		else:
			checkStateA(n[1:])
		
# take string input
n = input()

# call checkStateA
# to check the inputted string
checkStateA(n)
