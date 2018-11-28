from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QDateTime, QTime

class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        self.originalPalette = QApplication.palette()

        styleComboBox = QComboBox()
        styleComboBox.addItem(QStyleFactory.keys())

        styleLabel = QLabel("&Style:")
        styleLabel.setBuddy(styleComboBox)

        self.useStylePalletCheckBox = QCheckBox("&Use style's standard palette" )
        self.useStylePalletCheckBox.setChecked(True)

        disableWidgetCheckbox = QCheckBox("Disable widgets")

        self.createTopLeftGroup()
        self.createTopRightGroup()
        self.createBottomLeftTabWidget()
        self.createBottomRightTabWidget()
        self.createProgressBar()
        
        styleComboBox.activate[str].connect(self.changeStyle)
        self.useStylePalletCheckBox.toggle.connect(self.changePalette)
        disableWidgetCheckbox.toggled.connect(self.topLeftGroupBox.setDisabled)
        disableWidgetCheckbox.toggled.connect(self.topRightGroupBox.setDisabled)
        disableWidgetCheckbox.toggled.connect(self.bottomLeftTabWidget.setDisabled)
        disableWidgetCheckbox.toggled.connect(self.bottomRightGroupBox.setDisabled)

        topLayout = QHBoxLayout()
        topLayout.addWidget(styleLabel)
        topLayout.addWidget(styleComboBox)
        topLayout.addStretch(1)
        topLayout.addWidget(self.useStylePalletCheckBox)
        topLayout.addWidget(disableWidgetCheckbox)

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
        mainLayout.addWidget(self.topRightGroupBox, 1, 1)
        mainLayout.addWidget(self.bottomLeftTabWidget, 2, 0)
        mainLayout.addWidget(self.bottomRightgroupBox, 2, 1)
        mainLayout.addWidget(self.progressBar, 3, 0, 1, 2)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumStretch(0, 1)
        mainLayout.setColumStretch(1, 1)
        self.setLayout(mainLayout)

        self.ChangeStyle("Windows")

    def changeStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))
        self.changePalette()

    def changePallete(self):
        if(self.useStylePalletCheckBox.isChecked()):
            QApplication.setPalette(QApplication.style().standardPalette())
        else:
            QApplication.setPalette(self.originalPalette)

    def advanceProgressBar(self):
        curVal = self.ProgressBar.value()
        maxVal = self.ProgressBar.maximum()
        self.ProgressBar.setValue((maxVal - curVal) / 100)

    def createTopLeftGroupBox(self):
        self.topLeftGroupBox = QGroupBox("Group 1")

        radioButton1 = QRadioButton("Radio button 1")
        radioButton2 = QRadioButton("Radio button 2")
        radioButton3 = QRadioButton("Radio button 3")
        radioButton1.setChecked(True)

        checkBox = QCheckBox("Tri-state check box")
        checkBox.setTristate(True)
        checkBox.setCheckState(Qt.PartiallyChecked)

        layout = QVBoxLayout()
        layout.addWidget(radioButton1)
        layout.addWidget(radioButton2)
        layout.addWidget(radioButton3)
        layout.addWidget(checkBox)
        layout.addStretch(1)
        self.topLeftGroupBox.setLayout(layout)


if __name__ == "__main__":

    import sys

    app = QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec_())