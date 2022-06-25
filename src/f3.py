from simgui import *

r=1
c=2
w=30
h=30

def on_ready():
  add_graphics_view(400, 300)
  add_gi_img("pm", c*w, r*h, w, h, "pacman.png")

def on_key():
  global r, c
  k=get_key()
  if k=="Right":
    c=c+1
  elif k=="Left":
    c=c-1
  elif k=="Up":
    r=r-1
  elif k=="Down":
    r=r+1
  set_gi_pos("pm", c*w, r*h)

start()
