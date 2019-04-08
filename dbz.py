import sqlite3
conn = sqlite3.connect('dbz.db')
conn.execute('CREATE TABLE whistles (sno INTEGER PRIMARY KEY,sub Text,emp_name Text,message Text,remark Text DEFAULT NULL,date_su DATETIME DEFAULT CURRENT_TIMESTAMP,date_re Text DEFAULT NULL)')  
conn.execute('CREATE TABLE opinion (sno INTEGER PRIMARY KEY,sub Text,message Text,remark Text DEFAULT NULL,date_su DATETIME DEFAULT CURRENT_TIMESTAMP,date_re Text DEFAULT NULL)')  
conn.close()