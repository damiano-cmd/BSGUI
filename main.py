from requests import get
from bs4 import BeautifulSoup as soup
from os.path import isdir
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QWidget):
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(973, 292)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.url = QtWidgets.QLineEdit(self.centralwidget)
        self.url.setGeometry(QtCore.QRect(10, 60, 931, 31))
        self.url.setObjectName("url")
        self.url_lab = QtWidgets.QLabel(self.centralwidget)
        self.url_lab.setGeometry(QtCore.QRect(10, 30, 61, 21))
        self.url_lab.setStyleSheet("font: 12pt \"Nirmala UI Semilight\"")
        self.url_lab.setObjectName("url_lab")
        self.href = QtWidgets.QCheckBox(self.centralwidget)
        self.href.setGeometry(QtCore.QRect(120, 250, 111, 17))
        self.href.setStyleSheet("font: 12pt \"Nirmala UI Semilight\"")
        self.href.setObjectName("href")
        self.class_lab = QtWidgets.QLabel(self.centralwidget)
        self.class_lab.setGeometry(QtCore.QRect(10, 170, 41, 21))
        self.class_lab.setStyleSheet("font: 12pt \"Nirmala UI Semilight\"")
        self.class_lab.setObjectName("class_lab")
        self.class_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.class_2.setGeometry(QtCore.QRect(80, 170, 201, 21))
        self.class_2.setObjectName("class_2")
        self.element_lab = QtWidgets.QLabel(self.centralwidget)
        self.element_lab.setGeometry(QtCore.QRect(10, 130, 61, 16))
        self.element_lab.setStyleSheet("font: 12pt \"Nirmala UI Semilight\"")
        self.element_lab.setObjectName("element_lab")
        self.element = QtWidgets.QLineEdit(self.centralwidget)
        self.element.setGeometry(QtCore.QRect(80, 130, 201, 21))
        self.element.setObjectName("element")
        self.directory = QtWidgets.QLineEdit(self.centralwidget)
        self.directory.setGeometry(QtCore.QRect(370, 130, 451, 21))
        self.directory.setObjectName("directory")
        self.directory_lab = QtWidgets.QLabel(self.centralwidget)
        self.directory_lab.setGeometry(QtCore.QRect(300, 130, 71, 21))
        self.directory_lab.setStyleSheet("font: 12pt \"Nirmala UI Semilight\"")
        self.directory_lab.setObjectName("directory_lab")
        self.output_lab = QtWidgets.QLabel(self.centralwidget)
        self.output_lab.setGeometry(QtCore.QRect(300, 160, 61, 21))
        self.output_lab.setStyleSheet("font: 12pt \"Nirmala UI Semilight\"")
        self.output_lab.setObjectName("output_lab")
        self.output = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(370, 170, 591, 111))
        self.output.setObjectName("output")
        self.scrape = QtWidgets.QPushButton(self.centralwidget)
        self.scrape.setGeometry(QtCore.QRect(20, 250, 75, 23))
        self.scrape.setStyleSheet("border: 0;\n" "background-color:rgb(158, 158, 158)")
        self.scrape.setObjectName("scrape")
        self.id_lab = QtWidgets.QLabel(self.centralwidget)
        self.id_lab.setGeometry(QtCore.QRect(10, 210, 21, 16))
        self.id_lab.setStyleSheet("font: 12pt \"Nirmala UI Semilight\"")
        self.id_lab.setObjectName("id_lab")
        self.id = QtWidgets.QLineEdit(self.centralwidget)
        self.id.setGeometry(QtCore.QRect(80, 210, 201, 21))
        self.id.setObjectName("id")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #connect buttons
        self.scrape.clicked.connect(self.webscrape)
    
    def webscrape(self, MainWindow):

        #variabels
        _translate = QtCore.QCoreApplication.translate
        hrefCheck = self.href.isChecked()
        urlt = self.url.text()
        elementt = self.element.text()
        classt = self.class_2.text()
        directoryt = self.directory.text()
        idt = self.id.text()

        if urlt != '':
            try:
                html = get(self.url.text()).text
                soup2 = soup(html, 'html.parser')
                if elementt and classt and idt != '':
                    result = soup2.findAll(elementt, class_=classt, id=idt, href=hrefCheck)
                elif elementt and classt != '':
                    result = soup2.findAll(elementt, class_=classt, href=hrefCheck)
                elif elementt and idt != '':
                    result = soup2.findAll(elementt, id=idt, href=hrefCheck)
                elif classt and idt != '':
                    result = soup2.findAll(class_=classt, id=idt, href=hrefCheck)
                elif classt != '':
                    result = soup2.findAll(class_=classt, href=hrefCheck)
                elif idt != '':
                    result = soup2.findAll(id=idt, href=hrefCheck)
                elif elementt != '':
                    result = soup2.findAll(elementt, href=hrefCheck)
                else:
                    result = soup2.findAll(href=hrefCheck)
                self.output.setPlainText(_translate("MainWindow", str(result)))
                if isdir(directoryt):
                    with open(directoryt + '\\' + 'scrape.txt', 'w') as f:
                        f.write(str(result))
            except:
                self.output.setPlainText(_translate("MainWindow", "Something is not right!"))
        else:
            self.output.setPlainText(_translate("MainWindow", "Need to put in minimum requirement!"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BeautifulSoupGUI"))
        self.url_lab.setText(_translate("MainWindow", "URL:"))
        self.href.setText(_translate("MainWindow", "Look for href"))
        self.class_lab.setText(_translate("MainWindow", "Class:"))
        self.element_lab.setText(_translate("MainWindow", "Element:"))
        self.directory_lab.setText(_translate("MainWindow", "Directory:"))
        self.output_lab.setText(_translate("MainWindow", "Output:"))
        self.scrape.setText(_translate("MainWindow", "Scrape"))
        self.id_lab.setText(_translate("MainWindow", "ID:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowIcon(QtGui.QIcon('BSGUI.ico'))
    MainWindow.show()
    sys.exit(app.exec_())
