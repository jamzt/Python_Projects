import sqlite3
connection = sqlite3.connect("/Users/jamz/Desktop/test_db.db")
c = connection.cursor()
c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")