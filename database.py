import os
import sqlite3

DB_NAME = os.getenv("DB_NAME", "applications.db")


def get_connection():
    return sqlite3.connect(DB_NAME)

def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS applications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company TEXT NOT NULL,
        position TEXT NOT NULL,
        status TEXT NOT NULL
    )
    """)

    connection.commit()
    connection.close()


def add_application(company, position, status):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO applications (company, position, status)
    VALUES (?, ?, ?)
    """, (company, position, status))

    connection.commit()

    application_id = cursor.lastrowid

    connection.close()

    return application_id

def list_applications():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM applications")

    applications = cursor.fetchall()

    connection.close()

    return applications


if __name__ == "__main__":
    create_table()

def update_status(application_id, new_status):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    UPDATE applications
    SET status = ?
    WHERE id = ?
    """, (new_status, application_id))

    connection.commit()
    connection.close()

def delete_application(application_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    DELETE FROM applications
    WHERE id = ?
    """, (application_id,))

    deleted_count = cursor.rowcount

    connection.commit()
    connection.close()

    return deleted_count

def find_application(application_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    SELECT * FROM applications
    WHERE id = ?
    """, (application_id,))

    application = cursor.fetchone()

    connection.close()

    return application