from simgui import *

ball_url="http://clipart-library.com/images/qcBX57Bxi.jpg"
class MyData:
  pass
d=MyData()
d.s=5

def on_ready():
  add_graphics_view(500, 300)
  add_gi_img("ball", 100, 30, 50, 50, ball_url)
  start_timer("t1", 0.03)

def on_timeout_t1():
  would_be_x=get_gi_x("ball")+d.s
  if would_be_x<0:
    d.s=abs(d.s)
  if would_be_x+50>500:
    d.s=-abs(d.s)
  set_gi_pos("ball", get_gi_x("ball")+d.s, get_gi_y("ball"))

start()
