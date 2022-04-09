from simgui import *

ball_url="http://clipart-library.com/images/qcBX57Bxi.jpg"

s=5
def on_ready():
  add_graphics_view(400, 300)
  add_gi_img("ball", 100, 30, 50, 50, ball_url)
  start_timer("t1", 0.03)
  add_gi_img("r", 300, 30, 30, 100, "racquet.png")

def on_timeout_t1():
  global s
  new_x=get_gi_x("ball")+s
  if new_x<0:
    s=abs(s)
  if new_x+50>400:
    s=-abs(s)
  set_gi_pos("ball", get_gi_x("ball")+s, get_gi_y("ball"))

def on_key():
  global s
  k=get_key()
  if k=="Left":
    s=-abs(s)
  elif k=="Right":
    s=abs(s)

start(globals())