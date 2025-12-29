# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 15:46:30 2025

@author: bened
"""

import sqlite3

def get_connection(str(db_path)) -> sqlite3.Connection:
    return sqlite3.connect(db_path)

def init_db(connection: sqlite3.Connection) -> None:
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS schedules (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        sleep_time TEXT NOT NULL,
        wake_time TEXT NOT NULL,
        mode TEXT NOT NULL,
        enabled INTEGER NOT NULL DEFAULT 1
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS runs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        schedule_id INTEGER NOT NULL,
        action TEXT NOT NULL,
        executed_at TEXT NOT NULL,
        status TEXT NOT NULL,
        FOREIGN KEY (schedule_id) REFERENCES schedules(id)
    );
    """)
    
    def add_schedule(connection, str(name), str(sleep_time), str(wake_time), str(mode), int(enabled) = 1):
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO schedules (name, sleep_time, wake_time, mode, enabled)
        VALUES (?, ?, ?, ?, ?)
    """, (name, sleep_time, wake_time, mode, enabled))
    connection.commit()
    return cursor.lastrowid

    def list_schedules(connection, bool(enabled) = false):
        cursor = connection.cursor()
        if enabled:
            cursor.execute("""
           SELECT id, name, sleep_time, wake_time, mode, enabled
           FROM schedules
           WHERE enabled = 1
           ORDER BY wake_time
       """)
   else:
       cursor.execute("""
           SELECT id, name, sleep_time, wake_time, mode, enabled
           FROM schedules
           ORDER BY wake_time
       """)
       return cursor.fetchall()

    connection.commit()
