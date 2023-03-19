import sqlite3

# connecting to the database
connection = sqlite3.connect("accounts_db.db")

# cursor
crsr = connection.cursor()

'''

# SQL command to create a table in the database

sql_command = """CREATE TABLE accounts (acc_num VARCHAR(11),name VARCHAR(30),branch VARCHAR(15));"""
crsr.execute(sql_command)

#To enter data into accounts table

com0="insert into accounts values('08985438536','Streak','VSKP')"
crsr.execute(com0)

com1 = "INSERT INTO accounts VALUES('12345678901', 'John Doe', 'DEL')"
crsr.execute(com1)

com2 = "INSERT INTO accounts VALUES('23456789012', 'Jane Smith', 'MUM')"
crsr.execute(com2)

com3 = "INSERT INTO accounts VALUES('34567890123', 'Bob Johnson', 'BLR')"
crsr.execute(com3)

com4 = "INSERT INTO accounts VALUES('45678901234', 'Alice Williams', 'HYD')"
crsr.execute(com4)

com5 = "INSERT INTO accounts VALUES('56789012345', 'Mike Brown', 'KOL')"
crsr.execute(com5)

com6 = "INSERT INTO accounts VALUES('67890123456', 'Sarah Davis', 'CHN')"
crsr.execute(com6)

com7 = "INSERT INTO accounts VALUES('78901234567', 'David Wilson', 'PUN')"
crsr.execute(com7)

com8 = "INSERT INTO accounts VALUES('89012345678', 'Karen Taylor', 'JAIP')"
crsr.execute(com8)

com9 = "INSERT INTO accounts VALUES('90123456789', 'Mark Thompson', 'LUCK')"
crsr.execute(com9)

com10 = "INSERT INTO accounts VALUES('01234567890', 'Emily Garcia', 'AHM')"
crsr.execute(com10)

'''

com = "SELECT * FROM accounts"
crsr.execute(com)
rows = crsr.fetchall()
for row in rows:
    print(row)


connection.close()


