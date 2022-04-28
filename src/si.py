from os import kill
from simgui import *

sx=6
bullets=[]
aliens=[]

def on_ready():
  add_graphics_view(400, 300)
  make_aliens()
  add_gi_img("c", 200, 240, 30, 40, "cannon.png")
  start_timer("t1", 0.05)

def make_aliens():
  for a in range(0, 3):
    for b in range(0, 2):
      an=make_unique_name("a")
      aliens.append(an)
      add_gi_img(an, 100+a*80, 20+b*50, 50, 30, "alien.png")

def on_timeout_t1():
  move_bullet()
  kill_alien()
  move_alien()

def move_alien():
  bounce_alien()
  for an in aliens:
    x=get_gi_x(an)+sx
    y=get_gi_y(an)
    set_gi_pos(an, x, y)
  capture_cannon()
    
def capture_cannon():
  for an in aliens:
    if are_gi_overlap(an, "c"):
      play_wav("gameover.wav")
      msg_box("Game Over")
      quit()

def bounce_alien():  
  global sx
  for an in aliens:
    next_right_x=get_gi_x(an)+50+sx
    if next_right_x>=400:
      sx=-abs(sx)
      move_alien_down()
      break
    next_left_x=get_gi_x(an)+sx
    if next_left_x<0:
      sx=abs(sx)
      move_alien_down()
      break

def move_alien_down():    
  for an in aliens:
    x=get_gi_x(an)
    y=get_gi_y(an)+30
    set_gi_pos(an, x, y)

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
  for an in aliens:
    hit=False
    for n in bullets:
      if are_gi_overlap(n, an):
        hit=True
        break
    if hit:
      show_explosion(an)
      remove_gi(n)
      remove_gi(an)
      bullets.remove(n)
      aliens.remove(an)

def show_explosion(an):
  ex=get_gi_x(an)+50/2-60/2
  ey=get_gi_y(an)+30/2-60/2
  en=make_unique_name("e")
  add_gi_img(en, ex, ey, 60, 60, "explosion.png")
  send_data_to_future(en, 0.1)

def on_data_from_past(data):
  remove_gi(data)

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