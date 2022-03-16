from simgui import *

ball_url="http://clipart-library.com/images/qcBX57Bxi.jpg"

def on_ready():
  add_graphics_view(400, 300)
  add_gi_img("ball", 100, 30, 50, 50, ball_url)
  start_timer("t1", 0.03)

def on_timeout_t1():
  set_gi_pos("ball", get_gi_x("ball")+5, get_gi_y("ball"))

def on_key():
  k=get_key()
  if k=="Right":
    set_gi_pos("ball", get_gi_x("ball")+5, get_gi_y("ball"))
  elif k=="Left":
    set_gi_pos("ball", get_gi_x("ball")-5, get_gi_y("ball"))  
start(globals())
