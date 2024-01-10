import sqlite3

fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'data.pdf', 'myPhoto.jpg')

#creating variable conn that will hold the db that is not created yet
conn = sqlite3.connect('files.db')
def create_db():
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        fileList TEXT, \
      )''')
    

    for fileName in tbl_files:
        if fileName.endswith('.txt'):
            cur.execute("INSERT INTO tbl_files(fileName) VALUES (?), (fileName,)")

    conn.commit()
conn.close()



conn = sqlite3.connect('files.db')
cursor = conn.cursor()
cursor.execute("SELECT files FROM tbl_files WHERE fileName LIKE '%.txt%'")
filesQualifying =cursor.fetchall()
for fileName in filesQualifying:
        msg = "Files with txt format: {} ".format(fileName[0])
print(msg)

conn.close()

if __name__ == "__main__":
     create_db()
     add_to_db(fileList)
     


    

