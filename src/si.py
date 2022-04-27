from os import kill
from simgui import *

sx=6
bullets=[]

def on_ready():
  add_graphics_view(400, 300)
  add_gi_img("a1", 100, 30, 50, 30, "alien.png")
  add_gi_img("c", 200, 240, 30, 40, "cannon.png")
  start_timer("t1", 0.05)

def on_timeout_t1():
  move_bullet()
  kill_alien()
  move_alien()

def move_alien():
  if gi_exists("a1"):
    bounce_alien()
    x=get_gi_x("a1")+sx
    y=get_gi_y("a1")
    set_gi_pos("a1", x, y)
    capture_cannon()

def capture_cannon():
  if are_gi_overlap("a1", "c"):
    play_wav("gameover.wav")
    msg_box("Game Over")
    quit()

def bounce_alien():  
  global sx
  next_right_x=get_gi_x("a1")+50+sx
  if next_right_x>=400:
    sx=-abs(sx)
    move_alien_down()
  next_left_x=get_gi_x("a1")+sx
  if next_left_x<0:
    sx=abs(sx)
    move_alien_down()

def move_alien_down():    
  x=get_gi_x("a1")
  y=get_gi_y("a1")+30
  set_gi_pos("a1", x, y)

def move_bullet():
  i=0
  while i<len(bullets):
    n=bullets[i]
    x=get_gi_x(n)
    y=get_gi_y(n)-5
    set_gi_pos(n, x, y)
    if y<0:
      remove_gi(n)
      bullets.pop(i)
    else:
      i=i+1

def kill_alien():
  if gi_exists("a1"):
    for n in bullets:
      if are_gi_overlap(n, "a1"):
        ex=get_gi_x("a1")+50/2-60/2
        ey=get_gi_y("a1")+30/2-60/2
        add_gi_img("e", ex, ey, 60, 60, "explosion.png")
        remove_gi(n)
        remove_gi("a1")
        bullets.remove(n)
        break

def on_key():
  move_cannon()
  open_fire()

def move_cannon():
  k=get_key()
  if k=="Left":
    set_gi_pos("c", get_gi_x("c")-5, get_gi_y("c"))
  elif k=="Right":
    set_gi_pos("c", get_gi_x("c")+5, get_gi_y("c"))

def open_fire():
  k=get_key()
  if k==" ":
    x=get_gi_x("c")+30/2-10/2
    y=get_gi_y("c")-15
    n=make_unique_name("bullet")    
    bullets.append(n)
    add_gi_img(n, x, y, 10, 15, "bullet.png")


start(globals())