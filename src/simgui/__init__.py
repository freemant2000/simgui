from PySide2.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QApplication, QComboBox, QGridLayout, QMessageBox
from PySide2.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsPixmapItem, QGraphicsRectItem, QGraphicsEllipseItem, QGraphicsPolygonItem
from PySide2.QtGui import QPixmap, QBrush, QColor, QPolygonF
from PySide2.QtCore import Qt, QTimer, QEvent, QPointF
from urllib.request import build_opener
from random import randint

try:
  from simpleaudio import WaveObject
except:
  from .mockaudio import WaveObject  

def make_color(color):
  if isinstance(color, tuple):
    if len(color)==3:
      r, g, b=color
      return QColor(r, g, b)
  else:
      return QColor(color)

class GIWrapper:
  def __init__(self, sgapp, gi):
    self.sgapp=sgapp
    self.gi=gi
  def set_gi_pos(self, x, y):
    self.gi.setPos(x, y)
  def get_gi_x(self):
    return self.gi.pos().x()
  def get_gi_y(self):
    return self.gi.pos().y()
  def set_gi_color(self, color):    
    br=QBrush(make_color(color))
    self.gi.setBrush(br)
  def set_gi_img(self, img_url_or_file):
    pm=self.gi.pixmap()
    pm2=self.sgapp.load_pixmap(img_url_or_file, pm.width(), pm.height())
    self.gi.setPixmap(pm2)
  def set_gi_rect_size(self, w, h):
    self.gi.setRect(0, 0, w, h)
  def set_gi_cir_radius(self, r):
    self.gi.setRect(0, 0, r, r)
  def remove_gi(self):
    self.sgapp.gs.removeItem(self.gi)
  def get_brect_in_parent(self):
    r=self.gi.boundingRect()
    r=self.gi.mapRectToParent(r)
    return r
  def are_gi_overlap(self, giw):
    r1=self.get_brect_in_parent()
    r2=giw.get_brect_in_parent()
    return r1.intersects(r2)

class SimGraphicsView(QGraphicsView):
  def __init__(self, scene, key_handler):
      super().__init__(scene)
      self.key_handler=key_handler
  def keyPressEvent(self, event):
    self.key_handler(event)
  def keyReleaseEvent(self, event):
    self.key_handler(event)

class MyWidget(QWidget):
  def __init__(self, key_handler):
      super().__init__()
      self.key_handler=key_handler
  def keyPressEvent(self, event):
    self.key_handler(event)
  def keyReleaseEvent(self, event):
    self.key_handler(event)

