from simgui import *
w=100
h=30
def on_ready():
  add_graphics_view(400, 300)
  add_gi_rect("r1", 200, 70, w, h, "blue")
  send_data_to_future("r1", 4)

def on_data_from_past(data):
  print(data)

start(globals())
