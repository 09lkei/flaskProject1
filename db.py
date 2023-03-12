import sqlite3
import os


def create_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    create_table_statement = """
        CREATE TABLE IF NOT EXISTS accounts (
        username VARCHAR(20) PRIMARY KEY,
        password VARCHAR(20) NOT NULL
        );
    """
    c.execute(create_table_statement)
    conn.commit()
    conn.close()

def create_user(username, password):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    insert_statement = f"""
    INSERT INTO accounts
    VALUES
        ('{username}',
        '{password}');
    """
    try:
        c.execute(insert_statement)
        conn.commit()
        conn.close()
    except:
        return False
    else:
        return True


