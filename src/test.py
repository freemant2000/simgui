from PySide2.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QApplication, QComboBox, QGridLayout, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PySide2.QtGui import QPixmap

class SimGraphicsView(QGraphicsView):
  def keyPressEvent(self, event):
    print(event.key())


class SimGuiApp(QApplication):
    def __init__(self) -> None:
        super().__init__()
        self.mod=None
    def start(self, mod):
        self.mod=mod
        self.wid_dict={}
        self.last_row=None
        self.auto_row=0
        self.auto_col=0
        wid=QWidget()
        wid.setWindowTitle("simgui")
        self.lo=QGridLayout()
        wid.setLayout(self.lo)
        gs=QGraphicsScene()
        pm=QPixmap("src/wechat.png")
        pi=QGraphicsPixmapItem(pm)
        pi.setPos(50, 100)
        gs.addItem(pi)
        #gs.addText("hello")
        gv=SimGraphicsView(gs)
        gv.setMinimumSize(300, 200)
        self.lo.addWidget(gv)
        wid.show()
        self.exec_()

sgapp=SimGuiApp()
sgapp.start(None)
