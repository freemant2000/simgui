from PySide6.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsPixmapItem, QApplication, QWidget, QGridLayout
from PySide6.QtGui import QPixmap

app=QApplication()
gs=QGraphicsScene()
gv=QGraphicsView(gs)
gv.setMinimumSize(400, 300)
gs.setSceneRect(0, 0, 400-2, 300-2)
pm=QPixmap("/home/kent/simgui/src/examples/pikachu-0.png")
pi=QGraphicsPixmapItem(pm)
gs.addItem(pi)
lo=QGridLayout()
mw=QWidget()
mw.setLayout(lo)
lo.addWidget(gv)
mw.show()
app.exec_()
