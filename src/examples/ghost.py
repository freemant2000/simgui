from simgui import *
from board import add_img_in_cell, move_img_to_cell, get_next_loc, get_dist
from walls import make_hwalls, make_vwalls, can_move
from random import choice, shuffle
import pacman as pm

gr, gc=5, 6
targets=[]
mode="roaming"

def make_plan():
  global targets
  b_corners=[(0, 0), (9, 0), (0, 12), (9, 12)]
  shuffle(b_corners)
  if mode=="chasing":
    d, e=gr-pm.r, gc-pm.c
    p_corners=[(pm.r-d, pm.c-e), (pm.r-d, pm.c+e), (pm.r+d, pm.c-e)]
    shuffle(p_corners)
    targets=p_corners
    targets.extend(b_corners)
  elif mode=="roaming":
    targets=b_corners
  print(f"New plan: {targets})")

def on_ready():
  add_graphics_view(400, 300)
  make_ghost()
  make_vwalls()
  make_hwalls()
  make_plan()
  start_timer("t1", 0.4)

def make_ghost():
  add_img_in_cell("g", gr, gc, "pacman-ghost.png")

def on_timeout_t1():
  update_ghost()
 
def get_next_move(gtr, gtc):
  mvs=[]
  if gtr<gr and can_move(gr, gc, "u"):
    mvs.append("u")
  if gtr>gr and can_move(gr, gc, "d"):
    mvs.append("d")
  if gtc<gc and can_move(gr, gc, "l"):
    mvs.append("l")
  if gtc>gc and can_move(gr, gc, "r"):
    mvs.append("r")
  if mvs==[]:
    return None
  else:
    return choice(mvs)

def on_timeout_t1():
  update_ghost()
  
def update_ghost():
  change_mode()
  gtr, gtc=targets[0]
  if gr==gtr and gc==gtc:
    print(f"Reached target ({gtr}, {gtc})")
    make_plan()
    gtr, gtc=targets[0]
  d=get_next_move(gtr, gtc)  
  if d==None:
    targets.pop(0)
    print(f"Target removed. New targets: {targets})")
    if targets==[]:
      make_plan()
  move_ghost(d)
  print(f"Moved {d}")

def change_mode():  
  global mode
  dist=get_dist(pm.r, pm.c, gr, gc)
  if dist<8 and mode=="roaming":
    mode="chasing"
    print(f"Mode changed to {mode}")
    make_plan()
  elif dist>=8 and mode=="chasing":
    mode="roaming"
    print(f"Mode changed to {mode}")
    make_plan()

def move_ghost(d):
  global gr, gc
  gr, gc=get_next_loc(gr, gc, d)
  move_img_to_cell("g", gr, gc)

if __name__=="__main__":
  start()
#  make_plan()
#  change_mode()
