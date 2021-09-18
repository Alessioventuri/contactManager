from db import Database

# model for the contact
class Contact():
    def _init_(self):
        self.id = ""
        self.name = ""
        self.surname = ""
        self.email = ""
        self.phone = ""
        self.url = ""
        self.notes = ""
        
    def setField(self, id,name, surname, email, phone, url, notes):
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone
        self.url = url
        self.notes = notes

    def setId(self,id):
        self.id = id
        
    def setName(self, name):
        self.name = name
        
    def setSurname(self, surname):
        self.surname = surname
        
    def setPhone(self,phone):
        self.phone = phone
        
    def setEmail(self,email):
        self.email = email
        
    def setUrl(self,url):
        self.url = url
        
    def setNotes(self,notes):
        self.notes = notes
    
    def getId(self):
        return self.id
    def getName(self):
        return self.name
    def getSurname(self):
        return self.surname
    def getEmail(self):
        return self.email
    def getPhone(self):
        return self.phone
    def getUrl(self):
        return self.url
    def getNotes(self):
        return self.notes
    
    #function used to store contact inside the database
    def saveContact(self):
        id = self.id
        name = self.name
        surname = self.surname
        email = self.email
        phone = self.phone
        url = self.url
        notes = self.notes
        db = Database()
        if (name != None and name != "" and surname != None and surname != ""):
            db.savecontact(id, name, surname, email, phone, url, notes)
    
    #function used to get contact from Id
    def getContactFromId(self):
        db = Database()
        contact = db.getContactFromId(self.id)
        return contact
    
    #function used to show all contacts
    def showContacts(self):
        db = Database()
        contacts = db.getContacts()
        return contacts
    
    #function used to delete contact from database
    def deleteContact(self):
        db = Database()
        db.deleteContact(self.id)
    
    #function used to get contact from search
    def getContactFromtext(self,text):
        db = Database()
        contacts = db.getContactsFromText(text)
        return contacts

    #function used to update contact inside the database
    def updateContact(self,id,name,surname,email,phone,url,notes):
        db = Database()
        db.updateContact(id,name,surname,email,phone,url,notes)
        