from simgui import *
from random import randint

ball_url="http://clipart-library.com/images/qcBX57Bxi.jpg"

s=randint(3, 5)
t=s-randint(1, 2)
if randint(0, 1)==0:
  s=-s
if randint(0, 1)==0:
  t=-t

def on_ready():
  add_graphics_view(400, 300)
  add_gi_img("ball", 100, 30, 50, 50, ball_url)
  start_timer("t1", 0.03)
  add_gi_img("r", 350, 100, 30, 100, "racquet.png")
  add_gi_img("s", 5, 100, 30, 100, "racquet.png")  

def on_timeout_t1():
  auto_bounce()
  check_game_over()
  set_gi_pos("ball", get_gi_x("ball")+s, get_gi_y("ball")+t)
  hit_by_racquet()

def check_game_over():
  new_x=get_gi_x("ball")+s
  if new_x<0 or new_x+50>400:
    msg_box("Game over")
    quit()
    
def auto_bounce():
  global t
  new_y=get_gi_y("ball")+t
  if new_y<0:
    t=abs(t)
  if new_y+50>300:
    t=-abs(t)  

def hit_by_racquet():
  global s
  if are_gi_overlap("ball", "s"):
    s=abs(s)+0.2
  if are_gi_overlap("ball", "r"):
    s=-abs(s)-0.2
    
def on_key():
  global s
  k=get_key()
  if k=="Up":
    set_gi_pos("r", get_gi_x("r"), get_gi_y("r")-5)
  elif k=="Down":
    set_gi_pos("r", get_gi_x("r"), get_gi_y("r")+5)
  elif k=="e":
    set_gi_pos("s", get_gi_x("s"), get_gi_y("s")-5)
  elif k=="x":
    set_gi_pos("s", get_gi_x("s"), get_gi_y("s")+5)

start()