from pathlib import Path
import sys
import webbrowser
import json
import csv
from PySide6.QtWidgets import (QComboBox, QRadioButton, QListWidgetItem, QFormLayout, QLineEdit, QHBoxLayout, QLabel, QApplication, QVBoxLayout, QDialog, QPushButton, QListWidget, QDialogButtonBox)
from PySide6 import QtCore
from PySide6 import QtGui

class AddDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add new anime")
        self.newStatus = ""
        
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        
        self.title = QLineEdit()
        self.link = QLineEdit()
        self.currentep = QLineEdit()
        self.currentse = QLineEdit()
        self.totalep = QLineEdit()
        self.totalse = QLineEdit()

        self.priority = QComboBox()
        self.priority.addItems(["1","2","3"])
        self.priority.setCurrentIndex(2)

        self.rbn1 = QRadioButton("Plan to watch")
        self.rbn2 = QRadioButton("Watching")
        self.rbn3 = QRadioButton("Watched")
        self.rbn1.setChecked(True)
        self.rbn1.toggled.connect(self.toggle1)
        self.rbn2.toggled.connect(self.toggle2)
        self.rbn3.toggled.connect(self.toggle3)

        animeform = QFormLayout()
        animeform.addRow("Anime title: ", self.title)
        animeform.addRow("Link to website: ", self.link)
        animeform.addRow("Priority: ", self.priority)

        currentform = QFormLayout()
        currentform.addRow("Episode: ", self.currentep)
        currentform.addRow("Season: ", self.currentse)

        totalform = QFormLayout()
        totalform.addRow("Total: ", self.totalep)
        totalform.addRow("Total: ", self.totalse)

        counter = QHBoxLayout()
        counter.addLayout(currentform)
        counter.addLayout(totalform)

        btns = QHBoxLayout()
        btns.addWidget(self.rbn1)
        btns.addWidget(self.rbn2)
        btns.addWidget(self.rbn3)

        layout = QVBoxLayout()
        layout.addLayout(animeform)
        layout.addLayout(counter)
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
         
        self.title = QLineEdit()
        self.link = QLineEdit()
        self.title.setText(animelist[form.animelist.currentRow()]['Title'])
        self.link.setText(animelist[form.animelist.currentRow()]['Link'])  
        self.currentep = QLineEdit()
        self.currentse = QLineEdit()
        self.currentep.setText(animelist[form.animelist.currentRow()]['Episode'])
        self.currentse.setText(animelist[form.animelist.currentRow()]['Season'])
        self.totalep = QLineEdit()
        self.totalse = QLineEdit()
        self.totalep.setText(animelist[form.animelist.currentRow()]['TotalEp'])
        self.totalse.setText(animelist[form.animelist.currentRow()]['TotalSe'])

        self.priority = QComboBox()
        self.priority.addItems(["1","2","3"])
        self.priority.setCurrentIndex(int(animelist[form.animelist.currentRow()]['Priority'])-1)
        
        self.rbn1 = QRadioButton("Plan to watch")
        self.rbn2 = QRadioButton("Watching")
        self.rbn3 = QRadioButton("Watched")
        self.rbn1.toggled.connect(self.toggle1)
        self.rbn2.toggled.connect(self.toggle2)
        self.rbn3.toggled.connect(self.toggle3)
        if animelist[form.animelist.currentRow()]['Status'] == "":
            self.rbn1.setChecked(True)
            self.newStatus = ""
        elif animelist[form.animelist.currentRow()]['Status'] == "Watching":
            self.rbn2.setChecked(True)
            self.newStatus = "Watching"
        elif animelist[form.animelist.currentRow()]['Status'] == "Watched":
            self.rbn3.setChecked(True)
            self.newStatus = "Watched"

        animeform = QFormLayout()
        animeform.addRow("Anime title: ", self.title)
        animeform.addRow("Link to website: ", self.link)
        animeform.addRow("Priority: ", self.priority)

        currentform = QFormLayout()
        currentform.addRow("Episode: ", self.currentep)
        currentform.addRow("Season: ", self.currentse)

        totalform = QFormLayout()
        totalform.addRow("Total: ", self.totalep)
        totalform.addRow("Total: ", self.totalse)

        counter = QHBoxLayout()
        counter.addLayout(currentform)
        counter.addLayout(totalform)

        btns = QHBoxLayout()
        btns.addWidget(self.rbn1)
        btns.addWidget(self.rbn2)
        btns.addWidget(self.rbn3)

        layout = QVBoxLayout()
        layout.addLayout(animeform)
        layout.addLayout(counter)
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
        self.setFixedWidth(data['windowX'])
        self.setFixedHeight(data['windowY'])

        self.title = QLabel(self)
        self.title.setText(data['windowtitle'])

        self.animelist = QListWidget()
        for index, anime in enumerate(animelist):
            newItem = QListWidgetItem(anime['Priority'] + " " + anime['Title'])
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
        self.animelist.clicked.connect(self.updatebutton)
        self.animelist.itemDoubleClicked.connect(self.playAnime)
        self.animelist.setStyleSheet("border-image: url(wp.jpg);")

        self.count = QLabel(self)
        self.count.setText("0/" + str(self.animelist.count()))

        self.status = QLabel(self)
        self.episodes = QLabel(self)
        self.seasons = QLabel(self)
        
        self.add = QPushButton("Add Entry")
        self.remove = QPushButton("Remove Entry")
        self.edit = QPushButton("Edit Entry")
        self.play = QPushButton("Open Website")
        self.remove.setEnabled(False)
        self.edit.setEnabled(False)
        self.play.setEnabled(False)
        self.add.clicked.connect(self.addAnime)
        self.remove.clicked.connect(self.removeAnime)
        self.edit.clicked.connect(self.editAnime)
        self.play.clicked.connect(self.playAnime)

        buttonBar = QHBoxLayout()
        buttonBar.addWidget(self.title, alignment=QtCore.Qt.AlignLeft)
        buttonBar.addWidget(self.add)
        buttonBar.addWidget(self.remove)
        buttonBar.addWidget(self.edit)
        buttonBar.addWidget(self.play)

        infoBar = QHBoxLayout()
        infoBar.addWidget(self.status, alignment=QtCore.Qt.AlignLeft)
        infoBar.addWidget(self.episodes, alignment=QtCore.Qt.AlignCenter)
        infoBar.addWidget(self.seasons, alignment=QtCore.Qt.AlignCenter)
        infoBar.addWidget(self.count, alignment=QtCore.Qt.AlignRight)

        layout = QVBoxLayout()
        layout.addLayout(buttonBar)
        layout.addLayout(infoBar)
        layout.addWidget(self.animelist)

        self.setLayout(layout)        
        
    def updatebutton(self):
        self.remove.setEnabled(True)
        self.edit.setEnabled(True)
        self.play.setEnabled(True)

        if animelist[self.animelist.currentRow()]['Status'] == "":
            self.status.setText("Plan to watch")
            self.episodes.setText("")
            self.seasons.setText("")
        elif animelist[self.animelist.currentRow()]['Status'] == "Watching":
            self.status.setText("Watching")
            if animelist[self.animelist.currentRow()]['Episode'] != "" and animelist[self.animelist.currentRow()]['TotalEp'] != "":
                self.episodes.setText("Episode: " + str(animelist[self.animelist.currentRow()]['Episode']) + "/" + str(animelist[self.animelist.currentRow()]['TotalEp']))
            else:
                self.episodes.setText("")
            if animelist[self.animelist.currentRow()]['Season'] != "" and animelist[self.animelist.currentRow()]['TotalSe'] != "":
                self.seasons.setText("Season: " + str(animelist[self.animelist.currentRow()]['Season']) + "/" + str(animelist[self.animelist.currentRow()]['TotalSe']))
            else:
                self.seasons.setText("")
        elif animelist[self.animelist.currentRow()]['Status'] == "Watched":
            self.status.setText("Watched")
            self.episodes.setText("")
            self.seasons.setText("")
        self.count.setText(str(self.animelist.currentRow() + 1) + "/" + str(self.animelist.count()))

    def addAnime(self):
        addDlg = AddDialog()
        if not(addDlg.exec()):return
        newTitle = addDlg.title.text()
        newLink = addDlg.link.text()
        newEpisode = addDlg.currentep.text()
        newTotalEp = addDlg.totalep.text()
        newSeason = addDlg.currentse.text()
        newTotalSe = addDlg.totalse.text()
        newStatus = addDlg.newStatus
        newPriority = addDlg.priority.currentText()
        newAnime = {'Title':newTitle,'Link':newLink,'Status':newStatus,'Episode':newEpisode,'TotalEp':newTotalEp,'Season':newSeason,'TotalSe':newTotalSe,'Priority':newPriority}
        animelist.append(newAnime)
        animeSave()

        newItem = QListWidgetItem(newAnime['Priority'] + " " + newAnime['Title'])
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
        self.animelist.setCurrentRow(self.animelist.count()-1)
        self.updatebutton()

    def removeAnime(self):
        animelist.pop(self.animelist.currentRow())
        animeSave()

        self.animelist.takeItem(self.animelist.currentRow())

        if len(animelist) == 0:
            self.remove.setEnabled(False)
            self.edit.setEnabled(False)
            self.play.setEnabled(False)
            self.status.setText("")
            self.episodes.setText("")
            self.seasons.setText("")
            self.count.setText("0/" + str(self.animelist.count()))

    def editAnime(self):
        editDlg = EditDialog()
        if editDlg.exec():
            newTitle = editDlg.title.text()
            newLink = editDlg.link.text()
            newEpisode = editDlg.currentep.text()
            newTotalEp = editDlg.totalep.text()
            newSeason = editDlg.currentse.text()
            newTotalSe = editDlg.totalse.text()
            newStatus = editDlg.newStatus
            newPriority = editDlg.priority.currentText()
            newAnime = {'Title':newTitle,'Link':newLink,'Status':newStatus,'Episode':newEpisode,'TotalEp':newTotalEp,'Season':newSeason,'TotalSe':newTotalSe,'Priority':newPriority}
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
            self.animelist.currentItem().setText(newAnime['Priority'] + " " + newAnime['Title'])
            self.updatebutton()

    def playAnime(self):
        webbrowser.open(animelist[self.animelist.currentRow()]['Link'])

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
elif data['theme'] == 4:
    plantowatchcolor = [QtGui.QColor(255, 153, 102, 150), QtGui.QColor(0, 0, 0)]
    watchingcolor = [QtGui.QColor(102, 0, 0, 150), QtGui.QColor(255,255,255)]
    watchedcolor = [QtGui.QColor(255, 255, 255, 150), QtGui.QColor(0, 0, 0)]
else:
    plantowatchcolor = [QtGui.QColor(204, 153, 255), QtGui.QColor(0, 0, 0)]
    watchingcolor = [QtGui.QColor(102, 0, 102), QtGui.QColor(255,255,255)]
    watchedcolor = [QtGui.QColor(255, 255, 255), QtGui.QColor(0, 0, 0)]

animelist = []
header = ['Title','Link','Status','Episode','TotalEp','Season','TotalSe','Priority']

def animeOpen():
    Path('anime.csv').touch(exist_ok=True)
    with open('anime.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for item in reader:
            animelist.append(dict(item))
    animelist.sort(key=lambda i: i['Title'].lower())
    if data['sortbypriority']:
        animelist.sort(key=lambda i: int(i['Priority']))
    if data['sortbystatus']:
        animelist.sort(key=lambda i: 0 if i['Status']=="Watching" else 1 if i['Status']=="" else 2)

def animeSave():
    with open('anime.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, header, delimiter=';')
        writer.writeheader()
        writer.writerows(animelist)

if __name__ == '__main__':
    animeOpen()
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec())