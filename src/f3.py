from simgui import *

coin_url="https://www.iconpacks.net/icons/1/free-coin-icon-794-thumb.png"

def on_ready():
  add_graphics_view(400, 300)
  add_gi_img("abc", 60, 30, 50, 50, coin_url)
  n=input()
  x=get_gi_x(n)
  y=get_gi_y(n)
  print(x, y)
  set_gi_pos("abc", x, y+5)

start(globals())
