from simgui import *

coin_url="https://www.iconpacks.net/icons/1/free-coin-icon-794-thumb.png"
coins=["coin1", "coin2", "coin3"]

def on_ready():
  add_graphics_view(400, 300)
  i=0
  x=100
  while i<len(coins):
    add_gi_img(coins[i], x, 30, 50, 50, coin_url)
    i=i+1
    x=x+50

start(globals())