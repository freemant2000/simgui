from simgui import *

r, c=None, None

def on_ready():
  global r, c
  add_graphics_view(400, 300)
  r=add_gi_rect("", 100, 200, 60, 20, "red")
  c=add_gi_img("", 40, 100, 40, 40, "pacman-l0.png")
  make_gi_polygon([(20, 30), (140, 90), (60, 120)], "blue")

def on_key():
  k=get_key()
  if k=="Left":
    r.set_gi_pos(r.get_gi_x()-5, r.get_gi_y())
  elif k=="Right":
    r.set_gi_pos(r.get_gi_x()+5, r.get_gi_y())
  elif k=="Up":
    c.set_gi_img("pacman-l1.png")

start()