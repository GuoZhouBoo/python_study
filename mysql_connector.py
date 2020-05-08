#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : mysql_connector.py
# Author: gsm
# Date  : 2020/5/7
import mysql.connector


def connectdb():
    print('正在连接到mysql服务器...')
    # 打开数据库连接
    # 用户名:root, 密码:1213, 用户名和密码需要改成自己的mysql用户名和密码
    db = mysql.connector.connect(host="10.1.21.161", user="root", passwd="1213", database="python_connection_test",
                                 use_unicode=True)
    print('成功连接到数据库')
    return db


def createtable(db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 如果存在表course先删除
    cursor.execute("DROP TABLE IF EXISTS course")
    sql = """CREATE TABLE course (
            ID INT NOT NULL primary key,
            Name CHAR(120),
            teacher_id INT,
            course_type_id int )"""

    # 创建course表
    cursor.execute(sql)
    print '创建course表成功'


def insertdb(db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 插入语句
    sql = """INSERT INTO course
         VALUES (1, '论语', 1211, 0),
                (2, '计算机网络', 1212, 1),
                (3, '英语', 1213, 2),
                (4, '高数', 1214, 3),
                (5, '线性代数', 1215, 4),
                (6, '数据结构', 1216, 5)"""
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # Rollback in case there is any error
        print '插入数据失败!'
        db.rollback()


def querydb(db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT * FROM course"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            ID = row[0]
            Name = row[1]
            teacher_id = row[2]
            course_type_id = row[3]
            # 打印结果
            print "ID: %s, Name: %s, teacher_id: %d, course_type_id: %d" % \
                  (ID, Name, teacher_id, course_type_id)
    except:
        print "Error: unable to fecth data"


def updatedb(db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 更新语句
    sql = "UPDATE course SET teacher_id = teacher_id + 1 WHERE ID = '%d'" % (1)

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        print '更新数据失败!'
        # 发生错误时回滚
        db.rollback()


def deleterow(db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 删除语句
    sql = "DELETE FROM course WHERE ID = '%d'" % (1)

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交修改
        db.commit()
    except:
        print '删除数据失败!'
        # 发生错误时回滚
        db.rollback()


def closedb(db):
    print '关闭连接'
    db.close()


if __name__ == '__main__':
    db = connectdb()
    createtable(db)
    insertdb(db)
    print 'insert 之后的数据：'
    querydb(db)
    updatedb(db)
    print 'update 之后的数据：'
    querydb(db)
    deleterow(db)
    print 'delete 之后的数据：'
    querydb(db)
    closedb(db)
