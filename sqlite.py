import sqlite3
connection = sqlite3.connect("/Users/jamz/Desktop/test_db.db")
c = connection.cursor()
c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)")
connection.commit()
connection =sqlite3.connect(':memory:')
c.execute("DROP TABLE IF EXISTS People")
connection.close()
with sqlite3.connect("test_db.db") as connection:
    #perform any sql ops using connection here

# executing multiline of sql with semicolon
import sqlite3
with sqlite3.conect('test_db.db') as connection:
    c = coneection.cursor()
    c.executescript("""DROP TABLE IF EXISTS People;
                    CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);
                    INSERT INTO People('Ron', 'Obvious', '42');
                    """)
    

    peopleValues = (('Luigi', 'Vercotti', '43'), ('Arthur', 'Belling', 28))
    c.executemany("INSERT INTO People VALUE(?, ?, ?)", peopleValues)