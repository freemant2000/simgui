from simgui import *

w=100
h=30
def on_ready():
  add_graphics_view(400, 300)
  add_gi_rect("r1", 200, 70, w, h, "blue")

def on_key():
  add_gi_rect("r2", 
    get_gi_x("r1")-20,\
    get_gi_y("r1")+h/2-10/2,\
    20, 10, "yellow")

start(globals())
