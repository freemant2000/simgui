from simgui import *

def on_ready():
  a=get_win()
  a.r=100
  a.b=make_button("Hi")
  a.b.on_click(my_f)


def my_f():  
  a=get_win()
  a.r=a.r+10
  a.b.set_wid_color([a.r, a.r, a.r])

start()
