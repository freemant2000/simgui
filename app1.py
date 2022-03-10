from simgui import *

def on_ready():
    add_label("l1", "Hello")
    add_label("l2", "Hi")
    add_input("i1")
    add_input("i2")
    add_button("b1", "OK")

def on_click_b1():
    set_label_text("l2", 333)

def on_edited_i1():
    set_input_text("i2", get_input_num("i1")+1)

start(globals())

