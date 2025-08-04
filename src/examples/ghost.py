from board import *
from maze import *

gt=(0, 0)
g=(1, 2)
ns=[]
m=make_maze(False)
for d in ["l", "r", "u", "d"]:
  if can_move_in_maze(m, g[0], g[1], d):
    ns.append(get_next_loc(g, d))
print(ns)
