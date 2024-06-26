import sqlite3

peopleValues = (('Ron', 'Obvious', 42), ('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))

with sqlite3.connect('test_db.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS People")
    c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")

    c.executemany("INSERT INTO People VALUES (?, ?, ?)", peopleValues)

    #select all first and last names from people over age 30
        c.execute("SELECT FisrtName, LastName FROM People WHERE Age > 30"
                  for row in c.fetchall():
                    print(row)