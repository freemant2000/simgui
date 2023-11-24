from simgui import *

b="dinosaur"
s="mosquito"

def on_ready():
  add_button("b1", "Big")
  add_button("b2", "Small")
  add_label("a1", "4")
  set_wid_size("a1", 200, 160)
  add_graphics_view(400, 300)
  add_gi_img("p1", 50, 50, 200, 160, "https://media.gettyimages.com/illustrations/tyrannosaurus-rex-dinosaur-illustration-id99311107?s=612x612")
  add_gi_rect("p2", 10, 10, 40, 30, "blue")
  
#def on_key():
#  print(get_key())

def on_click_b1():
  #set_label_text("a1", b)
  set_label_img("a1", "https://media.gettyimages.com/illustrations/tyrannosaurus-rex-dinosaur-illustration-id99311107?s=612x612")
  set_wid_color("a1", "blue")

def on_click_b2():
  set_label_img("a1", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTbCuwaTTtDhzHqojo_s7elgql5ZIOo1Grg7g&usqp=CAU")
  set_wid_color("a1", "green")

start(globals())
