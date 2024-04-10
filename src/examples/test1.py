from simgui import *

def on_ready():
  add_graphics_view(400, 300)
  b=make_button("OK")
  b.on_click(my_f)

def my_f():
  make_gi_cir(-40, -40, 40, "red")

start()
