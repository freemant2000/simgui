from simgui import *
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

def on_ready():
  add_graphics_view(400, 300)
  make_ghost()
  make_vwalls()
  make_hwalls()
  start_timer("t1", 0.4)

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

