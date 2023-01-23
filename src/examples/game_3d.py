from simgui import *
from simgui.transforms import *

# def draw_polygon(pts, color=None):
#   draw_poly_line(pts+[pts[0]], color)

# def draw_poly_line(pts, color=None):
#   i=0
#   while i<len(pts)-1:
#     draw_line(pts[i], pts[i+1], color)
#     i=i+1

# def draw_line(pt1, pt2, color=None):
#   if color:
#     pencolor(color)
#   penup()
#   x, y=pt1
#   goto(x, y)
#   pendown()
#   x, y=pt2
#   goto(x, y)

#draw_polygon([(50, 50), (200, 100), (100, -200)], "blue")

r=0
c=0

def on_ready():
  add_graphics_view(400, 300, (1000, 900))
  make_tilts()
  pt=get_monster_loc()
  add_gi_img("pm", pt[0], pt[1], 60, 60, "pokemon.png")

def get_monster_loc():  
  base_x=c*200
  base_z=-r*200
  pt=(base_x+120, 30, base_z-250)
  pt=to_canvas(pt)
  return (pt[0]-30, pt[1]-30)

def to_canvas(pt):
  tr=Trans3D(300, 500, 100)
  rt=RoateX3D(-30)
  p=Project3D(-120)
  m=Map2D((-80, -10-80), (150-10, 50-30), (0, 300), (400, 0))  
  return m.map(p.proj(rt.rot(tr.trans(pt))))
  
def on_key():
  global r, c
  k=get_key()
  if k=="Left":
    c-=1
    x, y=get_monster_loc()
    set_gi_pos("pm", x, y)
  elif k=="Right":
    c+=1
    x, y=get_monster_loc()
    set_gi_pos("pm", x, y)
  if k=="Up":
    r+=1
    x, y=get_monster_loc()
    set_gi_pos("pm", x, y)
  elif k=="Down":
    r-=1
    x, y=get_monster_loc()
    set_gi_pos("pm", x, y)

def make_tilts():
  for i in range(4):
    for j in range(4):
      base_x=i*200
      base_z=-j*200
      pts=[(base_x+20, 30, base_z-150), (base_x+220, 30, base_z-150), (base_x+220, 30, base_z-350), (base_x+20, 30, base_z-350)]
      ppts=[to_canvas(pt) for pt in pts]
      add_gi_polygon(f"p{i}{j}", ppts, "yellow")

start()