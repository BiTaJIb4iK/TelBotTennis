from sqlite3 import Cursor, Connection
import sqlite3
from datetime import datetime
from typing import List, Tuple, Optional

from core.Database.basic import createConnectionToDatabase

def checkValidUser(user_id:int) -> bool:
    con = createConnectionToDatabase()
    cur = con.cursor()
    
    #check if there is user with the same id
    cur.execute(f"Select * from User where user_id = {user_id}")
    res = cur.fetchall()

    #check if there are any rows in return of command
    found = False
    for a in res:
        found = True
        break
    
    cur.close()
    con.close()

    return found

def addUser(user_id: int, user_name: str):
    #Handle adding new user
    if checkValidUser(user_id) == False:
        con = createConnectionToDatabase()
        cur = con.cursor()

        today = datetime.today()

        cur.execute("INSERT INTO User VALUES (?, ?, ?, ?, ?, ?, ?)", (user_id, user_name, today.strftime("'%Y-%m-%d'"), 0, 1, False, 0))
        con.commit()

        print("Added new user : " + str(user_id))

        #Add new badge "New" player
        addBadge(user_id, 1) 

        cur.close()
        con.close()
    else:
        print("User already exists!")

    

def getUser(user_id: int) -> Optional[Tuple[int, str, str, float, int, bool, int]]:
    con = createConnectionToDatabase()
    cur = con.cursor()
    
    #check if there is user with the same id
    cur.execute(f"Select * from User where user_id = {user_id}")
    res = cur.fetchone()

    cur.close()
    con.close()

    return res

def checkValidBadge(badge_id:int) -> bool:
    con = createConnectionToDatabase()
    cur = con.cursor()
    
    #check if there is user with the same id
    cur.execute(f"Select * from Badges where badge_id = {badge_id}")
    res = cur.fetchall()

    #check if there are any rows in return of command
    found = False
    for a in res:
        found = True
        break
    
    cur.close()
    con.close()
    
    return found

def addBadge(user_id: int, badge_id: int):
    con = createConnectionToDatabase()
    cur = con.cursor()
    
    #Handle adding new user
    if checkValidBadge(badge_id) & checkValidUser(user_id) == True:
        #TODO add badge new to the user 

        cur.execute("INSERT INTO User_badges VALUES (?, ?)", (user_id, badge_id))
        con.commit()

        print("Added badge badge : " + str(badge_id) + " to user : " + str(user_id))
    else:
        print(f"Can't add badge ({badge_id}) to user ({user_id})")

    cur.close()
    con.close()

def getUserBadges(user_id: int) -> List[int]:
    con = createConnectionToDatabase()
    cur = con.cursor()
    
    cur.execute(f"Select * from User_badges where user_id = {user_id}")
    res = cur.fetchall()

    array = []

    for a in res:
        array.append(a[1])

    print(array)

    cur.close()
    con.close()

    return array