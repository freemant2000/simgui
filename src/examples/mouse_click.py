from simgui import *

def on_ready():
  add_graphics_view(400, 300)

def on_mouse():
  x=get_mouse_x()
  y=get_mouse_y()
  print(get_mouse_btn())
  make_gi_cir(x-20, y-20, 40, "red")

start()

