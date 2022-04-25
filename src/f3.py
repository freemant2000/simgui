from simgui import *

def on_ready():
  add_graphics_view(400, 300)
  add_gi_rect("r1", 200, 70, 100, 30, "blue")
  print(get_gi_x("r1"), get_gi_y("r1"))

start(globals())
