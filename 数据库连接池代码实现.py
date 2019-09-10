import time
import pymysql
import threading
from DBUtils.PooledDB import PooledDB,SharedDBConnection
POOL = PooledDB(
    creator=pymysql,
    maxconnections=8,
    mincached=2,
    maxcached=5,
    maxshared=3,#没有用，pymysql默认是threadsafy默认是一，默认全部被共享。
    blocking=True,#如果是False的话不等待会报错
    maxusage=None, #一个链接最多被使用的次数，None表示无限制
    setsession=[], #开始绘制性的命令列表，
    ping=9, #检查数据库连接是否可用的间隔时间
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123',
    database='pooldb',
    charset='utf8',

)

def fun():
    conn = POOL.connection()
    cursor = conn.cursor()
    cursor.execute('select * from tb1')
    result = cursor.fetchall()
    print(result)
    conn.close()
