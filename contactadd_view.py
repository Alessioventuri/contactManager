# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contactadd.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.mv = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(200, 30, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_8.setStyleSheet("color: red")
        self.label_8.hide()
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.first_name = QtWidgets.QLineEdit(self.centralwidget)
        self.first_name.setGeometry(QtCore.QRect(200, 60, 221, 22))
        self.first_name.setInputMethodHints(QtCore.Qt.ImhNone)
        self.first_name.setObjectName("first_name")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(200, 80, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_9.setStyleSheet("color: red")
        self.label_9.hide()
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.last_name = QtWidgets.QLineEdit(self.centralwidget)
        self.last_name.setGeometry(QtCore.QRect(200, 110, 221, 22))
        self.last_name.setText("")
        self.last_name.setObjectName("last_name")
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(200, 160, 221, 22))
        self.email.setText("")
        self.email.setObjectName("email")
        self.telephone = QtWidgets.QLineEdit(self.centralwidget)
        self.telephone.setGeometry(QtCore.QRect(200, 210, 221, 22))
        self.telephone.setText("")
        self.telephone.setObjectName("telephone")
        
        self.url = QtWidgets.QLineEdit(self.centralwidget)
        self.url.setGeometry(QtCore.QRect(200, 260, 221, 22))
        self.url.setText("")
        self.url.setObjectName("url")
        self.notes = QtWidgets.QTextEdit(self.centralwidget)
        self.notes.setGeometry(QtCore.QRect(200, 310, 221, 81))
        self.notes.setObjectName("notes")

        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setEnabled(True)
        self.submit.setGeometry(QtCore.QRect(160, 420, 200, 42))
        self.submit.setObjectName("submit")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 340, 81, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(120, 5, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
 
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(420, 5, 71, 42))
        self.back_button.setObjectName("back_button")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(30, 60, 81, 21))
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 81, 21))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 260, 81, 21))
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 210, 81, 21))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 160, 81, 21))
        self.label_4.setObjectName("label_4")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " Add Contact "))
        self.first_name.setPlaceholderText(_translate("MainWindow", "First Name"))
        self.email.setPlaceholderText(_translate("MainWindow", "E-mail"))
        self.submit.setText(_translate("MainWindow", "Save"))
        self.label_6.setText(_translate("MainWindow", "Notes:"))
        self.label_7.setText(_translate("MainWindow", "ADD CONTACT"))
        self.notes.setPlaceholderText(_translate("MainWindow", "Notes..."))
        self.telephone.setPlaceholderText(_translate("MainWindow", "Telephone"))
        self.back_button.setText(_translate("MainWindow", "Back"))
        self.label_1.setText(_translate("MainWindow", "First Name:"))
        self.label_2.setText(_translate("MainWindow", "Last Name:"))
        self.label_5.setText(_translate("MainWindow", "Url:"))
        self.label_3.setText(_translate("MainWindow", "Telephone:"))
        self.label_8.setText(_translate("MainWindow", "First Name Required"))
        self.label_9.setText(_translate("MainWindow", "Last Name Required"))
        self.last_name.setPlaceholderText(_translate("MainWindow", "Last Name"))
        self.label_4.setText(_translate("MainWindow", "E-mail:"))
        self.url.setPlaceholderText(_translate("MainWindow", "URL"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

