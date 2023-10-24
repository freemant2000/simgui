from simgui import *

n=70

def on_ready():
  add_graphics_view(400, 300)
  add_gi_rect("r", 10, 20, 50, 100, (0, n, 0))
  add_gi_cir("c", 200, 20, 60, (0, 0, n))
  add_label("a", "Hello")
  set_wid_color("a", (n, 0, 0))

def on_key():
  global n
  k=get_key()
  if k=="Up":
    n=n+10
    if n>255:
      n=0
    set_gi_color("r", (0, n, 0))
    set_gi_color("c", (0, 0, n))
    set_wid_color("a", (n, 0, 0))

start()
