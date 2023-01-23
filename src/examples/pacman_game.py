from simgui import *
from walls import make_vwalls, make_hwalls
from ghost import make_ghost, update_ghost
import pacman as pm
from pellets import make_pellets

def on_ready():
  add_graphics_view(400, 300)
  add_label("s", "0")
  pm.make_pacman()
  make_ghost()
  make_vwalls()
  make_hwalls()
  make_pellets()
  start_timer("t1", 0.4)
  start_timer("t2", 0.5)

def on_key():
  k=get_key()
  if k=="Left":
    pm.set_direction("l")
  elif k=="Right":
    pm.set_direction("r")
  elif k=="Up":
    pm.set_direction("u")
  elif k=="Down":
    pm.set_direction("d")

def on_timeout_t1():
  pm.change_look()
  pm.move_pacman()
  set_label_text("s", pm.score)

def on_timeout_t2():  
  update_ghost()

start()
