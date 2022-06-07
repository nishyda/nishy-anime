import sys
import webbrowser
import json
import csv
from PySide6.QtWidgets import (QRadioButton, QListWidgetItem, QFormLayout, QLineEdit, QHBoxLayout, QLabel, QApplication, QVBoxLayout, QDialog, QPushButton, QListWidget, QDialogButtonBox)
from PySide6 import QtCore
from PySide6 import QtGui

f = open('config.json')
data = json.load(f)

if data['theme'] == 0:
    plantowatchcolor = [QtGui.QColor(data['plantowatchbg'][0], data['plantowatchbg'][1], data['plantowatchbg'][2]), QtGui.QColor(data['plantowatchfg'][0], data['plantowatchfg'][1], data['plantowatchfg'][2])]
    watchingcolor = [QtGui.QColor(data['watchingbg'][0], data['watchingbg'][1], data['watchingbg'][2]), QtGui.QColor(data['watchingfg'][0], data['watchingfg'][1], data['watchingfg'][2])]
    watchedcolor = [QtGui.QColor(data['watchedbg'][0], data['watchedbg'][1], data['watchedbg'][2]), QtGui.QColor(data['watchedfg'][0], data['watchedfg'][1], data['watchedfg'][2])]
elif data['theme'] == 2:
    plantowatchcolor = [QtGui.QColor(102, 153, 255), QtGui.QColor(0, 0, 0)]
    watchingcolor = [QtGui.QColor(0, 0, 102), QtGui.QColor(255,255,255)]
    watchedcolor = [QtGui.QColor(255, 255, 255), QtGui.QColor(0, 0, 0)]
elif data['theme'] == 3:
    plantowatchcolor = [QtGui.QColor(255, 153, 102), QtGui.QColor(0, 0, 0)]
    watchingcolor = [QtGui.QColor(102, 0, 0), QtGui.QColor(255,255,255)]
    watchedcolor = [QtGui.QColor(255, 255, 255), QtGui.QColor(0, 0, 0)]
else:
    plantowatchcolor = [QtGui.QColor(204, 153, 255), QtGui.QColor(0, 0, 0)]
    watchingcolor = [QtGui.QColor(102, 0, 102), QtGui.QColor(255,255,255)]
    watchedcolor = [QtGui.QColor(255, 255, 255), QtGui.QColor(0, 0, 0)]

animelist = []
header = ['Title','Link','Status']

