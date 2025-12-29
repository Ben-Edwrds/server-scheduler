# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 19:01:53 2025

@author: bened
"""
from datetime import datetime

class Scheduler:
    DATETIME_FMT = "%Y-%m-%d %H:%M"

    def __init__(self, schedules):
        self.schedules = schedules

    def simulate_all(self):
        print("\nSIMULATION:")
        for s in self.schedules:
            self.simulate(s)

    def simulate(self, schedule):
        _, name, sleep_time, wake_time, mode, _ = schedule
        
        sleep_dt = datetime.strptime(sleep_time, self.DATETIME_FMT)
        wake_dt = datetime.strptime(wake_time, self.DATETIME_FMT)
        wake_ts = int(wake_dt.timestamp())

        print(name)
        print("Sleep at: ", sleep_dt)
        print("Wake  at: ", wake_dt)
        print("Command: rtcwake -m ", mode, " -t ",wake_ts)
