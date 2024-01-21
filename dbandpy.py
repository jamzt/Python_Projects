import sqlite3
connection = sqlite3.connect("/Users/jamz/Desktop/db_and_py.db")
c = connection.cursor()
c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")
#c.execute("INSERT INTO Roster VALUES('Jean-Baptiste Zorg', 'Human', 122)")
#c.execute("INSERT INTO Roster VALUES('Korben Dallas', 'Meat Popsicle', 100)")
#c.execute("INSERT INTO Roster VALUES('Ak'not', 'Magalore', \-5)")


#connection.commit()
#connection =sqlite3.connect(':memory:')
#c.execute("DROP TABLE IF EXISTS Roster")
#connection.close()
#with sqlite3.connect("test_db.db") as connection:
    #perform any sql ops using connection here

# executing multiline of sql with semicolon
#import sqlite3
#with sqlite3.conect('db_and_py_db.db') as connection:
#    c = coneection.cursor()
#    c.executescript("""DROP TABLE IF EXISTS Roster;
#                    CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT);
#                    INSERT INTO Roster('Jean-Baptiste Zorg', 'Human', '42');
#                    """)
    
RosterValues = [('Jean-Baptiste Zorg', 'Human', 122), ('Korben Dallas', 'Meat Popsicle', 100), ('Ak\'not', 'Magalore', -5)]
c.executemany("INSERT INTO Roster VALUES (?, ?, ?)", RosterValues)

connection.commit()
    
with sqlite3.connect('/Users/jamz/Desktop/db_and_py.db') as connection:
    c = connection.cursor()
    c.execute("UPDATE Roster SET Species='Human' WHERE Name='Korben Dallas' AND IQ=100")

connection.commit()

c.execute("SELECT Name, IQ FROM Roster WHERE Species='Human'")
for row in c.fetchall():
    print(row)

connection.commit()
connection.close()