import sqlite3

conn = sqlite3.connect('2w_2ex.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (organization TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    orgvalue = pieces[1].split("@",1)[1]
    cur.execute('SELECT count FROM Counts WHERE organization = ? ', (orgvalue,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (organization, count)
                VALUES (?, 1)''', (orgvalue,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE organization = ?',
                    (orgvalue,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT organization, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])


cur.close()