def animeOpen():
    with open('anime.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for item in reader:
            animelist.append(dict(item))
    animelist.sort(key=lambda i: i['Title'].lower())
    if data['sort']:
        animelist.sort(key=lambda i: 0 if i['Status']=="Watching" else 1 if i['Status']=="" else 2)

def animeSave():
    with open('anime.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, header, delimiter=';')
        writer.writeheader()
        writer.writerows(animelist)

class AddDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add new anime")
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        
        animeform = QFormLayout()
        self.title = QLineEdit()
        self.link = QLineEdit()
        animeform.addRow("Anime title: ", self.title)
        animeform.addRow("Link to website: ", self.link)

        self.newStatus = ""

        self.rbn1 = QRadioButton("Plan to watch")
        self.rbn2 = QRadioButton("Watching")
        self.rbn3 = QRadioButton("Watched")

        self.rbn1.setChecked(True)

        self.rbn1.toggled.connect(self.toggle1)
        self.rbn2.toggled.connect(self.toggle2)
        self.rbn3.toggled.connect(self.toggle3)

        btns = QHBoxLayout()
        btns.addWidget(self.rbn1)
        btns.addWidget(self.rbn2)
        btns.addWidget(self.rbn3)

        layout = QVBoxLayout()

        layout.addLayout(animeform)
        layout.addLayout(btns)
        layout.addWidget(self.buttonBox)

        self.setLayout(layout)
    
    def toggle1(self):
        self.newStatus = ""
    
    def toggle2(self):
        self.newStatus = "Watching"
    
    def toggle3(self):
        self.newStatus = "Watched"


class EditDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edit anime")
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        
        animeform = QFormLayout()
        self.title = QLineEdit()
        self.link = QLineEdit()
        self.title.setText(animelist[form.animelist.currentRow()]['Title'])
        self.link.setText(animelist[form.animelist.currentRow()]['Link'])
        animeform.addRow("Anime title: ", self.title)
        animeform.addRow("Link to website: ", self.link)
        
        self.rbn1 = QRadioButton("Plan to watch")
        self.rbn2 = QRadioButton("Watching")
        self.rbn3 = QRadioButton("Watched")

        if animelist[form.animelist.currentRow()]['Status'] == "":
            self.rbn1.setChecked(True)
            self.newStatus = ""
        elif animelist[form.animelist.currentRow()]['Status'] == "Watching":
            self.rbn2.setChecked(True)
            self.newStatus = "Watching"
        elif animelist[form.animelist.currentRow()]['Status'] == "Watched":
            self.rbn3.setChecked(True)
            self.newStatus = "Watched"

        self.rbn1.toggled.connect(self.toggle1)
        self.rbn2.toggled.connect(self.toggle2)
        self.rbn3.toggled.connect(self.toggle3)

        btns = QHBoxLayout()
        btns.addWidget(self.rbn1)
        btns.addWidget(self.rbn2)
        btns.addWidget(self.rbn3)

        layout = QVBoxLayout()

        layout.addLayout(animeform)
        layout.addLayout(btns)
        layout.addWidget(self.buttonBox)

        self.setLayout(layout)
    
    def toggle1(self):
        self.newStatus = ""
    
    def toggle2(self):
        self.newStatus = "Watching"
    
    def toggle3(self):
        self.newStatus = "Watched"

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle(data['windowtitle'])
        self.title = QLabel(self)
        self.title.setText(data['windowtitle'])
        self.animelist = QListWidget()
        for index, anime in enumerate(animelist):
            newItem = QListWidgetItem(anime['Title'])
            if anime['Status'] == "":
                newItem.setBackground(plantowatchcolor[0])
                newItem.setForeground(plantowatchcolor[1])
            elif anime['Status'] == "Watching":
                newItem.setBackground(watchingcolor[0])
                newItem.setForeground(watchingcolor[1])
            elif anime['Status'] == "Watched":
                newItem.setBackground(watchedcolor[0])
                newItem.setForeground(watchedcolor[1])
            self.animelist.insertItem(index, newItem)

        self.count = QLabel(self)
        self.count.setText("none / " + str(self.animelist.count()))
        
        self.add = QPushButton("Add entry")
        self.remove = QPushButton("Remove entry")
        self.edit = QPushButton("Edit entry")
        self.play = QPushButton("Open website")

        self.remove.setEnabled(False)
        self.edit.setEnabled(False)
        self.play.setEnabled(False)

        buttonBar = QHBoxLayout()
        buttonBar.addWidget(self.count)
        buttonBar.addWidget(self.add)
        buttonBar.addWidget(self.remove)
        buttonBar.addWidget(self.edit)
        buttonBar.addWidget(self.play)

        layout = QVBoxLayout()
        layout.addWidget(self.title)
        layout.addLayout(buttonBar)
        layout.addWidget(self.animelist)

        self.setLayout(layout)

        self.setFixedWidth(data['windowX'])
        self.setFixedHeight(data['windowY'])

        self.animelist.clicked.connect(self.updatebutton)
        self.animelist.itemDoubleClicked.connect(self.playAnime)
        self.add.clicked.connect(self.addAnime)
        self.remove.clicked.connect(self.removeAnime)
        self.edit.clicked.connect(self.editAnime)
        self.play.clicked.connect(self.playAnime)
        
    def updatebutton(self):
        self.remove.setEnabled(True)
        self.edit.setEnabled(True)
        self.play.setEnabled(True)
        self.count.setText(str(self.animelist.currentRow() + 1) + " / " + str(self.animelist.count()))

    def addAnime(self):
        addDlg = AddDialog()
        if addDlg.exec():
            newTitle = addDlg.title.text()
            newLink = addDlg.link.text()
            newStatus = addDlg.newStatus
            newAnime = {'Title':newTitle,'Link':newLink,'Status':newStatus}
            animelist.append(newAnime)
            animeSave()

            newItem = QListWidgetItem(newAnime['Title'])
            if newAnime['Status'] == "":
                newItem.setBackground(plantowatchcolor[0])
                newItem.setForeground(plantowatchcolor[1])
            elif newAnime['Status'] == "Watching":
                newItem.setBackground(watchingcolor[0])
                newItem.setForeground(watchingcolor[1])
            elif newAnime['Status'] == "Watched":
                newItem.setBackground(watchedcolor[0])
                newItem.setForeground(watchedcolor[1])
            self.animelist.insertItem(self.animelist.count(), newItem)

    def removeAnime(self):
        animelist.pop(self.animelist.currentRow())
        animeSave()

        self.animelist.takeItem(self.animelist.currentRow())

        if len(animelist) == 0:
            self.remove.setEnabled(False)
            self.edit.setEnabled(False)
            self.play.setEnabled(False)
            self.count.setText("none / " + str(self.animelist.count()))

    def editAnime(self):
        editDlg = EditDialog()
        if editDlg.exec():
            newTitle = editDlg.title.text()
            newLink = editDlg.link.text()
            newStatus = editDlg.newStatus
            newAnime = {'Title':newTitle,'Link':newLink,'Status':newStatus}
            animelist[self.animelist.currentRow()] = newAnime
            animeSave()
            if newAnime['Status'] == "":
                self.animelist.currentItem().setBackground(plantowatchcolor[0])
                self.animelist.currentItem().setForeground(plantowatchcolor[1])
            elif newAnime['Status'] == "Watching":
                self.animelist.currentItem().setBackground(watchingcolor[0])
                self.animelist.currentItem().setForeground(watchingcolor[1])
            elif newAnime['Status'] == "Watched":
                self.animelist.currentItem().setBackground(watchedcolor[0])
                self.animelist.currentItem().setForeground(watchedcolor[1])
            self.animelist.currentItem().setText(newAnime['Title'])

    def playAnime(self):
        webbrowser.open(animelist[self.animelist.currentRow()]['Link'])

if __name__ == '__main__':
    animeOpen()
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec())