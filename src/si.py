from simgui import *

def on_ready():
  add_graphics_view(400, 300)
  add_gi_img("a1", 100, 30, 50, 30, "alien.png")
  add_gi_img("c", 200, 240, 30, 40, "cannon.png")

def on_key():
  k=get_key()
  if k=="Left":
    set_gi_pos("c", get_gi_x("c")-5, get_gi_y("c"))
  elif k=="Right":
    set_gi_pos("c", get_gi_x("c")+5, get_gi_y("c"))
  elif k==" ":
    add_gi_img("b", 100, 100, 10, 15, "bullet.png")
start(globals())