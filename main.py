# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 16:57:13 2025

@author: bened
"""

from db import get_connection, init_db, add_schedule, list_schedules
from settings import DB_PATH

conn = get_connection(DB_PATH)
init_db(conn)

new_id = add_schedule(
    conn,
    name="Night sleep",
    sleep_time="2026-01-01 23:30",
    wake_time="2026-01-02 07:00",
    mode="mem",
    enabled=1
)

print("schedule ID:", new_id)

print("schedules:")
for row in list_schedules(conn):
    print(row)

print("blablatest")
