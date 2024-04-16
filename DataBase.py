import sqlite3 as sq

with sq.connect("Game.db") as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS results(
        name TEXT,
        score INTEGER 
        )
    """)

    def insert_db(user, value):
        cur.execute("""
        INSERT INTO results values (?,?)
         
         """, (user, value))
        con.commit()


    def top_score():
        cur.execute(""" 
        SELECT name, max(score) FROM results
        GROUP by name
        ORDER by score DESC
        limit 3    
        """)
        return cur.fetchall()
