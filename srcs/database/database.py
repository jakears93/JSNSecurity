import pyrebase

config = {
        "apiKey": "19b17a41c94eeece3ba3a29a0095cf52f89392ed",
        "authDomain": "https://JDSecurity.firebaseio.com",
	"databaseURL": "https://jdsecuritysolutions-5726a.firebaseio.com/",
	"storageBucket": "gs://jdsecuritysolutions-5726a.appspot.com/",
}


# initialisatiing pyrebase
firebase = pyrebase.initialize_app(config)

# initialisatiing Database
db = firebase.database()

# selecting the column in the database
db.child("users").child("Morty")

# How to save a data
data = {"name": "Mortimer 'Morty' Smith"}
db.child("Rick").push(data)

# How to update a existing data
#db.child("users").child("Morty").update({"name": "Mortiest Morty"})

# Removing existing data
#db.child("users").child("Morty").remove()

# reterving the data
#users = db.child("users").get()
#print(users.val()) #  retervies  this data => {"Morty": {"name": "Mortimer 'Morty' Smith"}, "Rick": {"name": "Rick Sanchez"}}

