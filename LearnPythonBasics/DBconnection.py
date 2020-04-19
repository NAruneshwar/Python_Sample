# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 23:31:59 2019

@author: arunn
"""

import mysql.connector as DBC

mydb = DBC.connect(host="localhost", user = "root", password = "arun", database = "hemolog")
mycurcer = mydb.cursor()
mycurcer.execute("select * from users")
for k in mycurcer:
    print(k)