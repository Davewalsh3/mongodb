import pymongo  #MONGO CONNECTION FUNCTION
import os
if os.path.exists("env.py"):
    import env


MONGODB_URI = os.environ.get("MONGODB_URIs")

DBS_NAME = "mytestdatabase"

COLLECTION_NAME = "myfirstmdb"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print(" Oh, what a day... what a lovely day!")  # can delete this L8R
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e  # END OF MONGO CONNECT


def show_menu():  # creates our showmenu() function for userIntfce
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")

    option = input("Enter option: ")  # CREATE variable 'option'
    return option  # 'ask user to enter an option/value'


def main_loop():  # main loop, wil cntnue to cll our mnu evrytme we cm bk 2it
    while True:
        option = show_menu()
        if option == "1":
            print("You have selected option 1")
        elif option == "2":
            print("You have selected option 2")
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":  #if we slct 5, close cnction(break)
            conn.close() 
            break
        else:  # if we dnt slct any 1-5 we prnt 'invld optn'
            print("Invalid option")
        print("")  # main loop function created ending here


conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()