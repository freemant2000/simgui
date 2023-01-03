from simgui import *

vwalls=[[False, False, False, True, False, False, False, False, True, False, False, False], \
        [True, True, False, False, False, True, True, False, False, False, True, True], \
        [False, True, False, False, False, False, False, False, False, False, True, False], \
        [False, False, False, False, False, False, False, False, False, False, False, False], \
        [False, True, False, True, False, False, False, False, True, False, True, False], \
        [True, True, False, True, False, False, False, False, True, False, True, True], \
        [True, False, False, False, False, False, False, False, False, False, False, True], \
        [False, False, True, False, False, False, False, False, False, True, False, False], \
        [False, False, False, False, False, True, True, False, False, False, False, False], \
        [False, True, False, False, False, False, False, False, False, False, True, False]]
hwalls=[[False, False, False, False, False, False, False, False, False, False, False, False, False], \
        [True, False, False, False, True, True, False, True, True, False, False, False, True], \
        [False, False, True, False, False, False, True, False, False, False, True, False, False], \
        [False, False, True, False, True, True, False, True, True, False, True, False, False], \
        [False, False, False, False, False, False, False, False, False, False, False, False, False], \
        [False, False, False, False, True, True, True, True, True, False, False, False, False,], \
        [True, False, False, False, False, False, True, False, False, False, False, False, True], \
        [False, False, True, True, False, False, False, False, False, True, True, False, False], \
        [False, False, True, False, True, True, False, True, True, False, True, False, False]]

def make_hwalls():
  r=0
  while r<len(hwalls):
    w=0
    if len(hwalls[r])!=len(hwalls[0]):
      print("error hwall", r)    
    while w<len(hwalls[r]):
      if hwalls[r][w]:
        draw_hwall(r, w)
      w=w+1
    r=r+1

def make_vwalls():
  r=0
  while r<len(vwalls):
    w=0
    if len(vwalls[r])!=len(vwalls[0]):
      print("error", r)
    while w<len(vwalls[r]):
      if vwalls[r][w]:
        draw_vwall(r, w)
      w=w+1
    r=r+1

def draw_hwall(r, w):
  x=w*30
  y=(r+1)*30
  add_gi_rect(f"hw{r}-{w}", x, y-2/2, 30, 2, "red")

def draw_vwall(r, w):
  x=(w+1)*30
  y=r*30
  add_gi_rect(f"vw{r}-{w}", x-2/2, y, 2, 30, "red")

def can_move(r, c, d):
  return not is_blocked(r, c, d)

def is_blocked(r, c, d):
  if d=="l":
    return c==0 or vwalls[r][c-1]
  elif d=="r":
    return c==12 or vwalls[r][c]
  elif d=="u":
    return r==0 or hwalls[r-1][c]
  elif d=="d":
    return r==9 or hwalls[r][c]
