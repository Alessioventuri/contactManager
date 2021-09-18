

import pymongo

# database used to store contact
class Database:
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = myclient["contactmanager"]
    mycol = mydb["contact"]
    
    #function used to store contact inside the db
    def savecontact(self,id,name,surname,email,phone,url,notes):
        mylist = {"id": id, "firstname" : name, "lastname" : surname, "email" : email, "phone": phone, "url": url, "notes": notes}
        x = self.mycol.insert_one(mylist) 
     
    #function used to get contact from a id    
    def getContactFromId(self,id):
        result = self.mycol.find({"id":id})
        return result[0]
    #function used to get all contacts   
    def getContacts(self):
        result = self.mycol.find()
        return result
    #function used to get all contacts with certain name
    def getContactsFromText(self,text):
        results = self.mycol.find({"firstname":text})
        return results
    #function used to delete contact from database
    def deleteContact(self,id):
        self.mycol.delete_one({"id" : id})
    #function used to update contact   
    def updateContact(self,id,name,surname,email,phone,url,notes):
        self.mycol.update_one({"id" :id},{"$set":{"firstname":name,"lastname":surname,"email":email,"phone":phone,"url":url,"notes":notes}})