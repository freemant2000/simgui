from simgui import *
class MyData:
  pass

d=MyData()
d.s=3

def on_ready():
  add_graphics_view(400, 300)
  add_gi_rect("r", 100, 30, 50, 50, "red")
  start_timer("t1", 0.1)

def on_timeout_t1():
  if get_gi_x("r")+d.s<0:
    d.s=3
  if get_gi_x("r")+d.s+50>400:
    d.s=-3
  x=get_gi_x("r")
  y=get_gi_y("r")
  set_gi_pos("r", x+d.s, y)


start()
