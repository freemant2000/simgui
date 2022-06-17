from simgui import *

a=12

def on_ready():
  add_button("b1", a)
  add_label("a1", "hi")
  set_label_text("a1", "abc")
  set_button_text("a1", "abc2")
start()
