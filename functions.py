import sqlite3

def get_match_data():
    conn = sqlite3.connect('wiigolf.db')
    c = conn.cursor()
    c.execute('SELECT * FROM MATCHES ORDER BY ROWID ASC LIMIT 1')

    tst = c.fetchall()[0]
    retval = """<h1> Latest Wii Golf Match </h1>

    <br>

    <table>
        <tr>
            <th>Player</th>
            <th>Score</th>
        </tr>
        <tr>
            <td>%s</td>
            <td>%s</td>
        </tr>
        <tr>
            <td>%s</td>
            <td>%s</td>
        </tr>


    """ % (tst[0],tst[1],tst[2],tst[3])





    return (retval)

