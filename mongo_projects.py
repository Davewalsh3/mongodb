# 1 This is an example of MENU DRIVEN FRONT END
#  1-DATABASE WITH PYMONGO/PYTHON3
# 2- adding a helper functions for later

import pymongo  # 1 MONGO CONNECTION FUNCTION
import os
if os.path.exists("env.py"):
    import env


MONGODB_URI = os.environ.get("MONGODB_URIs")

DBS_NAME = "mytestdatabase"

COLLECTION_NAME = "myfirstmdb"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Welcome to your DB Intrfce Dave..")  # can delete this L8R
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e  # end mngo cnct fnctn


def show_menu():  # 1 creates our showmenu() function for userIntfce
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")

    option = input("Enter option: ")  # 1 CREATE variable 'option'
    return option  # 1 'ask user to enter an option/value'


def get_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")

    try:
        doc = coll.find_one({'first': first.lower(), 'last': last.lower()})
    except:
        print("Error accessing the database")

    if not doc:
        print("")
        print("no results found")

    return doc


def add_record():  # 1 fNCTN TO ALLW US 2 ADD RCRDS

    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    dob = input("Enter date of birth > ")
    gender = input("Enter gender > ")
    hair_colour = input("Enter hair colour > ")
    occupation = input("Enter occupation > ")
    nationality = input("Enter nationality > ")

    new_doc = {'first': first.lower(), 'last': last.lower(), 'dob': dob,
               'gender': gender, 'hair_colour': hair_colour, 'occupation':
               occupation, 'nationality': nationality}

    try:
        coll.insert(new_doc)
        print("")
        print("Document inserted")
    except:
        print("Error accessing the database")


def find_record():  # defined find record function
    doc = get_record()
    if doc:
        print("")  # = if we have results print blank line first
        for k, v in doc.items():  # iterate through each indiv. k/v in dict
            if k != "_id":  # if k not = (mongo)id, print the key
                print(k.capitalize() + ": " + v.capitalize())


def edit_record():
    doc = get_record()
    if doc:
        update_doc = {}
        print("")  # = if we have results print blank line first
        for k, v in doc.items():  # iterate through each indiv. k/v in dict
            if k != "_id":  # if k not = (mongo)id, print the key
                update_doc[k] = input(k.capitalize() + " [" + v + "] > ")

                if update_doc[k] == "":
                    update_doc[k] = v

    try:
        coll.update_one(doc, {'$set': update_doc})
        print("")
        print("document updated")
    except:
        print("error accessing the database")


def main_loop():  # 1 main loop wil cntnue to cll our mnu evrytme we cm bk 2it
    while True:
        option = show_menu()
        if option == "1":
            add_record()  # 1 this calls our new function (add record)
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":  # 1 if we slct 5, close cnction(break)
            conn.close()
            break
        else:  # 1 if we dnt slct any 1-5 we prnt 'invld optn'
            print("Invalid option")
        print("")  # 1 main loop function created ending here


conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()
