from board import *
from pacman import *

def on_ready():
  add_graphics_view(400, 300)
  draw_obj(g, pm)
  
start()
