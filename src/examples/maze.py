from simgui import *
from board import *

class Maze:
  pass

def make_maze(g, draw):
  m=Maze()
  m.g=g
  m.rwalls=[[False, False, False, True, False, False, False, False, True, False, False, False],
            [True, True, False, False, False, True, True, False, False, False, True, True],
            [False, True, False, False, False, False, False, False, False, False, True, False],
            [False, False, False, False, False, False, False, False, False, False, False, False],
            [False, True, False, True, False, False, False, False, True, False, True, False],
            [True, True, False, True, False, False, False, False, True, False, True, True],
            [True, False, False, False, False, False, False, False, False, False, False, True],
            [False, False, True, False, False, False, False, False, False, True, False, False],
            [False, False, False, False, False, True, True, False, False, False, False, False],
            [False, True, False, False, False, False, False, False, False, False, True, False]]
  m.bwalls=[[False, False, False, False, False, False, False, False, False, False, False, False, False],
            [True, False, False, False, True, True, False, True, True, False, False, False, True],
            [False, False, True, False, False, False, True, False, False, False, True, False, False],
            [False, False, True, False, True, True, False, True, True, False, True, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, True, True, True, True, True, False, False, False, False,],
            [True, False, False, False, False, False, True, False, False, False, False, False, True],
            [False, False, True, True, False, False, False, False, False, True, True, False, False],
            [False, False, True, False, True, True, False, True, True, False, True, False, False]]
  if draw:
    draw_rwalls(m)
    draw_bwalls(m)
  return m

def can_move_in_maze_multi(m, r, c, ds):
  for d in ds:
    if not can_move_in_maze(m, r, c, d):
      return False
    r, c=get_next_loc((r, c), d)
  return True

def can_move_in_maze(m, r, c, d):
  if not can_move(m.g, r, c, d):
    return False
  if d=="l":
    return not m.rwalls[r][c-1]
  elif d=="r":
    return not m.rwalls[r][c]
  elif d=="u":
    return not m.bwalls[r-1][c]
  elif d=="d":
    return not m.bwalls[r][c]

def draw_rwalls(m):
  r=0
  while r<len(m.rwalls):
    c=0
    while c<len(m.rwalls[r]):
      if m.rwalls[r][c]:
        draw_rwall(m.g, r, c)
      c=c+1
    r=r+1
def draw_bwalls(m):
  r=0
  while r<len(m.bwalls):
    c=0
    while c<len(m.bwalls[r]):
      if m.bwalls[r][c]:
        draw_bwall(m.g, r, c)
      c=c+1
    r=r+1

def draw_rwall(g, r, c):
  x=cell_x(g, c+1)
  y=cell_y(g, r)
  add_gi_rect(f"rw{r}-{c}", x-2/2, y, 2, 30, "red")

def draw_bwall(g, r, c):
  x=cell_x(g, c)
  y=cell_y(g, r+1)
  add_gi_rect(f"bw{r}-{c}", x, y-2/2, 30, 2, "red")

g=make_grid(400, 300)
m=make_maze(g, False)
print(can_move_in_maze_multi(m, 0, 12, "ddu"))