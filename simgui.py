from PySide2.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QApplication, QHBoxLayout, QGridLayout

class SimGuiApp(QApplication):
    def __init__(self) -> None:
        super().__init__()
        self.mod=None
    def start(self, mod):
        self.mod=mod
        self.wid_dict={}
        self.auto_row=0
        wid=QWidget()
        self.lo=QGridLayout()
        wid.setLayout(self.lo)
        self.call_handler("on_ready")
        wid.show()
        self.exec_()
    def call_handler(self, fn):
        handler=self.mod.get(fn)
        if handler:
          handler()
    def add_label(self, name, text):
        lbl=QLabel(text)
        self.wid_dict[name]=lbl
        self.lo.addWidget(lbl, self.auto_row, 0)
        self.auto_row+=1
    def add_button(self, name, text):
        btn=QPushButton(text)
        def on_click():
          self.call_handler("on_click_"+name)
        btn.clicked.connect(on_click)
        self.wid_dict[name]=btn
        self.lo.addWidget(btn, self.auto_row, 0)
        self.auto_row+=1
    def set_label_text(self, name, text):
      self.get_wid(name).setText(str(text))
    def get_wid(self, name):
      if name in self.wid_dict:
        return self.wid_dict[name]
      else:
        raise ValueError(f"no label named {name}", name)
    def add_input(self, name):
        edit=QLineEdit()
        def on_edited():
          self.call_handler("on_edited_"+name)
        edit.textEdited.connect(on_edited)
        self.wid_dict[name]=edit
        self.lo.addWidget(edit, self.auto_row, 0)
        self.auto_row+=1
    def get_input_text(self, name):
      inp=self.get_wid(name)
      return inp.text()
    def set_input_text(self, name, text):
      self.get_wid(name).setText(text)

sgapp=SimGuiApp()

def start(mod):
    sgapp.start(mod)

def add_label(name, text):
    sgapp.add_label(name, text)

def set_label_text(name, text):
    sgapp.set_label_text(name, text)

def add_button(name, text):
    sgapp.add_button(name, text)    

def add_input(name):
    sgapp.add_input(name)    

def get_input_text(name):
    return sgapp.get_input_text(name)        

def set_input_text(name, text):
    return sgapp.set_input_text(name, text)            