from sqlite3 import Cursor, Connection
import sqlite3
import random
from datetime import timedelta, datetime
from core.Database.basic import createConnectionToDatabase

def selectTable(str:str):
    con = createConnectionToDatabase()
    cur = con.cursor()
    
    cur.execute(f"select * from {str}")
    print(str, cur.fetchall())
    
    cur.close()
    con.close()

def clearTable(str:str):
    con = createConnectionToDatabase()
    cur = con.cursor()
    
    cur.execute(f"delete from {str}")
    print(str, cur.fetchall())
    con.commit()
    
    cur.close()
    con.close()

def testDate():
    con = createConnectionToDatabase()
    cur = con.cursor()
    
    today = datetime.today()

    cur.execute(f"select * from Days where day_date = '{today.strftime('%Y-%m-%d')}'")
    print(cur.fetchall())
    
    cur.close()
    con.close()


def printAllTables():
    con = createConnectionToDatabase()
    cur = con.cursor()

    cur.execute("select name from sqlite_master")
    res = cur.fetchall()

    print("Printing all tables")

    for a in res:
        string = a[0]
        if "sqlite" not in string:
            selectTable(string)

    cur.close()
    con.close()


def test_insert_key_ref():
    con = createConnectionToDatabase()
    cur = con.cursor()

    cur.execute("delete from Booking")
    con.commit()

    cur.execute("INSERT INTO Booking VALUES (?, ?, ?, ?, ?)", (0, 0, 0, 0, 1))
    con.commit()

    cur.execute("SELECT * FROM Booking")
    print(cur.fetchall())


    cur.close()
    con.close()