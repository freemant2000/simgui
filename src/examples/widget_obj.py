from simgui import *

lbl=None
inp=None
cb=None

def on_ready():
    global lbl, inp, cb
    lbl=add_label("", "Number")
    inp=add_input(None, right=True)
    inp.on_edited(handler1)
    cb=add_combo("", cols=2)
    cb.add_combo_item("chicken")
    cb.add_combo_item("beef")
    cb.add_combo_item("beans")
    cb.on_index_changed(handler3)
    b1=add_button("", "OK")
    b1.on_click(handler2)

def handler2():
    lbl.set_label_text(333)

def handler1():
    lbl.set_wid_color((inp.get_input_num(), 0, 0))

def handler3():
    print(cb.get_combo_text()+" is selected")

start()  # must do this to kick start the app with the UI
