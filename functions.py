import sqlite3

def get_match_data():
    conn = sqlite3.connect('wiigolf.db')
    c = conn.cursor()
    c.execute('SELECT * FROM MATCHES ORDER BY ROWID ASC LIMIT 5')
    
    retval = "<h1> Latest Wii Golf Matches </h1>"
    tst = c.fetchall()
    for i in range(5):


        retval = retval + """

    <br>

    <table>
        <tr>
            <th>Player</th>
            <th>Score</th>
            <th>Winner</th>
        </tr>
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
        </tr>
        <tr>
            <td>%s</td>
            <td>%s</td>
        </tr>



        """ % (tst[i][0],tst[i][1],tst[i][4],tst[i][2],tst[i][3])
    c.close()


    retval = retval + "</table>"
    return (retval)

