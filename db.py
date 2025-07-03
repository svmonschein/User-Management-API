import sqlite3
from typing import Any
def init_db() -> None:
    # connect a database, if it not present the database will be created
    con = sqlite3.connect("user.db") 

    # create the cursor needed to execute sql statements
    cur = con.cursor()

    # create user table
    cur.execute("""
                CREATE TABLE IF NOT EXISTS user(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username text NOT NULL,
                    email text NOT NULL
                    is_blocked INTEGER,
                )""")
    # saves changes
    con.commit()
    # closes conection to database
    con.close()


def add_user(user: dict[str,Any]) -> None:
    # connect a database, if it not present the database will be created
    con = sqlite3.connect("user.db") 

    # create the cursor needed to execute sql statements
    cur = con.cursor()

    # insert user in to table
    cur.execute("""
                INSERT INTO user (username, email, is_blocked)
                VALUES (?, ?, ?)
                """,(user["username"],user["email"], user["is_blocked"]))
    # saves changes
    con.commit()
    # closes conection to database
    con.close()

def get_all_users() -> list[Any]:
    # connect a database, if it not present the database will be created
    con = sqlite3.connect("user.db") 

    # create the cursor needed to execute sql statements
    cur = con.cursor()

    # GET all users
    cur.execute("""
                SELECT *
                FROM user
                """)
    
    results = cur.fetchall()

    # closes conection to database
    con.close()

    return results

def get_user_by_id(id: int) -> list[Any]:
    # connect a database, if it not present the database will be created
    con = sqlite3.connect("user.db") 

    # create the cursor needed to execute sql statements
    cur = con.cursor()

    # GET all users
    cur.execute("""
                SELECT *
                FROM user 
                WHERE id = ?
                """,(id)) 
    
    results = cur.fetchall()

    # closes conection to database
    con.close()

    return results



    



