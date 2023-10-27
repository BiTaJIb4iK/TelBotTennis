from sqlite3 import Cursor, Connection
import sqlite3
from datetime import datetime, timedelta
from typing import List, Tuple, Optional

from core.Database.basic import createConnectionToDatabase

def getCourts():
    con = createConnectionToDatabase()
    cur = con.cursor()
    
    #check if there is user with the same id
    cur.execute(f"Select * from Courts")
    res = cur.fetchall()

    cur.close()
    con.close()

    return res

def getDays():
    con = createConnectionToDatabase()
    cur = con.cursor()
    

    today = datetime.today()
    week_later = today + timedelta(days=6)
    #check if there is user with the same id
    cur.execute(f"Select * from Days where day_date between '{today.strftime('%Y-%m-%d')}' and '{week_later.strftime('%Y-%m-%d')}'")
    res = cur.fetchall()

    cur.close()
    con.close()

    return res

def getTimesAvailable(date_id: int):
    con = createConnectionToDatabase()
    cur = con.cursor()
    
    #check if there is user with the same id
    cur.execute(f"Select * from Time where time_id not in (select book_time from Booking where book_day = {date_id})")
    res = cur.fetchall()

    cur.close()
    con.close()

    return res

