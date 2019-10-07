#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  database.py
#  
#  
#  
import sqlite3
from sqlite3 import Error

con=None

def sql_connection():
    global con

    try:
        if con is None:
            con = sqlite3.connect('mydatabase.db')
            print("Connection is established: Database is created in memory")
    except Error:
        print(Error)
    finally:
        con.close()

def sql_insert():
    global con
    cursorObj = con.cursor()
    cursorObj.execute('SELECT 1 FROM dual')
    con.commit()

sql_connection()