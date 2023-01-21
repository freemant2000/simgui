from board import add_img_in_cell, move_img_to_cell, get_next_loc
from walls import can_move
from simgui import *

#r, c=1, 2
r, c=3, 2
facing, look="r", 0

def get_img_name():
  return "pacman-"+facing+str(look)+".png"

def make_pacman():
  add_img_in_cell("pm", r, c, get_img_name())

def set_direction(d):
  global facing, look
  facing, look=d, 0

def change_look():
  global look
  look=look+1
  if look>1:
    look=0
  #set_gi_img("pm", get_img_name())  

def move_pacman():
  global r, c
  if can_move(r, c,  facing):
    r, c=get_next_loc(r, c, facing)
    move_img_to_cell("pm", r, c)

