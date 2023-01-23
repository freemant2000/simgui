from simgui import *
from random import randint

coin_url="https://www.iconpacks.net/icons/1/free-coin-icon-794-thumb.png"
coins=[]
score=0
c=0
intv=2
lives=3

def on_ready():
  add_label("s", score)
  add_graphics_view(400, 300)
  add_gi_img("b", 200, 240, 30, 40, "bucket.png")
  show_lives()
  start_timer("t1", 0.2)
  start_timer("t2", intv)

def show_lives():  
  i=1
  while i<=lives:
    add_gi_img("b"+str(i), 5+(i-1)*15, 10, 10, 13, "bucket.png")
    i=i+1

def on_key():
  move_bucket()
  k=get_key()

def cleanup_coins():
  while coins!=[]:
    n=coins[0]
    y=get_gi_y(n)
    if y>=300:
      coins.pop(0)
      remove_gi(n)
      die()
    else:
      break

def die():  
  global lives
  hide_lives()
  lives=lives-1
  show_lives()
  if lives<=0:
    play_wav("gameover.wav")
    msg_box("Game over")
    quit()

def hide_lives():
  i=1
  while i<=lives:
    remove_gi("b"+str(i))
    i=i+1

def move_bucket():
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
  speed_up()
  n=make_unique_name("coin")
  coins.append(n)
  x=randint(50, 350)
  add_gi_img(n, x, 30, 50, 50, coin_url)

def speed_up():
  global c, intv
  c=c+1
  if c==5:
    c=0
    intv=intv-0.05
    stop_timer("t2")
    start_timer("t2", intv)

def on_timeout_t1():
  move_coins()
  cleanup_coins()
  collect_coins()

def collect_coins():
  global score
  i=0
  while i<len(coins):
    n=coins[i]
    if are_gi_overlap(n, "b"):
      coins.pop(i)
      remove_gi(n)
      play_wav("click.wav")
      score=score+1
      set_label_text("s", score)
    else:
      i=i+1

def move_coins():
  for n in coins:
    x=get_gi_x(n)
    y=get_gi_y(n)
    set_gi_pos(n, x, y+5)

start()