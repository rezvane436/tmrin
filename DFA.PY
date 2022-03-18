def start(c):
	if (c == 'a'):
		dfa = 1
	else:
		dfa = 3
	return dfa
	
# This function is for the first
# dfa = state of DFA
def state1(c):
	if (c == 'a'):
		dfa = 3
	else:
		dfa = 4
	return dfa
	
# This function is for the second
# dfa = state of DFA
def state2(c):
	if (c == 'a'):
		dfa = 5
	else:
		dfa = 2
	return dfa
	
# This function is for the third
# dfa = state of DFA
def state3(c):
	if (c == 'a'):
		dfa = 3
	else:
		dfa = 3
	return dfa
	
# This function is for the fourth
# dfa = state of DFA
def state4(c):
	if (c == 'a'):
		dfa = 5
	else:
		dfa = 2
	return dfa
	
	
# This function is for the fifth
# dfa = state of DFA
def state5(c):
	if (c == 'a'):
		dfa = 3
	else:
		dfa = 2
	return dfa
	
def isAccepted(String):
		
	# store length of Stringing
	l = len(String)
		
	# dfa tells the number associated
	# with the present dfa = state
	dfa = 0
	for i in range(l):
		if (dfa == 0):
			dfa = start(String[i])
	
		elif (dfa == 1):
			dfa = state1(String[i])
	
		elif (dfa == 2) :
			dfa = state2(String[i])
	
		elif (dfa == 3) :
			dfa = state3(String[i])
	
		elif (dfa == 4) :
			dfa = state4(String[i])
		
		elif (dfa == 5) :
			dfa = state5(String[i])
		else:
			return 0
	if(dfa == 3 or dfa == 0) :
		return 0
	else:
		return 1
	
# Driver code
if __name__ == "__main__" :
	String = "ageeksaforageeks"
	if (isAccepted(String)) :
		print("ACCEPTED")
	else:
		print("NOT ACCEPTED")
	
