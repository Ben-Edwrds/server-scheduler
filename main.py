# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 16:57:13 2025

@author: bened
"""

from db import get_connection, init_db, add_schedule, list_schedules
from settings import DB_PATH
from datetime import datetime
from scheduler import simulate_rtcwake

conn = get_connection(DB_PATH)
init_db(conn)

def check_datetime(prompt: str) -> str:
    while True:
        value = input(prompt)
        try:
            dt = datetime.strptime(value, "%Y-%m-%d %H:%M")
            return dt.strftime("%Y-%m-%d %H:%M")
        except ValueError:
            print("Use format: YYYY-MM-DD HH:MM")

name = input("Name: ")
sleep_time = check_datetime("Sleep time: YYYY-MM-DD HH:MM")
wake_time = check_datetime("Wake time: YYYY-MM-DD HH:MM")
mode = input("Mode (mem/disk/off): ")

new_id = add_schedule(conn, name, sleep_time, wake_time, mode, enabled=1)

print("Schedule added with ID: " + str(new_id))

print("schedules:")
for row in list_schedules(conn):
    print(row)

simulate_rtcwake(sleep_time, wake_time, mode)

