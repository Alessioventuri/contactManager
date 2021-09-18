from PyQt5 import QtWidgets
import pymongo
import contactlist_view
import adapterbutton
import numpy as np
from contact_model import Contact
import  contactadd_controller, contactinfo_controller

class ContactlistController(QtWidgets.QMainWindow):
    def __init__(self):
        super(ContactlistController,self).__init__()
        self.view = contactlist_view.Ui_MainWindow()
        self.view.setupUi(self)
        self.addBehavior()
        self.showContacts()
    
    def addBehavior(self):
        self.view.search_button.clicked.connect(self.searchContacts)
        self.view.add_button.clicked.connect(self.changeToAdderView)
    
    #function used to show the list of contacts   
    def showContacts(self):
        contacts = Contact().showContacts()
        if contacts != None :
            contacts.sort("firstname",pymongo.ASCENDING)
            for contact in contacts:
                obj = Contact()
                contact_ = list(contact.items())
                contactarray = np.array(contact_)
                obj.setField(contactarray[1],contactarray[2],contactarray[3],contactarray[4],
                             contactarray[5],contactarray[6],contactarray[7])
                button = adapterbutton.ButtonAdapterView(obj,self.view.mv)
                self.view.buttonListLayout_2.addWidget(button)
    
    #function used to search contacts inside the list            
    def searchContacts(self):
        search_name = self.view.search_text.text()
        contactSerch = Contact()
        for i in reversed(range(self.view.buttonListLayout_2.count())):
            self.view.buttonListLayout_2.itemAt(i).widget().setParent(None)
        if search_name == "":
            self.showContacts()
        if search_name != "":
            contact_searched = contactSerch.getContactFromtext(search_name)
            for contact in contact_searched:
                print(contact)
                contact_ = list(contact.items())
                contactarray = np.array(contact_)
                if (contactarray[2][1] != None or contactarray[2][1] != ""):
                    obj = Contact()
                    obj.setField(contactarray[1],contactarray[2],contactarray[3],contactarray[4],
                             contactarray[5],contactarray[6],contactarray[7])
                    button = adapterbutton.ButtonAdapterView(obj,self.view.mv)
                    self.view.buttonListLayout_2.addWidget(button)
                    
    # change view to add new contact               
    def changeToAdderView(self):
        self.view.homeWindow = QtWidgets.QMainWindow()
        self.view.ui = contactadd_controller.ContactAddController()
        self.view.mv.close()
        self.view.ui.show()
    
    # change view to contact info
    def changeToInfoView(self):
        self.view.homeWindow = QtWidgets.QMainWindow()
        self.view.ui = contactinfo_controller.ContactInfoController()
        self.view.mv.close()
        self.view.ui.show()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    listcontrol = ContactlistController()
    listcontrol.show()
    sys.exit(app.exec_())