import sqlite3
fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt','data.pdf', 'myPhoto.jpg')

# creating a database and table
def create_database():
    conn = sqlite3.connect('file_db.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS files
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, filename TEXT)''')
    conn.commit()
    conn.close()
#accesseing sqlite3 db to add files
def add_to_db(files):
    conn = sqlite3.connect('file_db.db')
    cursor = conn.cursor()

    for file in files:
        if file.endswith(".txt"):
            cursor.execute("INSERT INTO files (filename) VALUES (?)", (file,))
    conn.commit()
    conn.close()


def qualifying_files():
    conn = sqlite3.connect('file_db.db')
    cursor = conn.cursor()
    cursor.execute("SELECT filename FROM files WHERE filename LIKE '%.txt%'")
    qualifying_files = cursor.fetchall()
    for file in qualifying_files:
        print(file[0])
    conn.close()

if __name__ == "__main__":
  
    create_database()
    add_to_db(fileList)
    qualifying_files()
