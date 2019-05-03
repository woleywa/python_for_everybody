import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER, organization TEXT)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    # print(pieces)
    email = pieces[1]
    orgvalue = email.split("@",1)[1]
    # input('Please press enter to continue')
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count, organization)
                VALUES (?, 1 , ?)''', (email,orgvalue))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count, organization FROM Counts ORDER BY count DESC LIMIT 10'
# countorg = 'SELECT email, count FROM Counts GROUP BY '

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1], row[2])

cur.close()
