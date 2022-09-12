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
    except Error as e:
        print(e)
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

def insert_player_data(player,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13,h14,h15,h16,h17,h18,tscore):
    #TODO: Create better validation of scores
    
    values = [h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13,h14,h15,h16,h17,h18]
    total = 0
    for i in values:
        if i == 0:
            return 0
        total = total + i
    if total != tscore:
        return 0
    try:
            conn = sqlite3.connect('wiigolf.db')
    except Error as e:
            print(e)
            return 0
    c = conn.cursor()
    execute_string = f"INSERT INTO PLAYERS (PNAME,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13,h14,h15,h16,h17,h18,SCORE) values ('{player}',{h1},{h2},{h3},{h4},{h5},{h6},{h7},{h8},{h9},{h10},{h11},{h12},{h13},{h14},{h15},{h16},{h17},{h18},{tscore})"
    try:
        c.execute(execute_string)
    except Error as e:
        print(e)
        conn.close()
        return 0
    conn.commit()
    conn.close()


    return 1

def get_average_round(player):
#TODO write function to update the average score within the database
    try:
        conn = sqlite3.connect('wiigolf.db')
    except Error as e:
        print(e)
        return []
    c = conn.cursor()
    execute_string = f"Select SCORE FROM PLAYERS WHERE PNAME = '{player}'"
    c.execute(execute_string)
    data = c.fetchall()
    if data == []:
        conn.close()
        return data
    avg = 0
    for i in data:
        avg = avg + i[0]
    avg = avg/len(data)
    conn.close

    return avg

def connect_db():
    try:
        conn = sqlite3.connect('wiigolf.db')
    except Error as e:
        print(e)
        return None
    return conn

def get_all_average_rounds():
##TODO write function to get data from database
    conn = connect_db()
    if conn == None:
        return {}
    c = conn.cursor()
    execute_string = f"SELECT DISTINCT PNAME FROM PLAYERS"
    c.execute(execute_string)
    data = c.fetchall()
    averages = {}
    for pname in data:
        averages[pname[0]] = get_average_round(pname[0])
    return averages

