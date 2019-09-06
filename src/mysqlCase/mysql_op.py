# coding: utf-8
import pymysql

# @author zjw<cn.zjwblog@gmail.com>
# @time 2019-09-06 09:11 


conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    db='engine',
    charset='utf8'
)
cursor = conn.cursor()

rows_number = cursor.execute('select id from person')
print(rows_number)
print(cursor.fetchmany(3))
cursor.scroll(-2, 'relative')  # 游标移动到当前位置之后的5个，跳过5个，相对移动
print(cursor.fetchmany(3))
cursor.scroll(0, 'absolute')  # 游标移动到0号位置，绝对移动
print(cursor.fetchall())
cursor.scroll(-1, 'relative')
print(cursor.fetchall())
cursor.scroll(-1, 'relative')
print(cursor.fetchall())
