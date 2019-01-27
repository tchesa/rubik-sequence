from rubik import Rubik
import sys

states = []
cube = Rubik()
sys.setrecursionlimit(99999999)
sys.settrace

def addState(c):
  if not c in states:
    states.append(c.clone())
    print(len(states))
    addState(c.move('F'))
    addState(c.move('R'))
    addState(c.move('U'))
    addState(c.move('L'))
    addState(c.move('B'))
    addState(c.move('D'))
  else:
    print('not')
addState(cube)
