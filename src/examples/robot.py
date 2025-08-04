from simgui import *

class Robot:
  pass

def make_robot(x, y):
  r=Robot()
  r.x, r.y=x, y
  r.g1=make_gi_rect(r.x+(100-40)/2, r.y, 40, 30, "green")
  r.g2=make_gi_rect(r.x, r.y+30, 100, 70, "green")
  return r

def move_h_robot(r):
  r.x=r.x+5
  r.g1.set_gi_pos(r.x+(100-40)/2, r.y)
  r.g2.set_gi_pos(r.x, r.y+30)
