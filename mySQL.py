import pymysql#一种写好的库，可自己pip安装，类似的库很多可以自行查找
from dbutils.pooled_db import PooledDB

def INSERT(name,age):
    sql = "INSERT INTO HUAWEI(name,age) VALUES ('%s', %d)"%(name,age)
    cursor.execute(sql)

def SELECT(name):
    sql = "select * from HUAWEI where name ='%s' limit 1"%name
    cursor.execute(sql)
    for row in cursor.fetchall():
        print("姓名:%s\t年龄:%d" % row)

def DELETE(data):
    if isinstance(data,int):
        sql = "DELETE FROM HUAWEI WHERE age = %d"%data
    else:
        sql = "DELETE FROM HUAWEI WHERE name = '%s'"%data
    cursor.execute(sql)

def UPDATE(old_name,old_age,new_name,new_age):
    sql = "UPDATE HUAWEI SET name = '%s' , age = %d WHERE name = '%s' and age = %d "%(new_name,new_age,old_name,old_age)
    cursor.execute(sql)

def InnerJoin():
    sql = "select * from HUAWEI INNER JOIN RECORDS ON HUAWEI.NAME=RECORDS.NAME"
    cursor.execute(sql)

def LeftJoin():
    sql = "select * from HUAWEI LEFT JOIN RECORDS ON HUAWEI.NAME=RECORDS.NAME"
    cursor.execute(sql)

param = {
    'host':'localhost',#本机
    'port':3306,#端口号，一般mysql为3306
    'db':'huawei',#数据库名
    'user':'root',#登陆用户
    'password':'Huawei@123',#登陆用户的密码
    'charset':'utf8',#字符编码
    'maxconnections': 0,     # 连接池允许的最大连接数
    'mincached': 4,          # 初始化时连接池中至少创建的空闲的连接，0表示不创建
    'maxcached': 0,          # 连接池中最多闲置的连接，0表示不限制，连接使用完成后的空闲连接保留数。
    'maxusage': 5,           # 每个连接最多被重复使用的次数，None表示不限制
    'blocking': True         # True 等待，让用户等待，尽可能的成功；
}

spool = PooledDB(pymysql, **db_config)
db = spool.connection() #建立连接对象
cursor = db.cursor() #使用cursor()方法创建一个游标对象cur（不理解没关系）

#这是在执行sql语句，execute里面的为删除数据表的语句
cursor.execute("DROP TABLE IF EXISTS HUAWEI")
cursor.execute("DROP TABLE IF EXISTS RECORDS")
# 创建表的sql语句
create_table_sql = """CREATE TABLE HUAWEI (
         NAME  VARCHAR(20) NOT NULL,
         AGE INT )"""
cursor.execute(create_table_sql)
create_table_sql = """CREATE TABLE RECORDS (
         NAME  VARCHAR(20) NOT NULL,
         SUBJECT  VARCHAR(20) NOT NULL,SCORE INT )"""
cursor.execute(create_table_sql)


# 关闭数据库连接
db.close()
