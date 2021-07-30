import sqlite3

conn = sqlite3.connect('submission1.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_filelists( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        file_name  TEXT \
        )")
    conn.commit()
conn.close()


conn = sqlite3.connect('submission1.db')

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')


conn.commit()
conn.close()

conn = sqlite3.connect('submission1.db')

with conn:
    cur = conn.cursor()

for file in fileList:
    if file.endswith('.txt'):
        cur.execute("INSERT INTO tbl_filelists (file_name) VALUES (?)", (file,))
        print (file)

conn.commit()
conn.close()






