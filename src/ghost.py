from simgui import *
<<<<<<< HEAD
from board import add_img_in_cell, move_img_to_cell, get_next_loc
from walls import make_hwalls, make_vwalls, can_move
from random import choice, shuffle
import pacman as pm

#gtr, gtc=0, 0
gr, gc=5, 6

targets=[]
=======
from board import *
from random import choice
from walls import *
import pacman as pm

gtr, gtc=0, 0
gr, gc=2, 2

def get_next_move():
  mvs=[]
  if get_dist(pm.r, pm.c, gr, gc)<=8:
    if pm.is_powered_up:
      return choice(get_escape_moves())
    else:
      tr, tc=pm.r, pm.c
  else:
    tr, tc=gtr, gtc
  if tr<gr and can_move(gr, gc, "u"):
    mvs.append("u")
  if tr>gr and can_move(gr, gc, "d"):
    mvs.append("d")
  if tc<gc and can_move(gr, gc, "l"):
    mvs.append("l")
  if tc>gc and can_move(gr, gc, "r"):
    mvs.append("r")
  if mvs==[]:
    return None
  else:
    return choice(mvs)

def move_ghost(d):
  global gr, gc
  gr, gc=get_next_loc(gr, gc, d)
  move_img_to_cell("g", gr, gc)

def make_ghost():
  add_img_in_cell("g", gr, gc, "pacman-ghost.png")

def update_ghost():  
  global gtr, gtc
  d=get_next_move()  
  if d==None:
    gtr=choice([0, 9])
    gtc=choice([0, 12])
  else:
    move_ghost(d)
>>>>>>> a5725fc69171f4f133c6f5665e8862621eb06c0a

def on_ready():
  add_graphics_view(400, 300)
  make_ghost()
  make_vwalls()
  make_hwalls()
  start_timer("t1", 0.4)

<<<<<<< HEAD
def make_ghost():
  add_img_in_cell("g", gr, gc, "pacman-ghost.png")

def on_timeout_t1():
  update_ghost()
  
def update_ghost():  
  global gtr, gtc
  d=get_next_move()  
  if d==None:
    plan()
  else:
    move_ghost(d)

#mode="wander"
mode="escape"

def plan():
  global targets
  print("planning")
  dr=gr-pm.r
  dc=gc-pm.c
  b_corners=[(0, 0), (9, 0), (0, 12), (9, 12)]
  shuffle(b_corners)
  if mode=="wander":
    targets=b_corners
  elif mode=="chase":
    pm_corners=[(pm.r-dr, pm.c-dc), (pm.r-dr, pm.c+dc), (pm.r+dr, pm.c-dc)]
    shuffle(pm_corners)
    targets=pm_corners
    targets.extend(b_corners)
  elif mode=="escape":
    g_corners=[(gr+dr, gc+dc), (gr, gc+dc), (gr+dr, gc)]
    shuffle(g_corners)
    targets=g_corners
    targets.extend(b_corners)
  print("new targets", targets)

def get_next_move():
  mvs=[]
  while True:
    if targets==[]:
      print("no more target")
      return None
    gtr, gtc=targets[0]
    if gr==gtr and gc==gtc:
      print(f"reached target ({gtr}, {gtc})")
      return None
    if gtr<gr and can_move(gr, gc, "u"):
      mvs.append("u")
    if gtr>gr and can_move(gr, gc, "d"):
      mvs.append("d")
    if gtc<gc and can_move(gr, gc, "l"):
      mvs.append("l")
    if gtc>gc and can_move(gr, gc, "r"):
      mvs.append("r")
    if mvs!=[]:
      return choice(mvs)
    targets.pop(0)
    print("target removed", targets)

def move_ghost(d):
  global gr, gc
  gr, gc=get_next_loc(gr, gc, d)
  move_img_to_cell("g", gr, gc)

if __name__=="__main__":
  start()
=======
def on_timeout_t1():
  update_ghost()

def get_escape_moves():
  mvs=["u", "d", "l", "r"]
  rs=[]
  d=get_dist(gr, gc, pm.r, pm.c)
  for m in mvs:
    nr, nc=get_next_loc(gr, gc, m)
    if can_move(gr, gc, m) and get_dist(nr, nc, pm.r, pm.c)>d:
      rs.append(m)
  if rs==[]:
    for m in mvs:
      if can_move(gr, gc, m):
        rs.append(m)
  return rs

if __name__=="__main__":
  print(get_escape_moves())
  #start()

>>>>>>> a5725fc69171f4f133c6f5665e8862621eb06c0a
