from PyQt5 import QtWidgets
import contactinfo_controller

class ButtonAdapterView(QtWidgets.QPushButton):
    def __init__(self,contact,mainWindow):
        super(ButtonAdapterView,self).__init__()
        self.mv = mainWindow
        self.contact = contact
        self.defineButton()
        
    #function used to define the contact a clickable button
    def defineButton(self):
        self.setText(self.contact.getName()[1] + " " + self.contact.getSurname()[1])
        self.setFixedHeight(50)
        self.clicked.connect(self.changeToInfoView)
        
    #function used to change View to contactInfo    
    def changeToInfoView(self):
        self.homeWindow = QtWidgets.QMainWindow()
        self.ui = contactinfo_controller.ContactInfoController(self.contact)
        self.mv.close()
        self.ui.show()