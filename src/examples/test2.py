from simgui import *
def on_ready():
  add_graphics_view(400, 300)
  w=get_win()
  w.x=100
  w.y=260
  w.x2=300
  w.y2=260
  w.a=make_gi_rect(w.x, w.y, 40, 40, "yellow")
  w.b=make_gi_rect(w.x2, w.y2, 40, 40, "red")


def on_key():
  w=get_win()
  r=randint(3, 6)
  k=get_key()
  if k=="e":
    w.y=w.y-r
    w.a.set_gi_pos(w.x, w.y)
  elif k=="i":
    w.y2=w.y2-r
    w.b.set_gi_pos(w.x2, w.y2)

start()

