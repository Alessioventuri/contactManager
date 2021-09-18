from PyQt5 import QtWidgets, QtCore
import contactadd_view
from contact_model import Contact
import random
import contactlist_controller

class ContactAddController(QtWidgets.QMainWindow):
    def __init__(self):
        super(ContactAddController,self).__init__()
        self.view = contactadd_view.Ui_MainWindow()
        self.view.setupUi(self)
        self.addBehavior()
    
    def addBehavior(self):
        self.view.back_button.clicked.connect(self.changeToListView)
        self.view.submit.clicked.connect(self.saveContact)
    
    # ausiliar function that enable or disable the save button
    def enableSave(self):
        if (self.view.first_name.text() != "" and self.view.last_name.text() != ""):
            self.view.submit.setEnabled(True)
        else:
            self.view.submit.setEnabled(False)
    
    # function that allow to save the contact 
    def saveContact(self):
        if (self.view.first_name.text() == "" ):  
            self.view.label_8.show()
            self.view.label_9.hide()
        elif (self.view.last_name.text() == ""):
            self.view.label_8.hide()
            self.view.label_9.show()
        else:    
            name = self.view.first_name.text()
            surname = self.view.last_name.text()
            email = self.view.email.text()
            phone = self.view.telephone.text()
            url = self.view.url.text()
            notes = self.view.notes.toPlainText()  
            print(surname,email,phone,url,notes)  
            
            if (name != None and name != "" and surname != "" and surname != None):
                new = Contact()
                id = "".join(random.choice("0123456789abcdefghilmnopqrstuvz") for _ in range(10))
                new.setField(id, name,surname,email,phone,url,notes)
                new.saveContact()
                
            self.changeToListView()
        
    # change the view to List contact
    def changeToListView(self):
        self.view.homeWindow = QtWidgets.QMainWindow()
        self.view.ui = contactlist_controller.ContactlistController()
        self.view.mv.close()
        self.view.ui.show()   
            
            
            
    