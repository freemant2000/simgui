from simgui import *
from pacman import *
from board import *
from maze import *

class Game:
  pass
gm=Game()

def on_ready():
  add_graphics_view(400, 300)
  gm.g=make_grid(400, 300)
  gm.m=make_maze(gm.g, True)
  gm.pm=make_pm(gm.g, 1, 2)

def on_key():
  k=get_key()
  d=k[0].lower()
  if d==gm.pm.face and can_move_in_maze(gm.m, gm.pm.r, gm.pm.c, d):
    move_pm(gm.pm, d)
  else:
    set_pm_face(gm.pm, d)

start()
