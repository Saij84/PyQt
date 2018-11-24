from PyQt5.QtWidgets import *

app = QApplication([])
button = QPushButton('Click')

def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec_()

button.clicked.connect(on_button_clicked)
button.show()
app.exec_()

'''
The interesting line is highlighted above: button.clicked is a signal, .connect(...) lets us install a so-called slot on it. 
This is simply a function that gets called when the signal occurs. In the above example, our slot shows a message box.

The term slot is important when using Qt from C++, because slots must be declared in a special way in C++. In Python however, 
any function can be a slot – we saw this above. For this reason, the distinction between slots and "normal" functions has little relevance for us.

Signals are ubiquitous in Qt. And of course, you can also define your own. This however is beyond the scope of this tutorial.
'''