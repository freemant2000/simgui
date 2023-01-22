from simgui import *
from board import get_cell_center, board_w, board_h, max_r, max_c

pellets=[]

def on_ready():
  add_graphics_view(400, 300)
  make_pellets()


def eat_pellet(r, c):
  if pellets[r][c]>0:
    pellets[r][c]=0
    remove_gi(f"p-{r}-{c}")

def make_pellets():  
  init_pellets()
  r=0
  while r<len(pellets):
    c=0
    while c<len(pellets[r]):
      make_pellet(f"p-{r}-{c}", r, c, pellets[r][c]==2)
      c=c+1
    r=r+1

def make_pellet(name, r, c, is_power):
  rad=5
  x, y=get_cell_center(r, c)
  c="purple"
  if is_power:
    c="green"
  add_gi_cir(name, x-rad, y-rad, rad, c)

def init_pellets():
  for r in range(board_h):
    row=[]
    for c in range(board_w):
      row.append(1)
    pellets.append(row)
  r,c=randint(0, max_r), randint(0, max_c)
  pellets[r][c]=2

if __name__=="__main__":
  start()