from simgui import *

def on_ready():
  add_graphics_view(400, 300)
  add_gi_img("a1", 100, 30, 50, 30, "alien.png")
  add_gi_img("c", 200, 240, 30, 40, "cannon.png")

def on_key():
  move_cannon()
  open_fire()

def move_cannon():
  k=get_key()
  if k=="Left":
    set_gi_pos("c", get_gi_x("c")-5, get_gi_y("c"))
  elif k=="Right":
    set_gi_pos("c", get_gi_x("c")+5, get_gi_y("c"))

def open_fire():
  k=get_key()
  if k==" ":
    n=make_unique_name("bullet")
    x=get_gi_x("c")+30/2-10/2
    y=get_gi_y("c")-15
    add_gi_img(n, x, y, 10, 15, "bullet.png")


start(globals())