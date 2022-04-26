from simgui import *

def on_ready():
  add_graphics_view(400, 300)
  add_gi_rect("r1", 200, 70, 100, 20, "yellow")
  print(gi_exists("r1"))
  print(gi_exists("r2"))

start(globals())
