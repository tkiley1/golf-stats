import sqlite3
import hashlib
import statistics

def get_match_data():
    conn = sqlite3.connect('wiigolf.db')
    c = conn.cursor()
    c.execute('SELECT * FROM MATCHES')
    
    retval = "<h1> Latest Wii Golf Matches </h1>"
    tst = c.fetchall()

    #manual HTML table depricated
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
    #####
    c.close()


    retval = retval + "</table>"
    return (tst)

def new_user_reg(username, password):
    try:
        conn = sqlite3.connect('wiigolf.db')
    except:
        return "Failed to connect to database - try again."
    c = conn.cursor()
    execute_string = f"SELECT * FROM ACCOUNTS WHERE UNAME = '{username}'"
    c.execute(execute_string)
    if len(c.fetchall()) == 0:
        entry_string = f"INSERT INTO ACCOUNTS (UNAME, PASSWORD) VALUES ('{username}','{password}')"
        conn.execute(entry_string)
        conn.commit()
        conn.close()
        return 'SUCCESS'
    return "Username taken - try a different one"

def user_login(username, password):
    try:
        conn = sqlite3.connect('wiigolf.db')
    except:
        return "Failed to connect to database - try again."

    c = conn.cursor()
    execute_string = f"SELECT * FROM ACCOUNTS WHERE UNAME = '{username}'"
    c.execute(execute_string)
    data = c.fetchall()
    if len(data) == 0:
        conn.close()
        return "Incorrect username or password."
    if str(password) == str(data[0][1]):
        conn.close()
        return "SUCCESS"
    conn.close()
    return "Incorrect username or password."

def get_player_data(pname):
    try:
        conn = sqlite3.connect('wiigolf.db')
    except:
        return []
    c = conn.cursor()
    execute_string = f"SELECT * FROM PLAYERS WHERE PNAME = '{pname}'"
    c.execute(execute_string)
    data = c.fetchall()
    if len(data) == 0:
        conn.close()
        return []
    conn.close()
    stats = ['Average']
    volatility = ['Consistency Factor']
    for j in range(19):
        tmp = 0
        lst = []
        for i in range(len(data)):
            tmp = tmp + data[i][j+1]
            lst = lst + [data[i][j+1]]
        tmp = tmp / len(data)
        vol = statistics.stdev(lst)
        volatility = volatility + [format(vol, '.2f')]
        stats = stats + [format(tmp, '.2f')]
    data = data + [tuple(stats)] + [tuple(volatility)]

    return data

