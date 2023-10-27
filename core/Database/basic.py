from sqlite3 import Cursor, Connection
import sqlite3
from datetime import timedelta, datetime


def createConnectionToDatabase() -> Connection:
    return sqlite3.connect("test.db")

#better not to use this function often
def setUpDataBaseDefault():
    createDataBaseTables()
    fillBadges()
    fillCourts()
    fillDays()
    fillTime()

def createDataBaseTables():
    con = createConnectionToDatabase()
    cur = con.cursor()

    cur.executescript("""
-- Create the "Badges" table
CREATE TABLE IF NOT EXISTS Badges (
    badge_id INT PRIMARY KEY,
    badge_name CHAR(50),
    badge_preview CHAR(10)
);

-- Create the "User" table
CREATE TABLE IF NOT EXISTS User (
    user_id INT PRIMARY KEY,
    user_name char(129),
    user_register_date DATE,
    user_rating FLOAT,
    user_view_badge INT,
    user_banned BOOLEAN,
    user_strikes INT,
    FOREIGN KEY (user_view_badge) REFERENCES Badges(badge_id)
);

-- Create the "User_badges" table with foreign keys
CREATE TABLE IF NOT EXISTS User_badges (
    user_id INT,
    badge_id INT,
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (badge_id) REFERENCES Badges(badge_id)
);

-- Create the "Time" table
CREATE TABLE IF NOT EXISTS Time (
    time_id INT PRIMARY KEY,
    time_name CHAR(10)
);

-- Create the "Courts" table
CREATE TABLE IF NOT EXISTS Courts (
    court_id INT PRIMARY KEY,
    court_name CHAR(50),
    court_location CHAR(50)
);

-- Create the "Days" table
CREATE TABLE IF NOT EXISTS Days (
    day_id INT PRIMARY KEY,
    day_date DATE
);

-- Create the "Booking" table with foreign keys
CREATE TABLE IF NOT EXISTS Booking (
    book_id INT PRIMARY KEY,
    court_id INT,
    user_id INT,
    book_day INT,
    book_time INT,
    FOREIGN KEY (court_id) REFERENCES Courts(court_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (book_day) REFERENCES Days(day_id),
    FOREIGN KEY (book_time) REFERENCES Time(time_id)
);""")

    con.commit()

    cur.close()
    con.close()


def fillDays():
    con = createConnectionToDatabase()
    cur = con.cursor()

    cur.execute("delete from Days")
    con.commit()

    today = datetime.today()
    years = 10
    end_date = today + timedelta(days=365 * years)

    # Generate and insert dates into the table
    current_date = today

    id = 0
    while current_date <= end_date:
        cur.execute("INSERT INTO Days VALUES (?, ?)", (id, current_date.strftime('%Y-%m-%d'),))
        current_date += timedelta(days=1)
        id+=1

    con.commit()

    cur.close()
    con.close()

def fillTime():
    con = createConnectionToDatabase()
    cur = con.cursor()

    cur.execute("delete from Time")
    con.commit()

    id = 0
    while id <= 23:
        cur.execute("INSERT INTO Time VALUES (?, ?)", (id, str(id)+":00 - "+str(id+1)+":00"))
        id+=1

    con.commit()

    cur.close()
    con.close()

def fillCourts():
    con = createConnectionToDatabase()
    cur = con.cursor()

    cur.execute("delete from Courts")
    con.commit()

    cur.executemany("INSERT INTO Courts VALUES (?, ?, ?)", [(0, "Теннісний корт на харквіській", "метро Харківська, школа 212"), (1, "Теннісний корт у парку Перемоги", "парк перемоги")])
    con.commit()

    cur.close()
    con.close()

def fillBadges():
    con = createConnectionToDatabase()
    cur = con.cursor()

    cur.execute("delete from Badges")
    con.commit()

    cur.executemany("INSERT INTO Badges VALUES (?, ?, ?)", [(0, "Developer", "<b>[DEV]</b>"), (1, "New", "[new]"), (2, "Administrator", "[Admin]"), (3, "Champion", "[Champ]"), (4, "Elder", "[Old]"), (5, "Trust", "[Trust]"), (6, "Tipper", "[tip]"), (7, "Supporter", "[Sup]"), (8, "Donator", "[Don]"),])
    con.commit()

    cur.close()
    con.close()




