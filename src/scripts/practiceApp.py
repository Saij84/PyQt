from PyQt5.QtWidgets import *

class PracticeApp(QDialog):
    def __init__(self, parent=None):
        super(PracticeApp, self).__init__(parent)


        myComboBox = QComboBox()
        myComboBox.addItem("1000", 10000.0)
        myComboBox.addItem("1001", 10000.0)
        myComboBox.addItem("1002", 10000.0)
        myComboBox.addItem("1003", 10000.0)


        myLable = QLabel("Number:")
        myLable.setBuddy(myComboBox)

        topLayout = QHBoxLayout()
        topLayout.addWidget(myComboBox)
        topLayout.addWidget(myLable)

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 1, 1, 2)
        self.setLayout(mainLayout)



if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    PracticeApp = PracticeApp()
    PracticeApp.show()
    sys.exit(app.exec_())