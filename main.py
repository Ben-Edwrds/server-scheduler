# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 16:57:13 2025

@author: bened
"""

from db import get_connection, init_db, add_schedule, list_schedules
from settings import DB_PATH

conn = get_connection(DB_PATH)
init_db(conn)

name = input("Name: ")
sleep_time = input("Sleep time (YYYY-MM-DD HH:MM): ")
wake_time = input("Wake time (YYYY-MM-DD HH:MM): ")
mode = input("Mode (mem/disk/off): ")
new_id = add_schedule(conn, name, sleep_time, wake_time, mode, enabled=1)

print("Schedule added with ID: " + str(new_id))

print("schedules:")
for row in list_schedules(conn):
    print(row)

print("blablatest")
