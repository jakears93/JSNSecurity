import pyrebase

config = {
        "apiKey": "19b17a41c94eeece3ba3a29a0095cf52f89392ed",
        "authDomain": "https://JDSecurity.firebaseio.com",
	"databaseURL": "https://jdsecuritysolutions-5726a.firebaseio.com/",
	"storageBucket": "jdsecuritysolutions-5726a.appspot.com",
}


# initialisatiing pyrebase
firebase = pyrebase.initialize_app(config)

# initialisatiing Database
#db = firebase.database()

username = "jacob"
room = "BedRoom"

#storagepath = username+"/"+room+"/test.txt"

storage = firebase.storage()
#fbupload = storage.child(storagepath).put("test.txt")


# selecting the column in the database
#db.child("Usernames")

# How to save a data
#data = {"name": "Mortimer 'Morty' Smith",
#        "email": "wuubalubadubdub",
#        "password": "mrmeeseeks",
#        "username": "Morty"}

#db.child("Morty").push(data)

# How to update a existing data
#db.child("Morty").update(data)

# Removing existing data
#db.child("users").child("Morty").remove()

# reterving all the data
storage.child("jacob/BedRoom/test.txt").put("test.txt")



#retieve data by name
#user_by_name = db.child("Usernames").order_by_child("name").get()


#print(user_by_name.val())
