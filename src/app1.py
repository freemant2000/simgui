from simgui import *

def on_ready():
    add_label("l1", "Hello")
    add_label("l2", "Hi")
    add_input("i1", cols=2)
    add_input("i2")
    add_button("b1", "OK")
    go_back_row()
    add_button("b2", "Cancel", col=1)
    add_combo("cb1")
    add_combo_item("cb1", "chicken")
    add_combo_item("cb1", "beef")
    add_combo_item("cb1", "beans")


def on_click_b1():
    set_label_text("l2", 333)

def on_edited_i1():
    set_input_text("i2", get_input_num("i1")+1)

def on_index_changed_cb1():
    print("hiiii")

start(globals())

