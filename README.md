# contactManager

### Description
This project is a programming assignment done for Human Computer Interaction exam.
It consists in a Contact Manager application implemented in python.

### Dependencies
 * [PyQt 5.9.2]( https://pypi.org/project/PyQt5/5.9.2/)
 * [PyMongo 3.12.0](https://docs.mongodb.com/drivers/pymongo/)

### Implementation
This application implement the MVC ( Model-View-Controller) pattern where the Model is :
 *  contact_model.py

the Views are :
 * contactlist_view.py
 * contactadd_view.py
 * contactinfo_view.py 
 
and the Controllers are :
 * contactlist_controller.py
 * contactadd_controller.py
 * contactinfo_controller.py

All interface are implemented with PyQt5 and converted in python through "pyuic" tool. In this way, I separate the view from the controller and editing the design of the view doesn't involve the editing of the controller.

To store the data I used MongoDB , a noSQL database. Docker is used to run MongoDB.
