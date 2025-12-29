# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 19:01:53 2025

@author: bened
"""

from datetime import datetime

FMT = "%Y-%m-%d %H:%M"

def simulate_rtcwake(sleep_time: str, wake_time: str, mode: str) -> None:
    sleep_dt = datetime.strptime(sleep_time, FMT)
    wake_dt = datetime.strptime(wake_time, FMT)
    wake_ts = int(wake_dt.timestamp())

    print("\n[SIMULATION]")
    print(f"Sleep at: {sleep_dt}")
    print(f"Wake  at: {wake_dt}")
    print(f"Would run: rtcwake -m {mode} -t {wake_ts}")
