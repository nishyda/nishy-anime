from ast import main
import sys
import json
import csv
from PySide6.QtWidgets import (QColorDialog, QCheckBox, QComboBox, QHBoxLayout, QApplication, QVBoxLayout, QDialog, QPushButton)


class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super(SettingsDialog, self).__init__(parent)

        f = open('config.json')
        data = json.load(f)
        f.close()

        self.setWindowTitle("NishyAnime Settings GUI")
        self.setFixedWidth(350)
        self.setFixedHeight(150)

        self.orderStatus = QCheckBox("Order by status")
        self.orderPrio = QCheckBox("Order by priority")
        if data['sortbystatus']:
            self.orderStatus.setChecked(True)
        if data['sortbypriority']:
            self.orderPrio.setChecked(True)

        self.themeSelect = QComboBox()
        self.themeSelect.addItem("Custom (To be implemented soon)")
        self.themeSelect.addItem("Thanos Bean Purple (Default)")
        self.themeSelect.addItem("Ikea Bag Blue")
        self.themeSelect.addItem("Pumpkin Hill Orange")
        self.themeSelect.setCurrentIndex(data['theme'])

        self.color1 = QColorDialog()
        self.color2 = QColorDialog()
        self.color3 = QColorDialog()
        self.color4 = QColorDialog()
        self.color5 = QColorDialog()
        self.color6 = QColorDialog()

        self.saveQuit = QPushButton("Save and Quit")
        self.quit = QPushButton("Exit")
        self.saveQuit.clicked.connect(self.save)
        self.quit.clicked.connect(self.close)

        orderForm = QHBoxLayout()
        orderForm.addWidget(self.orderStatus)
        orderForm.addWidget(self.orderPrio)

        quitForm = QHBoxLayout()
        quitForm.addWidget(self.saveQuit)
        quitForm.addWidget(self.quit)

        mainForm = QVBoxLayout()
        mainForm.addLayout(orderForm)
        mainForm.addWidget(self.themeSelect)
        mainForm.addLayout(quitForm)

        self.setLayout(mainForm)
    
    def save(self):
        f = open('config.json')
        data = json.load(f)
        f.close()
        data['sortbystatus'] = True if self.orderStatus.isChecked() else False
        data['sortbypriority'] = True if self.orderPrio.isChecked() else False
        data['theme'] = self.themeSelect.currentIndex()
        f = open('config.json','w')
        json.dump(data,f)
        f.close()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = SettingsDialog()
    form.show()
    sys.exit(app.exec())
