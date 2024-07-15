import pyrebase

config = {"apiKey": "AIzaSyC69PvKjmsflCDrFO7HOQU3QvdqnL0IXXo",
  "authDomain": "planets-8f0eb.firebaseapp.com",
  "projectId": "planets-8f0eb",
  "databaseURL" : "https://planets-8f0eb-default-rtdb.firebaseio.com/",
  "storageBucket": "planets-8f0eb.appspot.com",
  "messagingSenderId": "610933293529",
  "appId": "1:610933293529:web:6686228f321410520cd9c8",
  "measurementId": "G-HY82P1YEXJ"
  }

Firebase = pyrebase.initialize_app(config)
db = Firebase.database()

a = db.child("Star Wars").get()
a = a.val()
#print(a[1]['Clima'])
