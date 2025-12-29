# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 16:57:13 2025

@author: bened
"""

from db import get_connection, init_db
conn = get_connection("project.db")
init_db(conn)

print("blablatest")