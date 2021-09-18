from PyQt5 import QtWidgets
import contactinfo_view
from contact_model import Contact
import contactlist_controller

class ContactInfoController(QtWidgets.QMainWindow):
    def __init__(self,contact):
        super(ContactInfoController,self).__init__()
        self.contact = contact
        self.view = contactinfo_view.Ui_MainWindow()
        self.view.setupUi(self)
        self.addBehavior()
        self.showInfo()

    def addBehavior(self):
        self.view.submit.clicked.connect(self.saveContact)
        self.view.delete_button.clicked.connect(self.deleteContact)
        self.view.back_button.clicked.connect(self.changeToListView)
    
    #function used to show info contact
    def showInfo(self):
        self.view.contact_name.setText(self.contact.getName()[1]+ " " + self.contact.getSurname()[1])
        self.view.first_name.setText(self.contact.getName()[1])
        self.view.last_name.setText(self.contact.getSurname()[1])
        self.view.email.setText(self.contact.getEmail()[1])
        self.view.telephone.setText(self.contact.getPhone()[1])
        self.view.url.setText(self.contact.getUrl()[1])
        self.view.notes.setText(self.contact.getNotes()[1])
       
    #function used to delete contact from the list 
    def deleteContact(self):
        name = self.view.first_name.text()
        surname = self.view.last_name.text()
        phone = self.view.telephone.text()
        email = self.view.email.text()
        url = self.view.url.text()
        notes = self.view.notes.toPlainText()
        
        contactToDelete = Contact()
    
        id = self.contact.getId()[1]
        print(id, name, surname,email,phone,url,notes)
        contactToDelete.setField(id, name, surname,email,phone,url,notes)
        contactToDelete.deleteContact()
        
        self.changeToListView()
    
    #fucntion used to save the modified contact
    def saveContact(self):
        if (self.view.first_name.text() == "" ):  
            self.view.label_8.show()
            self.view.label_9.hide() 
        elif (self.view.last_name.text() == ""):
            self.view.label_9.show() 
            self.view.label_8.hide()  
        else:
            name = self.view.first_name.text()
            surname = self.view.last_name.text()
            phone = self.view.telephone.text()
            email = self.view.email.text()
            url = self.view.url.text()
            notes = self.view.notes.toPlainText()
            
            if (name != None and name != "" and surname != None and surname != ""):
                id = self.contact.getId()[1]
                self.contact.updateContact(id,name,surname,email,phone,url,notes)
                
            self.changeToListView()
     
    #change the view to List contacts   
    def changeToListView(self):
        self.view.homeWindow = QtWidgets.QMainWindow()
        self.view.ui = contactlist_controller.ContactlistController()
        self.view.mv.close()
        self.view.ui.show()