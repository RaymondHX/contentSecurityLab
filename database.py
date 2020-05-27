"""
数据库连接模块
"""

import pymysql

class Mysql_Connect(object):
    #数据库连接
    def __init__(self, host, user, passwd, db):
        try:
            self.db = pymysql.connect(
                host="101.37.19.14",
                user=user,
 	            password=passwd,
                db=db,
                port=3306)
        except:
            print("数据库连接错误")
            self.db = None
            return
        #获取游标
        self.cursor = self.db.cursor()

    #增
    def insert(self, insert_words):
        try:
            # 执行sql语句
            self.cursor.execute(insert_words)
            # 提交到数据库执行
            self.db.commit()
            return True
        except:
            # 如果发生错误则回滚
            self.db.rollback()
            return False

    #查
    def select(self, select_words):
        try:
            # 执行SQL语句
            self.cursor.execute(select_words)
            self.db.commit()
            results = self.cursor.fetchall()
            return results
        except:
            print("Error: unable to fetch data")
            self.db.rollback()
            return None

    #改
    def update(self, update_words):
        try:
            # 执行SQL语句
            self.cursor.execute(update_words)
            # 提交到数据库执行
            self.db.commit()
            return True
        except:
            # 发生错误时回滚
            self.db.rollback()
            return False

    #删
    def delete(self, delete_words):
        try:
            # 执行SQL语句
            self.cursor.execute(delete_words)
            # 提交修改
            self.db.commit()
            return True
        except:
            # 发生错误时回滚
            self.db.rollback()
            return False

    #创建视图
    def create_view(self, create_view_words):
        try:
            # 执行SQL语句
            self.cursor.execute(create_view_words)
            # 提交修改
            self.db.commit()
            return True
        except:
            # 发生错误时回滚
            self.db.rollback()
            return False

    # 创建用户
    def create(self, create_words):
        try:
            # 执行SQL语句
            self.cursor.execute(create_words)
            # 提交修改
            self.db.commit()
            return True
        except:
            # 发生错误时回滚
            self.db.rollback()
            return False

    # 授予权限
    def grant(self, grant_words):
        try:
            # 执行SQL语句
            self.cursor.execute(grant_words)
            # 提交修改
            self.db.commit()
            return True
        except:
            # 发生错误时回滚
            self.db.rollback()
            return False

    # 授予权限
    def revoke(self, revoke_words):
        try:
            # 执行SQL语句
            self.cursor.execute(revoke_words)
            # 提交修改
            self.db.commit()
            return True
        except:
            # 发生错误时回滚
            self.db.rollback()
            return False

        # 授予权限

    def show(self, show_words):
        try:
            # 执行SQL语句
            self.cursor.execute(show_words)
            results = self.cursor.fetchall()
            return results
        except:
            # 发生错误时回滚
            self.db.rollback()
            return None

    def close_conn(self):
        self.cursor.close()
        self.db.close()


