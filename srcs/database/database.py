import pyrebase
config = {
	"apiKey": "5YKnTyh4dPVxoD7Ov26a5ifqt3EXNPLPHJ6Vtphl",
	#19b17a41c94eeece3ba3a29a0095cf52f89392ed
	"databaseURL": "https://jdsecuritysolutions-5726a.firebaseio.com/",
	"storageBucket": "gs://jdsecuritysolutions-5726a.appspot.com/",
	"serviceAccount": "path/toyour/serviceAccountCredentials.json"
}

#MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDkrwZXgZMt32K4\niiDufGFC0Fo1JAy8ZNpPXisfTBZQTO11gdaaLA3yKEe4GIjmDdPSo9t0pmwG4Yhi\nBpVAMQdIhYqiyjc+gugSXVeq9AgCraVmzee0A4ZVpq2KPAg3WzK/84j9Ww/xl7n4\n0IiV9tD617gYBm24TnSZy/JPAciqSej0RaO0duwDefa7tXqRIe3Oln8GWGkHA/YL\nqkjp10E4ZrT/PyGSL/KuJbAYgz3xv+FEy9md6f7BGsZ+3vQMgVWht5OgmjtmMhDJ\n54l7Fg+lwSHphp0xp0lhpmYgCzUSkAFwe8E5GM0JrdTj+Cui6eXY6seOr0KTeDgh\nr2gOnWnfAgMBAAECggEARTORv7k+SIto3F8wR/rrk8RpB9u43unGBm6Arh/gQLyG\nvyBjSJQ8RCNcUKFcDAHzL7LWHh6eYhatprxHPf2YLqH6qfh3bzs97xDADsN6CRVz\nEAEPNLI8XH7r1QEFm3rFiMCxm7mKwZkgdeLk8jyWUNImq16GpVdYgZHt6Wqoxp60\nlBdNIrdiWR6s88GVpfs127tdh5L+7VsWD3jDikFo0von+b0xOKGJLUXDuSN0JnlI\ndi3PdbKl/3AdSB7+Ljto92hYRrb7z7pJ9i+kH3se9PEEHGnT/zt/IjoYkHGMhXWb\n2qJIHQvjJkKOJaJB/aSJDIwDYdT2DurhhQnrVgJVwQKBgQD57n8rT+gr2xEsc3RV\nXScBY3Aex4JK96QQTj7jJsCPHT860hVIi3rVs87T9+QYuDTMs+gdYMM5j5IVBLub\nilcly2HcCVQML4oKHgl5fyrgJikBtSdrV+Yjm7bO+cS2eWT+1AuauQM/h8gRQYWw\nun5R4kV86S4fS9UzC1QzVvmiUwKBgQDqPHT596fHe7uisw1JdJ1QSrVIJW0CsIyR\ncM9svspx0S0ebLWiOCMR1yOF6cwaDAkUkqrdjIlyPiguOJyAGIBs72lyADQUe968\nanp7mZ4rDp64qRc2RwSaL1souU0KIBxuup3CVu6eT/IZcoafQmKcUGxJ85H4yW6N\n6vCGm/6AxQKBgQDUNSE6yD0MR5PcVyc2d8JvlluTdrh1KLDfu2AABF5I5X9TVR8H\nGo6wNlxtc7PzHSyPhk2V7Bu2muVg/UTBuwNlrrsnVbBMLG0bTAelZkkkSqJUtdiD\ndv2LzGG6eS4B9S7Ag5Baza4pWgOQSz7VIHOy2NlBRseHgR7DmWHjuXx5ywKBgQCM\nGB6qhqnNkL6Xv9l5joqsRBKKlP/O9QMN1dfppW71hfMjWEeGP2cSO4deh4fwKDSi\nHlqdaXmnX2+uvWM05fKhtMtvSJndinycWl7pX+aOwA7ESTW929nv0dUG1VUzciMv\nQuQqIM5U12HoQGwuAolyDlPGIyyyDN/Xd6XmDJS6NQKBgAeHi5ceTRs2V1t9JKa7\nw6zKAw1gqqkxPy93QVJbC1TWLB1UACEIfyjdQ6uFWx6bU1I2Cx71nZTsobKzNAIw\nep5TjtEgYMWxcOa6hhN8jYkqEuWhpTupL+3KUd7VweSQfEPrbSeK46KiaXFSnqyu\nKE0IC0eWrUtcF2yiZJcuS69R


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

