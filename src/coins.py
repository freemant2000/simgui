from simgui import *
from random import randint

coin_url="https://www.iconpacks.net/icons/1/free-coin-icon-794-thumb.png"
coins=[]

def on_ready():
  add_graphics_view(400, 300)
  add_gi_img("b", 200, 240, 30, 40, "bucket.png")
  start_timer("t1", 0.2)
  start_timer("t2", 2)

def on_key():
  k=get_key()
  if k=="Left":
    x=get_gi_x("b")
    new_right_x=x+30-1-5
    if new_right_x>=0:
      set_gi_pos("b", x-5, 240)
  elif k=="Right":
    x=get_gi_x("b")
    new_x=x+5
    if new_x<=399:
      set_gi_pos("b", x+5, 240)

def on_timeout_t2():
  n=make_unique_name("coin")
  coins.append(n)
  x=randint(50, 350)
  add_gi_img(n, x, 30, 50, 50, coin_url)

def on_timeout_t1():
  for n in coins:
    x=get_gi_x(n)
    y=get_gi_y(n)
    set_gi_pos(n, x, y+5)

start(globals())