class SimGuiApp(QApplication):
    SCENE_WIDTH=400
    SCENE_HEIGHT=300
    def __init__(self) -> None:
        super().__init__()
        self.mod=None
    def start(self, mod):
        self.mod=mod
        self.in_modal=False
        self.key_ev=None
        self.gs=None
        self.gv=None
        self.gi_dict={}
        self.timer_dict={}
        self.wid_dict={}
        self.last_row=None
        self.auto_row=0
        self.auto_col=0
        self.make_opener()
        self.wid=MyWidget(self.on_key)
        self.wid.setWindowTitle("simgui")
        self.lo=QGridLayout()
        self.wid.setLayout(self.lo)
        self.wid.show()
        ev=QEvent(QEvent.Type.User)
        self.postEvent(self, ev)
        self.exec_()
    def event(self, ev):
      if ev.type()==QEvent.Type.User:
        self.call_handler("on_ready")  
      return super().event(ev)
    def make_opener(self):
      self.op=build_opener()
      self.op.addheaders=[("User-agent", "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11")]
      self.op.cache={}
    def call_handler(self, fn, data=None):
        handler=self.mod.get(fn)
        if handler:
          if data:
            handler(data)
          else:
            handler()
    def add_label(self, name, text, **kwargs):
        lbl=QLabel(str(text))
        self.add_wid(name, lbl, **kwargs)
    def add_button(self, name, text, **kwargs):
        btn=QPushButton(str(text))
        def on_click():
          self.call_handler("on_click_"+name)
        btn.clicked.connect(on_click)
        self.add_wid(name, btn, **kwargs)
    def set_wid_text(self, name, text):
      self.get_wid(name).setText(str(text))
    def set_wid_min_size(self, name, w, h):
      wid=self.get_wid(name)
      wid.setMinimumSize(w, h)
    def set_wid_max_size(self, name, w, h):
      wid=self.get_wid(name)
      wid.setMaximumSize(w, h)
    def set_wid_color(self, name, color):
      wid=self.get_wid(name)
      c=self.get_css_color(color)
      wid.setStyleSheet(f"background-color: {c}")
    def fetch_web_data(self, url):
      if url in self.op.cache:
        return self.op.cache[url]
      else:
        d=self.op.open(url).read()
        self.op.cache[url]=d
        return d
    def set_label_img(self, name, img_url):
      data=self.fetch_web_data(img_url)
      pm=QPixmap()
      pm.loadFromData(data)
      lbl=self.get_wid(name)
      lbl.setScaledContents(True)
      lbl.setPixmap(pm)
    def add_wid(self, name, w, **kwargs):
      if not (name in self.wid_dict):
        self.wid_dict[name]=w
        if "right" in kwargs:
          row=self.last_row
          col=self.auto_col
        else:
          row=self.auto_row
          col=0
        row=kwargs.get("row", row)
        col=kwargs.get("col", col)
        rows=kwargs.get("rows", 1)
        cols=kwargs.get("cols", 1)
        self.lo.addWidget(w, row, col, rows, cols)
        self.last_row=row
        self.auto_row=row+rows
        self.auto_col=col+cols
      else:
        raise ValueError(f"widget named {name} already exists", name)
    def get_wid(self, name):
      if name in self.wid_dict:
        return self.wid_dict[name]
      else:
        raise ValueError(f"no widget named {name}", name)
    def add_input(self, name, **kwargs):
        edit=QLineEdit()
        def on_edited():
          self.call_handler("on_edited_"+name)
        edit.textEdited.connect(on_edited)
        self.add_wid(name, edit, **kwargs)
    def add_combo(self, name, **kwargs):
        cb=QComboBox()
        def on_idx_changed():
          self.call_handler("on_index_changed_"+name)
        cb.currentIndexChanged.connect(on_idx_changed)
        self.add_wid(name, cb, **kwargs)
    def add_combo_item(self, name, item):
        cb=self.get_wid(name)
        cb.addItem(str(item))
    def get_combo_text(self, name):
        cb=self.get_wid(name)
        return cb.currentText()
    def get_input_text(self, name):
      inp=self.get_wid(name)
      return inp.text()
    def get_input_num(self, name):
      t=self.get_input_text(name)
      return int(t)
    def get_input_value(self, name):
      t=self.get_input_text(name)
      try:
        return int(t)
      except:
        return t
    def set_input_text(self, name, text):
      self.get_wid(name).setText(str(text))
    def on_key(self, event):
      evt=event.type()
      if evt==QEvent.KeyPress:
        self.key_ev=event
        self.call_handler("on_key")
      elif evt==QEvent.KeyRelease:
        self.key_ev=event
        self.call_handler("on_key_up")
    def add_graphics_view(self, min_w, min_h, scene_w=None, scene_h=None):
        if self.gs:
          raise ValueError("Only one graphics view can be added")
        self.gs=QGraphicsScene()
        self.gv=SimGraphicsView(self.gs, self.on_key)
        self.gv.setMinimumSize(min_w, min_h)
        if scene_w and scene_h:
          self.gv.setSceneRect(0, 0, scene_w, scene_h)
        else:
          #there is a 1 pixel margin hard coded
          self.gv.setSceneRect(0, 0, SimGuiApp.SCENE_WIDTH-2, SimGuiApp.SCENE_HEIGHT-2)
        self.add_wid("simgui_gv", self.gv)
    def add_gi_img(self, name, x, y, w, h, img_url_or_file):
      pm2=self.load_pixmap(img_url_or_file, w, h)
      gi=QGraphicsPixmapItem(pm2)
      giw=GIWrapper(self, gi)
      giw.set_gi_pos(x, y)
      self.add_gi(name, giw)
      return giw
    def load_pixmap(self, img_url_or_file, w, h):
      if img_url_or_file.find("://")>0:
        data=self.fetch_web_data(img_url_or_file)
        pm=QPixmap()
        pm.loadFromData(data)
      else:
        from pathlib import Path
        p=Path(img_url_or_file)
        if p.exists():
          pm=QPixmap(img_url_or_file)
        else:
          raise ValueError(f"File {img_url_or_file} not found")
      pm2=pm.scaled(w, h, Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation)
      return pm2
    def set_gi_img(self, name, img_url_or_file):
      giw=self.get_gi(name)
      giw.set_gi_img(img_url_or_file)
    def add_gi_rect(self, name, x, y, w, h, color):
      gi=QGraphicsRectItem(0, 0, w, h)
      giw=GIWrapper(self, gi)
      giw.set_gi_pos(x, y)
      giw.set_gi_color(color)
      self.add_gi(name, giw)
      return giw
    def get_css_color(self, color):
      qc=make_color(color)
      n=qc.name(QColor.HexRgb)
      return n
    def add_gi_polygon(self, name, points, color):
      x, y=points[0]
      pts=[QPointF(x2-x, y2-y) for (x2, y2) in points]
      gi=QGraphicsPolygonItem(QPolygonF(pts))
      giw=GIWrapper(self, gi)
      giw.set_gi_pos(x, y)
      giw.set_gi_color(color)      
      self.add_gi(name, giw)
      return giw
    def set_gi_rect_size(self, name, w, h):
      giw=self.get_gi(name)
      giw.set_gi_rect_size(w, h)
    def add_gi_cir(self, name, x, y, r, color):
      gi=QGraphicsEllipseItem(0, 0, r, r)
      giw=GIWrapper(self, gi)
      giw.set_gi_pos(x, y)
      giw.set_gi_color(color)   
      self.add_gi(name, giw)
      return giw
    def set_gi_cir_radius(self, name, r):
      giw=self.get_gi(name)
      giw.set_gi_cir_radius(r)
    def add_gi(self, name, giw):
      if self.gs==None:
        raise ValueError("Must add a graphics scene first")
      if name:
        if name in self.gi_dict:
          raise ValueError(f"Graphics item {name} already exists")
        self.gi_dict[name]=giw
        self.gs.addItem(giw.gi)
    def set_gi_pos(self, name, x, y):
      giw=self.get_gi(name)
      giw.set_gi_pos(x, y)
    def get_gi_x(self, name):
      giw=self.get_gi(name)
      return giw.get_gi_x()
    def get_gi_y(self, name):
      giw=self.get_gi(name)
      return giw.get_gi_y()
    def set_gi_color(self, name, color):    
      giw=self.get_gi(name)
      giw.set_gi_color(color)
    def gi_exists(self, name):
      return  name in self.gi_dict
    def get_gi(self, name):
      if name in self.gi_dict:
        return self.gi_dict[name]
      else:
        raise ValueError(f"No graphics item named {name}")
    def remove_gi(self, name):
      if self.gs==None:
        raise ValueError("Must add a graphics scene first")
      giw=self.get_gi(name)
      del self.gi_dict[name]
      giw.remove_gi()
    def make_unique_name(self, prefix):
      while True:
        name=prefix+str(randint(0, 65535))
        if not(name in self.gi_dict) and not(name in self.wid_dict):
          return name

    def get_key(self):
      code_map={Qt.Key_Left: "Left", Qt.Key_Right: "Right", Qt.Key_Up: "Up", Qt.Key_Down: "Down", \
            Qt.Key_Enter: "Enter", Qt.Key_Insert: "Insert", Qt.Key_Delete: "Delete", \
            Qt.Key_Return: "Enter", Qt.Key_Home: "Home", Qt.Key_End: "End",
            Qt.Key_PageUp: "PageUp", Qt.Key_PageDown: "PageDown" }
      key=self.key_ev.key()
      txt=self.key_ev.text()
      if key in code_map:
        return code_map[key]
      elif txt:
        return txt
      else:
        return "Unknown"
    def start_timer(self, name, interval):
      def on_timeout():
        if not self.in_modal:
          self.call_handler("on_timeout_"+name)
      tm=QTimer()
      tm.timeout.connect(on_timeout)
      tm.start(int(interval*1000))
      self.timer_dict[name]=tm
    def stop_timer(self, name):
      self.timer_dict[name].stop()
    def send_data_to_future(self, data, interval):
      def on_timeout():
        tm.stop()
        self.call_handler("on_data_from_past", data)
      tm=QTimer()
      tm.timeout.connect(on_timeout)
      tm.start(int(interval*1000))
    def are_gi_overlap(self, n1, n2):
      giw1=self.get_gi(n1)
      giw2=self.get_gi(n2)
      return giw1.are_gi_overlap(giw2)
    def msg_box(self, text):
      self.in_modal=True
      try:
        QMessageBox.information(self.wid, "Info", str(text))
      finally:
        self.in_modal=False
    def play_wav(self, path):
      wo=WaveObject.from_wave_file(path)
      wo.play()

