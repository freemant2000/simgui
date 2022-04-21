from simgui import *

def on_ready():
  add_graphics_view(400, 300)
  i=1
  while i<=3:
    add_gi_img("b"+str(i), 200+(i-1)*50, 240, 30, 40, "bucket.png")
    i=i+1

start(globals())
