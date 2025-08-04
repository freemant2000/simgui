from simgui import *

def on_ready():
  add_graphics_view(400, 300)

def on_mouse():
  x=get_mouse_x()
  y=get_mouse_y()
  make_gi_rect(x-50, y-30, 100, 60, "red")

start()
