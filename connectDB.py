import sqlite3
path = "D:/sqlite/CSDL.db"
connection = sqlite3.connect(path)
print(connection)

def show_data():
    cursor = connection.cursor()
    sql = "SELECT ten,sdt,ten_san,h_start,m_start,h_stop,m_stop,date FROM khach_hang join san on khach_hang.id_san = san.id"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result
    connection.close()

def show_data_spin_box():
    cursor = connection.cursor()
    sql = "SELECT id FROM SAN"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def add_data_khach():
    cursor = connection.cursor()
    sql = 'insert into khach_hang values(?,?,?,?)'
    data = (111,222,333,444)
    cursor.execute(sql,data)
    result = cursor.fetchall()
    connection.commit()
    connection.close()
