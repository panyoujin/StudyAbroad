# coding:utf-8
import pymysql
import contextlib
import configparser

cf = configparser.ConfigParser()
cf.read("ConfigParser.conf")
db_host = cf.get("mysql","db_host")
db_port = cf.getint("mysql","db_port")
db_user = cf.get("mysql","db_user")
db_pass = cf.get("mysql","db_pass")
db_name = cf.get("mysql","db_name")


#定义上下文管理器，连接后自动关闭连接
@contextlib.contextmanager
def mysql():
  conn = pymysql.connect(host=db_host, port=db_port, user=db_user, passwd=db_pass, db=db_name, charset='utf8')
  cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
  try:
    yield cursor
  except Exception as err:
    conn.rollback()
    cursor.close()
    conn.close()
  finally:
    conn.commit()
    cursor.close()
    conn.close()

#获取列表
def get_list(sql,args):
  row_list = []
  with mysql() as cursor:
      cursor.execute(sql%args)
      row_list = cursor.fetchall()
  return row_list

#获取对象
def get_object(sql,args):
  with mysql() as cursor:
    cursor.execute(sql%args)
    row_list = cursor.fetchall()
    if len(row_list) > 0 :
      return row_list[0]

#新增或者修改对象
def operate_object(sql,args):
  with mysql() as cursor:
    row_count = cursor.execute(sql%args)
    return row_count

def operate__many(sql_list,args_list):
  with mysql() as cursor:
    count = 0
    for sql_item in sql_list:
      cursor.execute(sql_item%args_list[count])
      count+=1
    return count