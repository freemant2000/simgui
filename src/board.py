from simgui import *

w, h=30, 30
mg=3
cnt_w, cnt_h=w-2*mg, h-2*mg

def cnt_x(c):
  return c*w+mg

def cnt_y(r):
  return r*h+mg

def add_img_in_cell(item_name, r, c, img_name):
  add_gi_img(item_name, cnt_x(c), cnt_y(r), cnt_w, cnt_h, img_name)

def move_img_to_cell(item_name, r, c):
  set_gi_pos(item_name, cnt_x(c), cnt_y(r))

def get_dist(r1, c1, r2, c2):
  return abs(r2-r1)+abs(c2-c1)

def get_next_loc(r, c, d):
  nr, nc=r, c
  if d=="u":
    nr=r-1
  elif d=="d":
    nr=r+1
  elif d=="l":
    nc=c-1
  elif d=="r":
    nc=c+1
  return (nr, nc)

print(get_next_loc(2, 1, "l"))
