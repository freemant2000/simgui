from simgui import *

def on_ready():
  add_graphics_view(400, 300)

def on_key():
  n=make_unique_name("rect")
  add_gi_rect(n, 200, 70, 100, 20, "yellow")
  send_data_to_future(n, 2)

def on_data_from_past(data):
  n=data
  x=get_gi_x(n)
  y=get_gi_y(n)
  set_gi_pos(n, x, y-5)

start(globals())
