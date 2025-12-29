# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 15:46:30 2025

@author: bened
"""

import sqlite3

connection = sqlite3.connect("chinook.db")
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

connection.commit()