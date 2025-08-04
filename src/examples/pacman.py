from board import *

class Pacman:
  pass

def make_pm(g, r, c):
  pm=Pacman()
  pm.g=g
  pm.r=r
  pm.c=c
  pm.look=0
  pm.face="r"
  add_img(pm.g, "pm", pm.r, pm.c, "pacman-r0.png")
  return pm

def move_pm(pm, d):
  if can_move(pm.g, pm.r, pm.c, d):
    if d=="l":
      pm.c=pm.c-1
    elif d=="r":
      pm.c=pm.c+1
    elif d=="u":
      pm.r=pm.r-1
    elif d=="d":
      pm.r=pm.r+1
    pm.look=1-pm.look
    move_img(pm.g, "pm", pm.r, pm.c)
    set_gi_img("pm", f"pacman-{pm.face}{pm.look}.png")

def set_pm_face(pm, d):
  pm.face=d
  set_gi_img("pm", f"pacman-{pm.face}{pm.look}.png")