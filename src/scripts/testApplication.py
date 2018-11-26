from PyQt5.QtWidgets import *


app = QApplication([])

window = QMainWindow()
window.setWindowTitle("testAplication")
window.resize(800, 650)

label = QLabel("Style")

qTopLayout = QHBoxLayout()
qTopLayout.addWidget(label)

window.addDockWidget(qTopLayout)
window.show()




app.exec_()