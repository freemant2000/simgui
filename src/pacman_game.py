from simgui import *
from walls import make_vwalls, make_hwalls
from ghost import make_ghost, update_ghost
from pacman import *

def on_ready():
  add_graphics_view(400, 300)
  make_pacman()
  make_ghost()
  make_vwalls()
  make_hwalls()
  start_timer("t1", 0.4)
  start_timer("t2", 0.5)

def on_timeout_t1():
  change_look()
  move_pacman()

def on_timeout_t2():  
  update_ghost()

def on_key():
  k=get_key()
  if k=="Left":
    set_direction("l")
  elif k=="Right":
    set_direction("r")
  elif k=="Up":
    set_direction("u")
  elif k=="Down":
    set_direction("d")
