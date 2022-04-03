from simgui import *
from random import randint

coin_url="https://www.iconpacks.net/icons/1/free-coin-icon-794-thumb.png"
coins=[]

def on_key():
  n="coin"+str(randint(0, 10000))
  coins.append(n)
  x=randint(50, 350)
  add_gi_img(n, x, 30, 50, 50, coin_url)
 
def on_ready():
  add_graphics_view(400, 300)
  start_timer("t1", 0.2)

def on_timeout_t1():
  for n in coins:
    x=get_gi_x(n)
    y=get_gi_y(n)
    set_gi_pos(n, x, y+5)

start(globals())