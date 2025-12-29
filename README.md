# Server Scheduler (Python)

## Description
This Python application allows a user to schedule server sleep and wake times.
Schedules are stored in a SQLite database and can be simulated using the `rtcwake` command.

The application was built as part of the course *Programming in Python*.

---

## Features
- Add schedules via terminal input
- Store schedules in a SQLite database
- Validate datetime input (YYYY-MM-DD HH:MM)
- Simulate server sleep/wake behaviour (no real system commands executed)
- Export schedules to CSV
- Optional CSV import
- Uses object-oriented programming (Scheduler class)