sgapp=SimGuiApp()

# the mod parameter is no longer needed
def start(mod=None):
  import __main__
  sgapp.start(vars(__main__))

def add_label(name, text, **kwargs):
    sgapp.add_label(name, text, **kwargs)

def set_label_text(name, text):
    sgapp.set_wid_text(name, text)

def set_label_img(name, img_url):
    sgapp.set_label_img(name, img_url)

def set_wid_color(name, color):
    sgapp.set_wid_color(name, color)

def set_wid_min_size(name, w, h):
    sgapp.set_wid_min_size(name, w, h)

def set_wid_max_size(name, w, h):
    sgapp.set_wid_max_size(name, w, h)

def add_button(name, text, **kwargs):
    sgapp.add_button(name, text, **kwargs)    

def set_button_text(name, text):
    sgapp.set_wid_text(name, text)

def add_input(name, **kwargs):
    sgapp.add_input(name, **kwargs)    

def get_input_text(name):
    return sgapp.get_input_text(name)        

def get_input_num(name):
    return sgapp.get_input_num(name)        

def get_input_value(name):
    return sgapp.get_input_value(name)        

def set_input_text(name, text):
    return sgapp.set_input_text(name, text)

def add_combo(name, **kwargs):
  sgapp.add_combo(name, **kwargs)      

