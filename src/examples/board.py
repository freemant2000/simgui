from simgui import *
class Grid:
  pass

def make_grid(w, h):
  g=Grid()
  g.w, g.h=w, h
  g.cell_w=30
  g.cell_h=30
  g.mgn=3
  return g

def check_col(g, c):
  return c>=0 and c<g.w//g.cell_w

def check_row(g, r):
  return r>=0 and r<g.h//g.cell_h

def can_move(g, r, c, d):
  return not((r==0 and d=="u") or 
             (r==g.h//g.cell_h-1 and d=="d") or 
             (c==0 and d=="l") or 
             (c==g.w//g.cell_w-1 and d=="r"))

def add_img(g, n, r, c, fn):
  add_gi_img(n, cell_x(g, c)+g.mgn, cell_y(g, r)+g.mgn,
             g.cell_w-2*g.mgn, g.cell_h-2*g.mgn, fn)
def move_img(g, n, r, c):
  set_gi_pos(n, cell_x(g, c)+g.mgn, cell_y(g, r)+g.mgn)

def cell_x(g, c):
  return g.cell_w*c
def cell_y(g, r):
  return g.cell_h*r

def get_next_loc(loc, d):
  r, c=loc
  if d=="u":
    return (r-1, c)
  elif d=="d":
    return (r+1, c)
  elif d=="l":
    return (r, c-1)
  elif d=="r":
    return (r, c+1)

def get_last_loc(loc, ds):
  for d in ds:
    loc=get_next_loc(loc, d)
  return loc
