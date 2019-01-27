from enum import Enum

class Rubik:
  def __init__(self): # starts at the solved state
    self.front = [[Color.RED for _ in range(3)] for _ in range(3)]
    self.back = [[Color.ORANGE for _ in range(3)] for _ in range(3)]
    self.left = [[Color.GREEN for _ in range(3)] for _ in range(3)]
    self.right = [[Color.BLUE for _ in range(3)] for _ in range(3)]
    self.up = [[Color.WHITE for _ in range(3)] for _ in range(3)]
    self.down = [[Color.YELLOW for _ in range(3)] for _ in range(3)]

  def clone(self):
    new = Rubik()
    for x in range(3):
      for y in range(3):
        new.front[x][y] = self.front[x][y]
        new.back[x][y] = self.back[x][y]
        new.left[x][y] = self.left[x][y]
        new.right[x][y] = self.right[x][y]
        new.up[x][y] = self.up[x][y]
        new.down[x][y] = self.down[x][y]
    return new

  def move(self, code):
    # rubik movements, following the rubik notation of https://ruwix.com/the-rubiks-cube/notation/
    # F  R  U  L  B  D    basics
    # F' R' U' L' B' D'   reverse
    # F2 R2 U2 L2 B2 D2   double
    newState = self.clone()
    if (code == 'F'):
      for i in range(3):
        for j in range(3):
          newState.front[i][j] = self.front[3-j-1][i]
        newState.up[2][i] = self.left[i][2]
        newState.left[i][2] = self.down[0][i]
        newState.down[0][i] = self.right[i][0]
        newState.right[i][0] = self.up[2][i]
    elif (code == 'R'):
      for i in range(3):
        for j in range(3):
          newState.right[i][j] = self.right[3-j-1][i]
        newState.up[i][2] = self.front[i][2]
        newState.front[i][2] = self.down[i][2]
        newState.down[i][2] = self.back[3-i-1][0]
        newState.back[i][0] = self.up[3-i-1][2]
    elif (code == 'U'):
      for i in range(3):
        for j in range(3):
          newState.up[i][j] = self.up[3-j-1][i]
        newState.left[0][i] = self.front[0][i]
        newState.front[0][i] = self.right[0][i]
        newState.right[0][i] = self.back[0][i]
        newState.back[0][i] = self.left[0][i]
    elif (code == 'L'):
      for i in range(3):
        for j in range(3):
          newState.left[i][j] = self.left[3-j-1][i]
        newState.front[i][0] = self.up[i][0]
        newState.up[i][0] = self.back[3-i-1][2]
        newState.back[i][2] = self.down[3-i-1][0]
        newState.down[i][0] = self.front[i][0]
    elif (code == 'B'):
      for i in range(3):
        for j in range(3):
          newState.back[i][j] = self.back[3-j-1][i]
        newState.up[0][i] = self.right[i][2]
        newState.right[i][2] = self.down[2][i]
        newState.down[2][i] = self.left[i][0]
        newState.left[i][0] = self.back[0][i]
    elif (code == 'D'):
      for i in range(3):
        for j in range(3):
          newState.down[i][j] = self.down[3-j-1][i]
        newState.front[2][i] = self.left[2][i]
        newState.left[2][i] = self.back[2][i]
        newState.back[2][i] = self.right[2][i]
        newState.right[2][i] = self.front[2][i]
    return newState

  def __eq__(self, other):
    for x in range(3):
      for y in range(3):
        if self.front[x][y] != other.front[x][y]:
          return False
        if self.back[x][y] != other.back[x][y]:
          return False
        if self.left[x][y] != other.left[x][y]:
          return False
        if self.right[x][y] != other.right[x][y]:
          return False
        if self.up[x][y] != other.up[x][y]:
          return False
        if self.down[x][y] != other.down[x][y]:
          return False
    return True

class Color(Enum):
  RED = 1
  ORANGE = 2
  GREEN = 3
  BLUE = 4
  WHITE = 5
  YELLOW = 6
