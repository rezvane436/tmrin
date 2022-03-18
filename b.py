def accepts(transitions,initial,accepting,s):
    state = initial
    for c in s:
        state = transitions[state][c]
    return state in accepting

dfa = {1:{'a':4, 'b':2},
       2:{'a':10, 'b':3},
       3:{'a':4, 'b':3},
       4:{'a':7, 'b':5},
       5:{'a':10, 'b':6},
       6:{'a':7, 'b':6},
       7:{'a':1, 'b':8},
       8:{'a':10, 'b':9},
       9:{'a':1, 'b':9},
       10:{'a':10, 'b':10}}

def dfaTest(s):
    return accepts(dfa,3,{1,2,3},s)

def valid(s):
    return s.count('a') % 3 == 0 and not 'aba' in s

import random

tests = [''.join(random.choice(['a','b']) for j in range(100)) for i in range(1,1001)]

print(all(valid(s) == dfaTest(s) for s in tests))