def add_combo_item(name, item):
  sgapp.add_combo_item(name, item)

def get_combo_text(name):
  return sgapp.get_combo_text(name)

def add_graphics_view(min_w, min_h, scene_w=None, scene_h=None):
  sgapp.add_graphics_view(min_w, min_h, scene_w, scene_h)

def add_gi_img(name, x, y, w, h, img_url):
  sgapp.add_gi_img(name, x, y, w, h, img_url)

def add_gi_rect(name, x, y, w, h, color):
  sgapp.add_gi_rect(name, x, y, w, h, color)

def add_gi_cir(name, x, y, r, color):
  sgapp.add_gi_cir(name, x, y, r, color)

def add_gi_polygon(name, points, color):
  sgapp.add_gi_polygon(name, points, color)

def remove_gi(name):
  sgapp.remove_gi(name)

def get_key():
  return sgapp.get_key()

def get_gi_x(name):
  return sgapp.get_gi_x(name)

def get_gi_y(name):
  return sgapp.get_gi_y(name)

def set_gi_pos(name, x, y):
  sgapp.set_gi_pos(name, x, y)

def set_gi_img(name, img_url_or_file):
  sgapp.set_gi_img(name, img_url_or_file)

def set_gi_color(name, color):
  sgapp.set_gi_color(name, color)

def set_gi_rect_size(name, w, h):
  sgapp.set_gi_rect_size(name, w, h)

def set_gi_cir_radius(name, r):
  sgapp.set_gi_cir_radius(name, r)

def start_timer(name, interval):
  sgapp.start_timer(name, interval)

def stop_timer(name):
  sgapp.stop_timer(name)

def make_unique_name(prefix):
  return sgapp.make_unique_name(prefix)

def gi_exists(name):
  return sgapp.gi_exists(name)

def are_gi_overlap(n1, n2):
  return sgapp.are_gi_overlap(n1, n2)

def msg_box(text):
  sgapp.msg_box(text)

def quit():
  sgapp.quit()

def play_wav(path):
  sgapp.play_wav(path)

def send_data_to_future(data, interval):
  sgapp.send_data_to_future(data, interval)