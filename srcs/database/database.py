import pyrebase
config = {
  "apiKey": "Your API Key",
  "authDomain": "YourprojectId.firebaseapp.com",
  "databaseURL": "https://YourdatabaseName.firebaseio.com",
  "storageBucket": "YourprojectId.appspot.com",
  "serviceAccount": "path/toyour/serviceAccountCredentials.json"
}
# initialisatiing pyrebase
firebase = pyrebase.initialize_app(config)

# initialisatiing Database
db = firebase.database()

# selecting the column in the database
#db.child("users").child("Morty")

# How to save a data
#data = {"name": "Mortimer 'Morty' Smith"}
#db.child("users").push(data)

# How to update a existing data
#db.child("users").child("Morty").update({"name": "Mortiest Morty"})

# Removing existing data
#db.child("users").child("Morty").remove()

# reterving the data
#users = db.child("users").get()
#print(users.val()) #  retervies  this data => {"Morty": {"name": "Mortimer 'Morty' Smith"}, "Rick": {"name": "Rick Sanchez"}}

