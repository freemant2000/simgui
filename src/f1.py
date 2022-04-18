from simgui import *

url="http://clipart-library.com/images/qcBX57Bxi.jpg"

def on_ready():
  add_graphics_view(400, 300)
  add_gi_img("ball", 100, 200, 50, 50, url)

def on_key():
  remove_gi("ball")

start(globals())
