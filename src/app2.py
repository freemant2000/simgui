from simgui import *

b="dinosaur"
s="mosquito"

def on_ready():
  add_button("b1", "Big")
  add_button("b2", "Small")
  add_label("a1", "4")

def on_click_b1():
  set_label_text("a1", b)

def on_click_b2():
  set_label_text("a1", s)

start(globals())
