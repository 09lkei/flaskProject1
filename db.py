import sqlite3
import os


def create_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    create_table_statement = """
        CREATE TABLE IF NOT EXISTS accounts (
        username VARCHAR(20) PRIMARY KEY,
        password VARCHAR(20) NOT NULL,
        yeargroup CHAR(2) NOT NULL
        );
    """
    c.execute(create_table_statement)
    conn.commit()
    conn.close()

def create_user(username, password, yeargroup):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    insert_statement = f"""
    INSERT INTO accounts
    VALUES
        ('{username}',
        '{password}',
        '{yeargroup}');
    """
    try:
        c.execute(insert_statement)
        conn.commit()
        conn.close()
    except:
        return False
    else:
        return True

def login(username, password):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    login_statement = f"""
    SELECT username FROM accounts where username = '{username}' AND PASSWORD = '{password}'
    """
    c.execute(login_statement)
    if c.fetchone():
        return True
    else:
        return False

def delete_user(username):
    conn = sqlite3.connect("database.db")
    c=conn.cursor()
    delete_statement = f"""
    DELETE FROM accounts WHERE username={username}
    """
    c.execute(delete_statement)

def user_details(username):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    detail_statement = f"""
    SELECT username, yeargroup FROM accounts where username = '{username}'
    """
    c.execute(detail_statement)
    return c.fetchone()

def update_user(username, password, yeargroup):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    update_statement = f"""
        UPDATE yeargroup SET password = '{password}', yeargroup = '{yeargroup}', WHERE username = '{username}'
        """
    c.execute(update_statement)
