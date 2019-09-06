import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect('localhost', 'root', '123456', 'engine', 'utf8')
    cursor = db.cursor()
    cursor.execute('SELECT VERSION()')

    data = cursor.fetchone()

    print("Database version : %s " % data)

    # 关闭数据库连接
    db.close()
